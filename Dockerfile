FROM python:3.9-slim
COPY . .

WORKDIR .

RUN apt-get -y update
RUN apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
