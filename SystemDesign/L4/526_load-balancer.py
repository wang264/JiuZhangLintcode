# Description
# Implement a load balancer for web servers. It provide the following functionality:
#
# Add a new server to the cluster => add(server_id).
# Remove a bad server from the cluster => remove(server_id).
# Pick a server in the cluster randomly with equal probability => pick().
# At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
#   add(1)
#   add(2)
#   add(3)
#   pick()
#   pick()
#   pick()
#   pick()
#   remove(1)
#   pick()
#   pick()
#   pick()
# Output:
#   1
#   2
#   1
#   3
#   2
#   3
#   3
# Explanation: The return value of pick() is random, it can be either 2 3 3 1 3 2 2 or other.


import random


class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.id_to_arr_index = dict()
        self.nums = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        # write your code here
        self.nums.append(server_id)
        last_index = len(self.nums) - 1
        self.id_to_arr_index[server_id] = last_index

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        # write your code here
        idx_to_remove = self.id_to_arr_index[server_id]
        idx_last_element = len(self.nums) - 1
        self.id_to_arr_index[self.nums[idx_last_element]] = idx_to_remove
        self.nums[idx_to_remove], self.nums[idx_last_element] = self.nums[idx_last_element], self.nums[idx_to_remove]
        del self.id_to_arr_index[server_id]
        self.nums.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        # write your code here
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]