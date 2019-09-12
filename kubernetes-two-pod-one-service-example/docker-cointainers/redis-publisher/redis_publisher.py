import redis
import os
import time

i = 0
PORT_SERVICE_REDIS_SERVICE_HOST = os.environ['PORT_SERVICE_REDIS_SERVICE_HOST']
PORT_SERVICE_REDIS_SERVICE_PORT = os.environ['PORT_SERVICE_REDIS_SERVICE_PORT']

print(PORT_SERVICE_REDIS_SERVICE_HOST, PORT_SERVICE_REDIS_SERVICE_PORT)

myredis = redis.Redis(PORT_SERVICE_REDIS_SERVICE_HOST, PORT_SERVICE_REDIS_SERVICE_PORT)

while True:
     myredis.publish('channel',f'{i}')
     i = i + 1
     time.sleep(5)
