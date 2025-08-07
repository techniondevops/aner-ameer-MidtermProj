# Midterm Project – DevOps Deployment

Welcome to the **Midterm DevOps Project** repository for DeployNova!  
This project showcases a Python-based application containerized with Docker and deployed on AWS using Elastic Beanstalk and ECR.

---

## 🧩 Project Overview

- **Topic**: Contact Manager
- **Language**: Python
- **Architecture**: Modular (`main.py` + `functions.py`)
- **Interface**: Flask-based web UI
- **Storage**: In-memory using Python dictionaries/lists
- **Features**:
  - Add / Edit / Delete / Display entries
  - Sort and calculate based on stored data
  - Web interface through Flask

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py
│   ├── functions.py
│   └── templates/
│       └── index.html
├── Dockerfile
├── requirements.txt
└── Dockerrun.aws.json (used for deployment)
```

---

## 🐳 Docker Configuration

### Dockerfile

Ubuntu-based image that installs Flask, sets the working directory, and runs the app on port 8080.

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app/main.py"]
```

### Flask Run Command

Your Flask app must start like this to work in Elastic Beanstalk:

```python
app.run(host="0.0.0.0", port=8080)
```

---

## 🚀 AWS Deployment (Manual via Console)

### 1. AWS ECR

- Created a private repository in **Elastic Container Registry**: `midterm-proj`
- Built and pushed the Docker image:

```bash
docker build -t midterm-proj .
docker tag midterm-proj:latest 495307862605.dkr.ecr.us-east-1.amazonaws.com/midterm-proj:latest
docker push 495307862605.dkr.ecr.us-east-1.amazonaws.com/midterm-proj:latest
```

export aws_access_key_id=[KEY_ID]
export aws_secret_access_key=[ACCESS_KEY]
export aws_session_token=[SECERT_KEY]

aws ecr create-repository --repository-name leads-manager-app --region us-east-1
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 192060932952.dkr.ecr.us-east-1.amazonaws.com
docker tag leads-manager-app:latest 192060932952.dkr.ecr.us-east-1.amazonaws.com/leads-manager-app:latest
docker push 192060932952.dkr.ecr.us-east-1.amazonaws.com/leads-manager-app:latest

aws cloudformation deploy \
  --template-file D:\\MidtermProj\\aws\\cloudformation.yml \
  --stack-name leads-manager-stack \
  --parameter-overrides ImageURI=192060932952.dkr.ecr.us-east-1.amazonaws.com/leads-manager:latest \
  --capabilities CAPABILITY_NAMED_IAM
---

## ⚠️ Troubleshooting & Lessons Learned

- ❌ Attempting "High Availability" failed due to IAM sandbox limits on Auto Scaling
- ✅ Switching to **Single Instance** solved the issue
- ❌ Initial 503 errors appeared due to Flask listening on port 5000 instead of 8080
- ✅ Fixed by:
  - Updating Flask to listen on `port=8080`
  - Rebuilding Docker image
  - Using correct `Dockerrun.aws.json`
- ❌ EB errors about version = 3 fixed by using `"AWSEBDockerrunVersion": 1`

---

## ✅ Final Deliverables

- ✅ Python app with modular logic
- ✅ Web UI using Flask
- ✅ Dockerized (with Dockerfile)
- ✅ Image pushed to AWS ECR
- ✅ Successfully deployed using AWS Elastic Beanstalk

---

## 🧠 Developer Notes

This project was built and deployed manually for educational and demonstration purposes, simulating a DevOps pipeline using containerization and cloud-native deployment tools.

---

## 📬 Contact

**Developers**: Aner & Ameer

