# Description
# Implement a memcache which support the following features:
#
# 1. get(curtTime, key). Get the key's value, return 2147483647 if key does not exist.
# 2. set(curtTime, key, value, ttl). Set the key-value pair in memcache with a time to live (ttl). The key will be
# valid from curtTime to curtTime + ttl - 1 and it will be expired after ttl seconds. if ttl is 0, the key lives
# forever until out of memory.

# 3. delete(curtTime, key). Delete the key.
# 4. incr(curtTime, key, delta). Increase the key's value by delta return the new value. Return 2147483647 if key does not exist.
# 5. decr(curtTime, key, delta). Decrease the key's value by delta return the new value. Return 2147483647 if key does not exist.
# It's guaranteed that the input is given with increasingcurtTime.
#
# Have you met this question in a real interview?
# Clarification
# Actually, a real memcache server will evict keys if memory is not sufficient, and it also supports variety of
# value types like string and integer. In our case, let's make it simple, we can assume that we have enough memory
#  and all of the values are integers.
#
# Search "LRU" & "LFU" on google to get more information about how memcache evict data.
#
# Try the following problem to learn LRU cache:
# http://www.lintcode.com/problem/lru-cache
#
# Example
# Example1
#
# get(1, 0)
# >> 2147483647
# set(2, 1, 1, 2)
# get(3, 1)
# >> 1
# get(4, 1)
# >> 2147483647
# incr(5, 1, 1)
# >> 2147483647
# set(6, 1, 3, 0)
# incr(7, 1, 1)
# >> 4
# decr(8, 1, 1)
# >> 3
# get(9, 1)
# >> 3
# delete(10, 1)
# get(11, 1)
# >> 2147483647
# incr(12, 1, 1)
# >> 2147483647
# Related Problems


class Resource:

    def __init__(self, value, expired):
        self.value = value
        self.expired = expired


INT_MAX = 0x7fffffff


class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.client = dict()

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        res = self.client.get(key)
        if res.expired >= curtTime or res.expired == -1:
            return res.value
        else:
            return INT_MAX

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        # Write your code here
        if ttl:
            res = Resource(value, curtTime + ttl - 1)
        else:
            res = Resource(value, -1)

        self.client[key] = res

        # @param {int} curtTime an integer

    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return

        del self.client[key]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        # Write your code here
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value += delta

        return self.client[key].value

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        # Write your code here
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value -= delta

        return self.client[key].value