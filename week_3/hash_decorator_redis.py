import redis

redis_host = 'localhost'
redis_port = 6379

hash_db = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


def hash_decorator(func):
    """Function-decorator, which save the result of the function func in redis database
       and return it from this DB, if it was calculated earlier"""

    def wrapper(number: int) -> int:
        result = hash_db.get(str(number))
        if result:
            return result
        result = func(number)
        hash_db.set(f"{number}", f"{result}")
        return result
    return wrapper


@hash_decorator
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    print(multiplier(4))
    print(multiplier(4))

