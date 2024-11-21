import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    destination_bucket = 'bucketons'

    # Get the image from the source bucket
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    image = Image.open(io.BytesIO(response['Body'].read()))

    # Resize the image
    resized_image = image.resize((100, 100))

    # Save the resized image in memory
    output = io.BytesIO()
    resized_image.save(output, format='JPEG')
    output.seek(0)

    # Upload the resized image to the destination bucket
    destination_key = f"resized-{source_key}"
    s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=output, ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': f"Image resized and saved to {destination_bucket}/{destination_key}"
    }
