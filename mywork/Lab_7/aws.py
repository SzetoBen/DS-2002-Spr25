import boto3
import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Basketball.png/330px-Basketball.png'
response = requests.get(url)
bucket = 'ds2002-gbf5yb'
local_file = 'basketball.jpg'
s3_file_name = 'basketball.jpg'
expires_in = 10 

if response.status_code == 200:
    with open(local_file, 'wb') as f:
        f.write(response.content)
    print("Image saved")
else:
    print("Failed to save.")

s3 = boto3.client('s3', region_name="us-east-1")

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = s3_file_name,
    ACL = 'public-read',
)

presign_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': s3_file_name},
    ExpiresIn=expires_in
)

print(presign_url)