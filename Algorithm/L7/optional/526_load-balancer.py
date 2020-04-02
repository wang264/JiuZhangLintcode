# 526. Load Balancer
# 中文English
# Implement a load balancer for web servers. It provide the following functionality:
#
# Add a new server to the cluster => add(server_id).
# Remove a bad server from the cluster => remove(server_id).
# Pick a server in the cluster randomly with equal probability => pick().
# At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.
#
# 样例
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
#
# 一种可行的思路是同时使用哈希表和数组.
#
# pick(): 数组中随机选取一个元素可以直接使用随机函数得到一个 [0, 数组大小-1] 的整数即可.
# add(server_id): 在数组末尾添加这个server_id, 并在哈希表中添加 server_id -> 数组下标 的键值映射
# remove(server_id): 利用哈希表得到 server_id 的数组下标, 在数组中将它和最末尾的元素交换位置, 然后删除, 并将修改同步到哈希表
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
        last_idx = len(self.nums) - 1
        self.nums.append(server_id)
        self.id_to_arr_index[server_id] = last_idx + 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        # write your code here
        # 利用哈希表得到 server_id 的数组下标
        idx = self.id_to_arr_index[server_id]
        # 在数组中将它和最末尾的元素交换位置, 然后删除, 并将修改同步到哈希表
        self.id_to_arr_index[self.nums[-1]] = idx
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.id_to_arr_index.pop(self.nums[-1])
        self.nums.pop()
    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]
#
# # write your code here
# l = LoadBalancer()
# l.add(1)
# l.add(2)
# l.add(3)
# l.pick()
# l.pick()
# l.pick()
# l.pick()
# l.remove(1)
# l.pick()
# l.pick()
# l.pick()