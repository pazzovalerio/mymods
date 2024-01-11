import redis
r = redis.Redis()

x = int(r.get("gettoni"))
print (x)
