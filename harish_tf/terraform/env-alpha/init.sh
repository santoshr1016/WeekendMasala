#!/bin/bash -e

SUFFIX="priscilacarval"

if [ -z "$SUFFIX" ]
then
    echo "Please edit this file and put your suffix here"
    exit 1
fi

terraform init \
    -backend-config="bucket=skip-incubator-terraform-devops" \
    -backend-config="key=tf-state/alpha-${SUFFIX}.tfstate" \
    -backend-config="region=eu-west-1"