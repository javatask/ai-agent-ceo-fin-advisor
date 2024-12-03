# AWS Bedrock Agent Auto-Deployment Tool 🚀

A streamlined solution for deploying AWS Bedrock Agents with minimal configuration. Deploy your AI-powered agent with a single command.

## 🛠️ Quick Start

### Prerequisites

Install required tools:
```bash
# AWS CLI v2
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
unzip awscliv2.zip && \
sudo ./aws/install

# AWS SAM CLI
curl -L https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip -o sam-cli.zip && \
unzip sam-cli.zip -d sam-installation && \
sudo ./sam-installation/install

# jq - JSON processor
sudo apt-get update && sudo apt-get install -y jq python3-pip  # Ubuntu/Debian
# or
sudo yum install -y jq python3-pip  # Amazon Linux/RHEL
```

### AWS Configuration

1. Set up SSO access:
```bash
aws configure sso
aws sso login
```

2. Verify required permissions:
- ✓ Lambda Management
- ✓ IAM Role Creation
- ✓ CloudFormation Operations
- ✓ Bedrock Access
- ✓ S3 Bucket Management
- ✓ SES Configuration

## 💫 Deployment

```bash
git clone https://github.com/yourusername/bedrock-agent-deployer
cd bedrock-agent-deployer
chmod +x one-click.sh
./one-click.sh
```

## ⚙️ Architecture Overview

The deployment process:
1. Resource naming with UUID generation
2. Lambda function deployment via SAM
3. ARN retrieval and configuration
4. Agent deployment through CloudFormation
5. Automated agent initialization

## 🔍 Monitoring & Troubleshooting

### Common Issues

1. **Deployment Failures**
   - Check CloudFormation Events tab
   - Verify AWS SSO session: `aws sts get-caller-identity`
   - Review IAM permissions

2. **Resource Limits**
   - Monitor service quotas
   - Request limit increases if needed

## 🧹 Resource Cleanup

```bash
# Replace {suffix} with your deployment suffix
aws cloudformation delete-stack --stack-name ceo-fin-report-{suffix}
aws cloudformation delete-stack --stack-name ai-agent-finance-tool-{suffix}
```

## ⚠️ Important Notes

- **Costs**: Monitor AWS resource usage
- **Security**: Protect AWS credentials
- **Updates**: Check repository for latest features

## 📝 Contributing

1. Fork repository
2. Create feature branch
3. Submit pull request

## 📜 License

MIT License - See LICENSE file