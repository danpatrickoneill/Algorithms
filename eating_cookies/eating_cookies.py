#!/usr/bin/python

import sys
import time

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# global cache and assignment option
# cache = {}
# cache[n] = eating_cookies(
#         n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


def eating_cookies(n,  cache=None):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if cache:
        # Check cache at index n
        if cache[n]:
            return cache[n]
        # If it doesn't exist, cache return value
        else:
            cache[n] = eating_cookies(
                n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    # print(cache)
    return eating_cookies(
        n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

# Small inputs only version
# def eating_cookies(n,  cache=None):
#     if n <= 1:
#         return 1
#     if n == 2:
#         return 2
#     return eating_cookies(
#         n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


start_time = time.time()
eating_cookies(25, [0 for i in range(26)])
end_time = time.time()
print(end_time - start_time)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
