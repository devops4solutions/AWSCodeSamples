import boto3
bucketName = "devops4solutions-source"
bucketRegion = "us-east-2"

# Creates an s3 Resource; this is a higher level API type service for s3.
s3 = boto3.resource('s3')

# Creates a bucket
bucket = s3.create_bucket(ACL='private',Bucket=bucketName,CreateBucketConfiguration={'LocationConstraint': bucketRegion})
