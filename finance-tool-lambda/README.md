# Finance Tool Lambda

Serverless financial analytics application using AWS Lambda with Python 3.13.

## Overview

Processes financial data and generates reports, storing them in S3 with email notifications.

## Architecture

- Python 3.13 Runtime
- AWS Services: Lambda, S3, Lambda Layers (Pandas), SES

## Prerequisites

- AWS CLI & SAM CLI
- Python 3.10
- AWS Account

## Environment Variables

```bash
EMAIL_FROM=sender@example.com
EMAIL_TO=recipient@example.com
BUCKET_NAME=reports-bucket
REPORTS_PREFIX=financial/
```

## Project Structure

```
finance-tool-lambda/
├── fin_data/          # Lambda function code
├── layers/            # Lambda layers (Pandas)
└── template.yaml      # SAM template
```

## Deployment

```bash
# Build
sam build

# Deploy with guided setup
sam deploy --guided
```

## Local Development

```bash
# Test function locally
sam local invoke AnalyticsFunction
```

## Lambda Layer

- Name: python-utils
- Contents: Pandas utilities
- Runtime: Python 3.13

## IAM Permissions

- S3: CRUD operations
- SES: Email sending

## Important Notes

- Monitor AWS costs
- Maintain AWS credentials
- Keep dependencies updated
- Configure S3 permissions

## License

MIT License