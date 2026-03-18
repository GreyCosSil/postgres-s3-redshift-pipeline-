import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

AWS_BUCKET = os.getenv("AWS_BUCKET")

file_path = "data/customers.csv"

today = datetime.today().strftime('%Y-%m-%d')
s3_key = f"raw/customers/load_date={today}/customers.csv"

s3 = boto3.client("s3")

s3.upload_file(file_path, AWS_BUCKET, s3_key)

print(f"Upload realizado: s3://{AWS_BUCKET}/{s3_key}")
