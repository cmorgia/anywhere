#!/bin/bash
export VM_NAME=ECS
export SNAP_ID=bf6d234e-e971-4f78-83db-6825c7d93f27
export BUCKET=testecsanywhere
sam build && sam deploy --stack-name TestECSAnywhere --s3-bucket $BUCKET --capabilities CAPABILITY_NAMED_IAM
prlctl snapshot-switch $VM_NAME -i $SNAP_ID
aws ssm create-activation --iam-role ecsExternalInstanceRole >activation.txt
ACT_ID=$(jq -r .ActivationId <activation.txt)
ACT_CODE=$(jq -r .ActivationCode <activation.txt)
rm -f activation.txt
prlctl exec ECS --user root "curl --proto https -o /tmp/ecs-anywhere-install.sh https://amazon-ecs-agent.s3.amazonaws.com/ecs-anywhere-install-latest.sh && bash /tmp/ecs-anywhere-install.sh --region eu-central-1 --cluster TestCluster --activation-id $ACT_ID --activation-code $ACT_CODE"
prlctl exec ECS --user root openvpn --daemon openvpn --config /media/psf/Home/devel/anywhere/vpn/config.conf
