#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTPATH

git clone https://github.com/OpenVPN/easy-rsa.git

cd easy-rsa/easyrsa3
./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa build-server-full server nopass
./easyrsa build-client-full client1.domain.tld nopass

cp pki/ca.crt ../../
cp pki/issued/server.crt ../../
cp pki/private/server.key ../../
cp pki/issued/client1.domain.tld.crt ../../
cp pki/private/client1.domain.tld.key ../../

cd ../..
export SERVER_CERT_ARN=$(aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt | jq -r .CertificateArn)
export CLIENT_CERT_ARN=$(aws acm import-certificate --certificate fileb://client1.domain.tld.crt --private-key fileb://client1.domain.tld.key --certificate-chain fileb://ca.crt | jq -r .CertificateArn)

cat <<EOL >../params.sh
export SERVER_CERT_ARN=${SERVER_CERT_ARN}
export CLIENT_CERT_ARN=${CLIENT_CERT_ARN}
EOL