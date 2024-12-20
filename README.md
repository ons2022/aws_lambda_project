# AWS Lambda Image Resizer

This project demonstrates a serverless application that automatically resizes images uploaded to an S3 bucket using AWS Lambda.

## Setup Instructions

1. **Create S3 Buckets**:
   - Source bucket: Store original images.
   - Destination bucket: Store resized images.

2. **Deploy the Lambda Function**:
   - Use the code in `lambda_function.py`.
   - Configure permissions for the Lambda execution role to access S3.

3. **Set Up an S3 Trigger**:
   - In the source bucket settings, add a trigger to invoke the Lambda function.

## Testing Instructions

1. Upload an image to the source bucket.
2. Verify that a resized image appears in the destination bucket.

## Technologies Used
- AWS Lambda
- AWS S3
- Python
#   a w s _ l a m b d a _ p r o j e c t  
 