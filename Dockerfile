# Ubuntu base (course requirement)
FROM ubuntu:22.04

# Install Python + pip + curl
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# App code
COPY Python_code/ ./Python_code/
COPY Website/ ./Website/

# Flask will serve both frontend (templates/static) and API on 0.0.0.0:5000
EXPOSE 5000
CMD ["python3", "Python_code/API.py"]
