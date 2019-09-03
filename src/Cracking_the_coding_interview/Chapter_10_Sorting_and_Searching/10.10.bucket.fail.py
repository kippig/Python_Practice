# Rank from Stream:Imagineyouarereadinginastreamofintegers.Periodically,youwishtobeable to look up the rank of a numberx
# (the number of values less than or equal tox). lmplement the data structures and algorithms to support these
# operations. That is, implement the method track ( int x), which is called when each number is generated, and the
# method getRankOfNumber(int x), which returns the number of values less than or equal tox (not includingx itself)
import json


def update_hashmap(n, billions_hashmap: dict):
    current_hashmap = billions_hashmap
    for i in range(2, -1, -1):
        digit = n//10**i % 10
        if current_hashmap.get(digit) is None:
            current_hashmap[digit] = (dict(), 1)
        else:
            current_hashmap[digit] = current_hashmap[digit][0], current_hashmap[digit][1] + 1
        current_hashmap = current_hashmap[digit][0]


def get_rank(n, billions_hashmnap: dict):
    current_hashmap = billions_hashmap
    print(current_hashmap)
    for i in range(2, -1, -1):
        digit = n // 10 ** i % 10
        if digit == 0:
            if current_hashmap[digit][0].get(digit) is None:
                return 0
            current_hashmap = current_hashmap[digit][0]
        else:
            if current_hashmap[digit - 1][0].get(digit) is None:
                pass


def truncate_int(n):
    return n - n % 10**(len(str(n))-1)

billions_hashmap = dict()

update_hashmap(99, billions_hashmap)
update_hashmap(121, billions_hashmap)
update_hashmap(13, billions_hashmap)
update_hashmap(5, billions_hashmap)
print(billions_hashmap)
print(get_rank(13, billions_hashmap))