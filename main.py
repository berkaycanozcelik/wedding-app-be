from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

app = FastAPI()

origins = [
    "http://54.93.105.108",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Your Netlify domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS S3 configuration
s3_client = boto3.client(
    's3',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

bucket_name = os.getenv('S3_BUCKET_NAME')

@app.post("/upload-file/")
async def upload_file(files: List[UploadFile] = File(...)):
    try:
        for file in files:
            # Determine if file is an image or video based on content type or extension
            file_extension = file.filename.split(".")[-1].lower()
            if file.content_type.startswith('image/') or file_extension in ["jpg", "jpeg", "png", "gif"]:
                folder_name = "images"
            elif file.content_type.startswith('video/') or file_extension in ["mp4", "mov", "avi", "mkv"]:
                folder_name = "videos"
            else:
                raise HTTPException(status_code=400, detail="Unsupported file type")

            # Construct the S3 object key with folder prefix
            s3_key = f"{folder_name}/{file.filename}"

            # Upload file to S3
            s3_client.upload_fileobj(file.file, bucket_name, s3_key)
            print(f"Uploaded {file.filename} to {folder_name}/")

        return JSONResponse(content={"message": "Files uploaded successfully!"}, status_code=200)
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="Credentials not available")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/healthcheck/")
async def health_check():
    try:
        # Perform a basic operation to check if the S3 connection is working
        s3_client.list_buckets()  # This is a simple way to check S3 connectivity
        return JSONResponse(content={"status": "Healthy"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"status": "Unhealthy", "detail": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
