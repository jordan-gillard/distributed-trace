FROM python:3.11

WORKDIR workdir/
COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt
EXPOSE 8080

ENTRYPOINT python3 -m app
