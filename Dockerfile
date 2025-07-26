# Use official Python image
FROM python:3.10-slim

WORKDIR /Python_code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Python_code/ ./Python_code/
COPY Website/ ./Website/

EXPOSE 5000
CMD ["python", "Python_code/API.py"]
