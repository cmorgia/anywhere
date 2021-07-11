#!/bin/sh
export ENDPOINT=$(aws cloudformation describe-stacks --stack-name AnywhereStack --query "Stacks[0].Outputs[?OutputKey=='Endpoint'].OutputValue" --output text)
envsubst <_config.conf >config.conf
echo "<ca>" >>config.conf
cat ../pki/ca.crt >>config.conf
echo "</ca>" >>config.conf
echo "<cert>" >>config.conf
cat ../pki/client1.domain.tld.crt | sed -ne '/-----BEGIN CERTIFICATE-----/,$p' >>config.conf
echo "</cert>" >>config.conf
echo "<key>" >>config.conf
cat ../pki/client1.domain.tld.key >>config.conf
echo "</key>" >>config.conf