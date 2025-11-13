# Python Flask CI/CD Pipeline with Jenkins & Docker (Port 5001)

This project demonstrates a complete CI/CD pipeline using Jenkins, Python, Flask, Docker, and pytest.

## Pipeline Stages
1. Checkout code from GitHub
2. Install Python dependencies
3. Run unit tests using pytest
4. Build Docker image
5. Run container on port 5001
6. Archive artifacts

## Run Locally

```bash
pip install -r requirements.txt
python app/app.py
