# 🚀 Leads Manager – Cloud Deployment (AWS Academy Sandbox)

This guide walks you from **💻 code → 🧪 local test → ☁️ AWS deployment** using **CloudFormation** with an **Application Load Balancer (ALB)**, an **Auto Scaling Group (ASG)**, and **no SSH/ECR** (perfect for the AWS Academy sandbox).  
Your EC2 instances **clone this repo**, **build the Docker image locally**, and **run Flask on port 5000**. The ALB listens on port 80 and forwards traffic to 5000.

---

## 🧩 Project Overview

- **Topic**: Leads Manager
- **Language**: Python
- **Architecture**: Monolithic
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
├── aws/
│   ├── cloudformation.yaml
├── Python_Code/
│   ├── API.py
│   ├── LeadsManager.py
│   ├── Main.py
├── Website/
│   ├── controller.js
│   ├── index.html
│   ├── leadsSerivce.js
│   ├── style.css
├── Dockerfile
├── requirements.txt
```

---

## 🐳 Docker Sanity Local Run

```bash
# 🏗 Build container
docker build -t leads-manager-app:latest .

# ▶️ Run container
docker run --rm -p 5000:5000 leads-manager-app:latest

# 🌐 Visit
http://localhost:5000
```

You should see the UI, and clicking actions should hit `/leads` on the same origin.

---

---
## 0) Setting AWS Lab Credentials
```bash
export AWS_ACCESS_KEY_ID=<access-key-data>
export AWS_SECRET_ACCESS_KEY=<secret-key-data>
export AWS_SESSION_TOKEN=<token-data>
```
---
## 1) Pushing ECR to AWS (in-case needed)
Variables (replace if yours differ):
```bash
AWS_REGION=us-east-1
ACCOUNT_ID=192060932952
REPO=leads-manager-app
IMAGE_TAG=latest
IMAGE_URI=${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO}:${IMAGE_TAG}
```

```bash
aws ecr create-repository --repository-name ${REPO} --region ${AWS_REGION} || true
```
Login + tag + push:

```bash
aws ecr get-login-password --region ${AWS_REGION} \
 | docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

docker tag leads-manager-app:latest ${IMAGE_URI}
docker push ${IMAGE_URI}
```
--
## 📜 2) CloudFormation template

The template:
- 🏗 Creates **VPC**, two public subnets + internet gateway + route table
- 🌍 Creates **ALB** (port 80) + Target Group (port 5000)
- 🔒 Creates Security Groups (ALB open :80 to world; instance allows :5000 from ALB only)
- ⚙️ Launch Template → installs Docker + Git → clones repo → builds & runs container
- 🔄 Auto Scaling Group (**Min/Desired/Max = 1**) → auto-attaches to Target Group

> ✅ With ASG, the instance registers automatically → no 503 “no healthy targets”.

---

## 🚀 3) Deploy the stack

```bash
aws cloudformation deploy \
  --stack-name leads-manager-sandbox-app \
  --template-file cloudformation.yml
```

Wait **2–4 minutes** for `git clone → docker build → docker run`.

---

## 🔍 4) Get ALB URL & test

```bash
# get ALB URL
aws cloudformation describe-stacks \
  --stack-name leads-manager-sandbox-app \
  --query "Stacks[0].Outputs[?OutputKey=='LoadBalancerDNSName'].OutputValue" \
  --output text
```
or

```bash
ALB=$(aws cloudformation describe-stacks   --stack-name leads-manager-sandbox-app   --query "Stacks[0].Outputs[?OutputKey=='LoadBalancerDNSName'].OutputValue"   --output text)
echo "http://$ALB"
```

Open in browser → UI & API should work.

---

## 🩺5) Check target health (503 troubleshooting)

```bash
TG_ARN=$(aws elbv2 describe-target-groups   --names TargetGroup   --query 'TargetGroups[0].TargetGroupArn' --output text)

aws elbv2 describe-target-health --target-group-arn "$TG_ARN"   --query 'TargetHealthDescriptions[].{Id:Target.Id,State:TargetHealth.State,Reason:TargetHealth.Reason,Desc:TargetHealth.Description}'   --output table
```

- `initial` → wait a bit  
- `unhealthy` → see troubleshooting

---

## 🔄6) Updating the app

**Option A – Recreate instance**  
```bash
aws autoscaling update-auto-scaling-group   --auto-scaling-group-name <ASG-NAME> --desired-capacity 0
sleep 15
aws autoscaling update-auto-scaling-group   --auto-scaling-group-name <ASG-NAME> --desired-capacity 1
```

**Option B – Redeploy stack**  
```bash
aws cloudformation deploy   --stack-name leads-manager-sandbox-app   --template-file cloudformation.yml
```

---

## 🧹 7) Teardown

```bash
aws cloudformation delete-stack --stack-name leads-manager-sandbox-app
aws cloudformation wait stack-delete-complete --stack-name leads-manager-sandbox-app
```

---

## 🛠 Troubleshooting

**❌ ROLLBACK_COMPLETE** → run:
```bash
aws cloudformation describe-stack-events --stack-name leads-manager-sandbox-app   --query "StackEvents[?ResourceStatus=='CREATE_FAILED'].[Timestamp,LogicalResourceId,ResourceStatusReason]"   --output table
```
- Bad AMI → replace `ImageId`
- SG/VPC conflicts → delete stack, retry

**❌ ALB 503** → check Target Group health, ensure container is listening on :5000, repo is public

**❌ UI works but buttons fail** → check `Website/leadsService.js` uses `/leads`

---

💡 **Tip:** Keep your repo public so EC2 can `git clone` without keys.

🎯 You now have a **sandbox-safe, reproducible** AWS deployment pipeline!

## 📬 Contact

**Developers**: Aner & Ameer
