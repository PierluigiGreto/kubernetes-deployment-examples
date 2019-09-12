FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install redis
ENTRYPOINT [ "python3", "-u", "redis_subscriber.py" ]
