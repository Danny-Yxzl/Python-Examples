import redis


class RedisServer:
    def __init__(self, host, port, password):
        self.r = redis.StrictRedis(host=host, port=port, db=0, password=password, decode_responses=True)

    def set(self, key, value):
        try:
            self.r.set(key, value)
            return value
        except:
            return None
            
    def get(self, key):
        try:
            return self.r.get(key)
        except:
            return None

    def insr(self, key):
        try:
            return self.r.incr(key)
        except:
            return None


if __name__ == "__main__":
    r = RedisServer("redis.example.com", 6379, "PASSWORD")
    r.set("key1", 1)
    print(r.get("key1"))
    print(r.insr("key1"))

