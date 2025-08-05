import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # You can either generate this file OR expect it to already exist
    archive_path = '/tmp/flaskapp.tar.gz'

    # Simulating file creation (optional)
    with open(archive_path, 'w') as f:
        f.write('Dummy Flask App Backup Content')

    s3.upload_file(
        archive_path,
        'static-bucket377',
        'backup/flaskapp.tar.gz'
    )

    return {
        'statusCode': 200,
        'body': 'Backup uploaded to S3 successfully.'
    }

