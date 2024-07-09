FROM python:3.10
LABEL authors="mavifindsbugs"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app

CMD ["python3", "main.py"]