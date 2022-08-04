FROM python:3.7-alpine
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
WORKDIR /kafka_writer
COPY . .
RUN mkdir logs -p
CMD ["python3", "kafka_writer.py"]