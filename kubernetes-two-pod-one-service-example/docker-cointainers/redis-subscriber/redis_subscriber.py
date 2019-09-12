
import redis
import os

PORT_SERVICE_REDIS_SERVICE_HOST = os.environ['PORT_SERVICE_REDIS_SERVICE_HOST']
PORT_SERVICE_REDIS_SERVICE_PORT = os.environ['PORT_SERVICE_REDIS_SERVICE_PORT']

print(PORT_SERVICE_REDIS_SERVICE_HOST, PORT_SERVICE_REDIS_SERVICE_PORT)

myredis = redis.Redis(PORT_SERVICE_REDIS_SERVICE_HOST, PORT_SERVICE_REDIS_SERVICE_PORT)


pubsub = myredis.pubsub()
pubsub.subscribe(['channel'])

for item in pubsub.listen():
        print(f'{item["data"]}')
