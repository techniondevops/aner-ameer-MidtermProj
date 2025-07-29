FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Python_code/ ./Python_code/

COPY Website/ ./Website/

EXPOSE 5000

# CMD ["python", "-m", "flask", "run"]

CMD ["python", "Python_code/API.py"]
