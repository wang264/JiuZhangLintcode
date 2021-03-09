# Description
# Support follow & unfollow, getFollowers, getFollowings.
# Note: the results of getfollow() are sorted.
#
# Have you met this question in a real interview?
# Example
# follow(1, 3)
# getFollowers(1) // return [3]
# getFollowings(3) // return [1]
# follow(2, 3)
# getFollowings(3) // return [1,2]
# unfollow(1, 3)
# getFollowings(3) // return [2]

#
# 友谊服务 · Friendship Service
# 面向对象设计
# LintCode 版权所有
# 描述
# 支持 follow & unfollow, getFollowers, getFollowings方法
# 注意：getfollow（）的结果是排序后的。
#
# 样例
# 例1:
#
# 输入:
# follow(1, 3)
# getFollowers(1)
# getFollowings(3)
# follow(2, 3)
# getFollowings(3)
# unfollow(1, 3)
# getFollowings(3)
# 输出:
# [3]
# [1]
# [1,2]
# [2]
# 解释:
# follow(1, 3)
# getFollowers(1) // return [3]
# getFollowings(3) // return [1]
# follow(2, 3)
# getFollowings(3) // return [1,2]
# unfollow(1, 3)
# getFollowings(3) // return [2]
# 例2:
#
# 输入:
# follow(1, 2)
# unfollow(1, 2)
# getFollowings(1)
# unfollow(1, 2)
# getFollowings(1)
# unfollow(1, 2)
# follow(1, 2)
# getFollowings(1)
# 输出:
# []
# []
# []


class FriendshipService:

    def __init__(self):
        # initialize your data structure here.
        self.followers = dict()
        self.followings = dict()

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowers(self, user_id):
        # Write your code here
        if user_id not in self.followers:
            return []
        results = list(self.followers[user_id])
        results.sort()
        return results

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowings(self, user_id):
        # Write your code here
        if user_id not in self.followings:
            return []
        results = list(self.followings[user_id])
        results.sort()
        return results

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id follows to_user_id
    def follow(self, to_user_id, from_user_id):
        # Write your code here
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        self.followers[to_user_id].add(from_user_id)

        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followings[from_user_id].add(to_user_id)

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id unfollows to_user_id
    def unfollow(self, to_user_id, from_user_id):
        # Write your code here
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)

        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)
