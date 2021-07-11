#!/bin/bash
export VM_NAME=ECS
export SNAP_ID=ae0ebecd-0b6a-44f2-9b86-029df520e4a6
export AWS_PAGER=""

export SERVER_CERT_ARN=$(aws acm list-certificates --query "CertificateSummaryList[?DomainName=='server'].CertificateArn" --output text)
if [ -z "$SERVER_CERT_ARN" ] ; then
    export SERVER_CERT_ARN=$(aws acm import-certificate --certificate fileb://pki/server.crt --private-key fileb://pki/server.key --certificate-chain fileb://pki/ca.crt --tags Key=Name,Value=server | jq -r .CertificateArn)
fi

export CLIENT_CERT_ARN=$(aws acm list-certificates --query "CertificateSummaryList[?DomainName=='client1.domain.tld'].CertificateArn" --output text)
if [ -z "$CLIENT_CERT_ARN" ] ; then
    export CLIENT_CERT_ARN=$(aws acm import-certificate --certificate fileb://pki/client1.domain.tld.crt --private-key fileb://pki/client1.domain.tld.key --certificate-chain fileb://pki/ca.crt --tags Key=Name,Value=client1.domain.tld | jq -r .CertificateArn)
fi

cdk deploy --require-approval never --parameters "clientCertificateArn=$CLIENT_CERT_ARN" --parameters "serverCertificateArn=$SERVER_CERT_ARN" 

prlctl snapshot-switch $VM_NAME -i $SNAP_ID

echo "Creating activation"
aws ssm create-activation --iam-role ecsExternalInstanceRole >activation.txt

export ACT_ID=$(jq -r .ActivationId <activation.txt)
export ACT_CODE=$(jq -r .ActivationCode <activation.txt)
rm -f activation.txt

echo "ActivationID is $ACT_ID - Activation code is $ACT_CODE"

echo "Building VPN config"
( cd vpn && ./build.sh)

echo "Starting VM and configure ECS Anywhere"
prlctl exec ECS --user root "curl --proto https -o /tmp/ecs-anywhere-install.sh https://amazon-ecs-agent.s3.amazonaws.com/ecs-anywhere-install-latest.sh && bash /tmp/ecs-anywhere-install.sh --region $AWS_DEFAULT_REGION --cluster AnywhereCluster --activation-id $ACT_ID --activation-code $ACT_CODE"

echo "Starting VPN"
export RELPATH=$(python -c 'import os, sys; print(os.path.relpath(sys.argv[1],sys.argv[2]))' $(pwd) $HOME)
prlctl exec ECS --user root openvpn --daemon openvpn --config /media/psf/Home/$RELPATH/vpn/config.conf

echo "Starting ECS task"
aws ecs update-service --cluster AnywhereCluster --service nginx --desired-count 1 --force-new-deployment