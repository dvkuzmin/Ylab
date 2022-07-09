def hash_decorator(func):
    """Function-decorator, which save the result of the function func in dict
       and return it from this dict, if it was calculated earlier"""
    hash_dict = {}

    def wrapper(number: int) -> int:
        if number not in hash_dict:
            result = func(number)
            hash_dict[number] = result
            return result
        return hash_dict[number]
    return wrapper


@hash_decorator
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    print(multiplier(4))
    print(multiplier(4))
