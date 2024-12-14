import boto3

class S3Uploader:
    def upload(self, local_file, bucket, s3_key):
        s3 = boto3.client('s3')
        s3.upload_file(local_file, bucket, s3_key)