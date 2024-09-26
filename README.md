
# Wedding Image & Video Uploader - Backend

This is the backend service for the Wedding Image & Video Uploader, developed using FastAPI. It provides API endpoints to upload images and videos to an AWS S3 bucket. This project is a hands-on exercise aimed at demonstrating my skills in FastAPI, AWS S3 integration, Docker, and containerized app deployment.

## Features

- Upload multiple images or videos.
- Store files in AWS S3 with separate folders for images and videos.
- Basic health check endpoint for monitoring service status.
- CORS middleware enabled to allow communication with the frontend.

## Technologies Used

- FastAPI
- Python 3.11
- AWS S3 for file storage
- Docker
- Uvicorn (ASGI server)

## Getting Started

### Prerequisites

- Python 3.8+ installed.
- AWS S3 bucket and credentials set up.
- Docker installed. [Download Docker here](https://www.docker.com/get-started)
- `python-multipart` for handling file uploads.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/wedding-uploader-backend.git
cd wedding-uploader-backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your `.env` file with the following variables:

```bash
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=your-region
S3_BUCKET_NAME=your-bucket-name
```

### Running the Application

To start the FastAPI app locally, run:

```bash
uvicorn main:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

### API Endpoints

- `POST /upload-file/`: Uploads one or multiple images/videos to S3.
- `GET /healthcheck/`: Checks the health of the API and S3 connection.

### Docker Setup

This app is containerized using Docker for easier deployment.

1. Build the Docker image:

```bash
docker build -t wedding-backend .
```

2. Run the container:

```bash
docker run -p 8000:8000 --name wedding-be-app wedding-backend
```

### Deployment

You can deploy the backend service using platforms like AWS ECS, Google Cloud Run, or other container orchestration platforms. Ensure the necessary environment variables are set during deployment.

## Purpose

This project was developed to demonstrate my skills in Docker, FastAPI, and AWS S3 integration. It serves as a practical exercise in deploying a full-stack web application with modern technologies.

## License

This project is licensed under the MIT License.
