import json
import boto3

def lambda_handler(event, context):
    SENDER = "yatindrap6@gmail.com"      
    RECIPIENT = "yatindrap6@gmail.com"    
    AWS_REGION = "ap-south-1"
    SUBJECT = "Test Email from Lambda via SES"
    
   
    BODY_TEXT = "This is a test email sent from AWS Lambda using Amazon SES."

   
    client = boto3.client('ses', region_name=AWS_REGION)
    
   
    try:
        response = client.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': SUBJECT},
                'Body': {
                    'Text': {'Data': BODY_TEXT}
                }
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Email sent! Message ID: ' + response['MessageId'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending email: ' + str(e))
        }
