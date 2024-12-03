#!/bin/bash
# I assume that you did `aws sso login` and have permissions to create Lambdas, AI Agents, IAM roles etc
# Navigate to Lambda directory
RANDOM_SUFFIX=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1)
cd finance-tool-lambda

# Build and deploy SAM application
sam build
sam deploy --stack-name ai-agent-finance-tool-$RANDOM_SUFFIX

# Get the Lambda ARN and store it in a variable
LAMBDA_ARN=$(sam list stack-outputs --stack-name ai-agent-finance-tool-$RANDOM_SUFFIX --output json | jq -r '.[] | select(.OutputKey == "AnalyticsFunction") | .OutputValue')

# Check if Lambda ARN was retrieved successfully
if [ -z "$LAMBDA_ARN" ]; then
    echo "Error: Failed to retrieve Lambda ARN"
    exit 1
fi

# Deploy AI Agent
cd ..

# Generate agent-params.json with the Lambda ARN
echo "[\"LambdaFunctionArn=$LAMBDA_ARN\",\"AgentName=demo-ceo-fin-report-$RANDOM_SUFFIX\"]" > agent-params.json

echo "Successfully created agent-params.json with Lambda ARN: $LAMBDA_ARN"

# Deploy Agent stack
echo "Deploying Bedrock Agent stack..."
aws cloudformation deploy \
    --template-file bedrock-agent-stack.yaml \
    --stack-name ceo-fin-report-$RANDOM_SUFFIX \
    --parameter-overrides file://agent-params.json \
    --capabilities CAPABILITY_IAM 

echo "Deployment completed successfully!"

# Prepare Agent
AGENT_ID=$(aws cloudformation describe-stacks --stack-name ceo-fin-report-$RANDOM_SUFFIX --output text --query 'Stacks[0].Outputs[?OutputKey==`AgentId`].OutputValue')
aws bedrock-agent prepare-agent --agent-id $AGENT_ID