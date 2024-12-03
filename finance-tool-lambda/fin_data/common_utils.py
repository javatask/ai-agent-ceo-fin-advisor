import boto3
import os
from botocore.exceptions import ClientError
from datetime import datetime

def send_email(
    subject: str,
    html_body: str,
    aws_region: str = 'us-east-1'
) -> dict:
    """
    Send email using AWS SES.
    
    Args:
        subject: Email subject
        html_body: Email body (HTML supported)
        aws_region: AWS region where SES is configured
        
    Returns:
        dict: AWS SES response
        
    Raises:
        ClientError: If email sending fails
    """
    client = boto3.client('ses', region_name=aws_region)
    
    # Get configuration from environment variables
    email_from = os.environ['EMAIL_FROM']
    email_to = os.environ['EMAIL_TO']
   
    email_message = {
        'Subject': {'Data': subject},
        'Body': {'Html': {'Data': html_body}}
    }
    
    destination = {
        'ToAddresses': [email_to]
    }
    
    try:
        response = client.send_email(
            Source=email_from, 
            Destination=destination,
            Message=email_message
        )
        return response
        
    except ClientError as e:
        print(e)
        raise e


def save_html_to_s3(html_content):
    """Save HTML content to S3 bucket with timestamp."""
    # Get configuration from environment variables
    bucket_name = os.environ['BUCKET_NAME']
    prefix = os.environ['REPORTS_PREFIX']
    
    s3 = boto3.client('s3')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    key = f"{prefix}/report_{timestamp}.html"
    
    try:
        s3.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=html_content,
            ContentType='text/html'
        )
        return f"s3://{bucket_name}/{key}"
    except Exception as e:
        raise Exception(f"Failed to upload to S3: {str(e)}")
