# AwsAppRunner

A basic AWS App Runner Python application that builds from source.

## Overview

This project demonstrates how to deploy a Python web application to [AWS App Runner](https://aws.amazon.com/apprunner/) using the **build from source** method. AWS App Runner automatically builds the application from source code and deploys it as a fully managed container.

## Project Structure

```
.
├── app.py            # Flask web application
├── apprunner.yaml    # AWS App Runner build configuration
├── requirements.txt  # Python dependencies
└── README.md
```

## Application Endpoints

| Endpoint  | Method | Description                     |
|-----------|--------|---------------------------------|
| `/`       | GET    | Returns a welcome JSON message  |
| `/health` | GET    | Health check endpoint           |

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Test the endpoints:**
   ```bash
   curl http://localhost:8080/
   curl http://localhost:8080/health
   ```

## Deploying to AWS App Runner

### Prerequisites

- An AWS account
- The [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate permissions

### Deploy via AWS Console

1. Open the [AWS App Runner Console](https://console.aws.amazon.com/apprunner/).
2. Choose **Create service**.
3. For **Source**, select **Source code repository**.
4. Connect your GitHub account and select this repository.
5. Choose **Automatic** for deployment trigger (optional).
6. For **Build settings**, select **Use configuration file** — App Runner will use `apprunner.yaml`.
7. Complete the remaining configuration and choose **Create & deploy**.

### Deploy via AWS CLI

```bash
aws apprunner create-service \
  --service-name my-python-app \
  --source-configuration '{
    "CodeRepository": {
      "RepositoryUrl": "https://github.com/RampantLions/AwsAppRunner",
      "SourceCodeVersion": {
        "Type": "BRANCH",
        "Value": "main"
      },
      "CodeConfiguration": {
        "ConfigurationSource": "REPOSITORY"
      }
    }
  }'
```

## Configuration (`apprunner.yaml`)

The `apprunner.yaml` file tells AWS App Runner how to build and run the application:

```yaml
version: 1.0
runtime: python311
build:
  commands:
    build:
      - pip install -r requirements.txt
run:
  runtime-version: 3.11
  command: gunicorn -w 2 -b 0.0.0.0:8080 app:app
  network:
    port: 8080
    env: PORT
```

## Environment Variables

| Variable | Default | Description              |
|----------|---------|--------------------------|
| `PORT`   | `8080`  | Port the server listens on |