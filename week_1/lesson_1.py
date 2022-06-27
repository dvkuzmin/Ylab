from math import log, floor
from functools import reduce


# task 1

def domain_name(url: str) -> str:

    prefixes = ("https://www.", "http://www.", "https://", "http://", "www.")

    domain = ""

    for prefix in prefixes:
        if url.startswith(prefix):
            for letter in url[len(prefix)::]:
                if letter != ".":
                    domain += letter
                else:
                    return domain
    for letter in url:
        if letter != ".":
            domain += letter
        else:
            return domain


# task 2

def int32_to_ip(int32: int):
    int32_to_bin = str(bin(int32))[2::]

    while len(int32_to_bin) < 32:  # append insignificant zeros
        int32_to_bin = '0' + int32_to_bin

    oct1, oct2, oct3, oct4 = int32_to_bin[:8], int32_to_bin[8:16], int32_to_bin[16:24], int32_to_bin[24:32]
    return f"{int(oct1, 2)}.{int(oct2, 2)}.{int(oct3, 2)}.{int(oct4, 2)}"


# task 3

def zeros(n):
    if n == 0:
        return 0
    k_max = floor(log(n, 5))
    trailing_zeros = 0
    for k in range(k_max):
        trailing_zeros += floor(n / (5 ** (k + 1)))
    return trailing_zeros


# task 4

def bananas(s: str) -> set:
    target_word = 'banana'
    result = set()

    def search_next_letter(s: str, idx: int, res: str = None):
        """searching the next letter in target word"""
        nonlocal result
        res = res or ''
        counter = 0

        for letter in s:
            counter += 1
            if letter == target_word[idx]:
                res += letter
                if idx == len(target_word) - 1:  # if last letter in target word
                    res += '-' * (len(s) - counter)
                    result.add(res)
                    res = res[:-1-len(s)+counter] + '-'
                else:
                    search_next_letter(s[counter::], idx+1, res)
                    res = res[:-1] + '-'
            else:
                res += '-'

    search_next_letter(s, 0)
    return result


# task 5

def count_find_num(primesL: list, limit: int):
    number = reduce(lambda x, y: x * y, primesL)
    if number > limit:
        return []
    queue = [number]
    max_number = number
    counter = 0

    while queue:
        number = queue.pop(0)
        if number <= limit:
            counter += 1
            for multiplier in primesL:
                new_number = number * multiplier
                if max_number < new_number <= limit:
                    max_number = new_number
                if new_number not in queue:
                    queue.append(new_number)
    return [counter, max_number]


if __name__ == "__main__":
    # task 1

    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"

    # task 2

    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"

    # task 3

    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7

    # task 4

    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

    # task 5

    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
