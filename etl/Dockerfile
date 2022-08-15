FROM python:3.9.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
WORKDIR /etl
COPY . .
CMD ["python3", "main.py"]