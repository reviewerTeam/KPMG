#!/bin/bash
instanceid=$1
type=$2
aws ec2 describe-instance-attribute --instance-id  $instanceid --attribute instanceType --region eu-west-1 |  jq --arg v "$type" -r '.[$v]'
