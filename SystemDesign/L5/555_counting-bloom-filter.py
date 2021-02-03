# Description
# Implement a counting bloom filter. Support the following method:
#
# add(string). Add a string into bloom filter.
# contains(string). Check a string whether exists in bloom filter.
# remove(string). Remove a string from bloom filter.
# Have you met this question in a real interview?
# Example
# Example1
#
# Input:
# CountingBloomFilter(3)
# add("lint")
# add("code")
# contains("lint")
# remove("lint")
# contains("lint")
#
# Output:
# [true,false]
# Example2
#
# Input:
# CountingBloomFilter(3)
# add("lint")
# add("lint")
# contains("lint")
# remove("lint")
# contains("lint")
#
# Output:
# [true,true]
# Related Problems


# 用map维护数字出现的次数 当加入一个元素时，让map对应改元素的值+1，删除元素时，让map对应该元素的值-1


import random


class HashFunction:

    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap

        return ret


class CountingBloomFilter:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))

        self.bits = [0 for i in range(20000)]

    # @param {str} word a string
    def add(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] += 1

    # @param {str} word a string
    def remove(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] -= 1

    # @param {str} word a string
    # @return {bool} True if word is exists in bllom filter or false
    def contains(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            if self.bits[position] <= 0:
                return False

        return True