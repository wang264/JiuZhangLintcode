# Description
# In Consistent Hashing I we introduced a relatively simple consistency hashing algorithm. This simple version has two defects：
#
# After adding a machine, the data comes from one of the machines. The read load of this machine is too large, which will affect the normal service.
# When adding to 3 machines, the load of each server is not balanced, it is 1:1:2
# In order to solve this problem, the concept of micro-shards was introduced, and a better algorithm is like this：
#
# From 0~359 to a range of 0 ~ n-1, the interval is connected end to end and connected into a circle.
# When joining a new machine, randomly choose to sprinkle k points in the circle, representing the k micro-shards of the machine.
# Each data also corresponds to a point on the circumference, which is calculated by a hash function.
# Which machine belongs to which data is to be managed is determined by the machine to which the first micro-shard point that is clockwise touched on the circle is corresponding to the point on the circumference of the data.
# n and k are typically 2^64 and 1000 in a real NoSQL database.
#
# Implement these methods of introducing consistent hashing of micro-shard.
#
# create(int n, int k)
# addMachine(int machine_id) // add a new machine, return a list of shard ids.
# getMachineIdByHashCode(int hashcode) // return machine id
# When n is 2^64, there is almost no repetition in the interval within this interval.
# However, in order to test the correctness of your program, n may be small in the data, so you must ensure that the k random numbers you generate will not be duplicated.
# LintCode does not judge the correctness of your returnMachine's return (because it is a random number), it will only judge the correctness of your getMachineIdByHashCode result based on the result of the addMachine you return.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
#   create(100, 3)
#   addMachine(1)
#   getMachineIdByHashCode(4)
#   addMachine(2)
#   getMachineIdByHashCode(61)
#   getMachineIdByHashCode(91)
# Output:
#   [77,83,86]
#   1
#   [15,35,93]
#   1
#   2
# Example 2:
#
# Input:
#   create(10, 5)
#   addMachine(1)
#   getMachineIdByHashCode(4)
#   addMachine(2)
#   getMachineIdByHashCode(0)
#   getMachineIdByHashCode(1)
#   getMachineIdByHashCode(2)
#   getMachineIdByHashCode(3)
#   getMachineIdByHashCode(4)
#   getMachineIdByHashCode(5)
# Output:
#   [2,3,5,6,7]
#   1
#   [0,1,4,8,9]
#   2
#   2
#   1
#   1
#   2
#   1

import random


class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """

    @classmethod
    def create(cls, n, k):
        # Write your code here
        return cls(n, k)

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.used_location = set()  # save a list of locations on the ring that is already used
        self.machine_location = []  # [(location, machine_id)] this list is always sorted

    """
    Time Complexity O(nlogn), mainly because of keep machine_location sorted
    @param: machine_id: An integer
    @return: a list of shard ids
    """

    def addMachine(self, machine_id):
        # write your code here
        new_locations = []
        while len(new_locations) < self.k:
            rand_num = random.randint(0, self.n - 1)
            if rand_num not in self.used_location:
                self.used_location.add(rand_num)
                self.machine_location.append((rand_num, machine_id))
                self.machine_location.sort()
                new_locations.append(rand_num)
        return new_locations

    """
    Time complexity O(logn)
    @param: hashcode: An integer
    @return: A machine id
    """

    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        next_machine_index = self.binary_search(self.machine_location, 0, len(self.machine_location) - 1,
                                                hashcode)  # o(logn)

        if next_machine_index == -1:
            next_machine_index = 0
        return self.machine_location[next_machine_index][1]

    """
    return index in the orginal array where first number > target
    @param: nums: (location, machine_id)
    @param: start: start index in array
    @param: end: index in array
    @target: target
    @return: index of first number which is > target, return -1 if not found
    """

    def binary_search(self, nums, start, end, target):
        if not nums:
            return -1
        while start + 1 < end:
            mid = (start + end) // 2
            if target < nums[mid][0]:
                end = mid
            else:
                start = mid
        if nums[start][0] >= target:
            return start
        if nums[end][0] >= target:
            return end
        return -1