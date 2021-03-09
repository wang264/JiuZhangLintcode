# Description
# Implement a simple twitter. Support the following method:
#
# postTweet(user_id, tweet_text). Post a tweet.
# getTimeline(user_id). Get the given user's most recently 10 tweets posted by himself, order by timestamp from most recent to least recent.
# getNewsFeed(user_id). Get the given user's most recently 10 tweets in his news feed (posted by his friends and himself). Order by timestamp from most recent to least recent.
# follow(from_user_id, to_user_id). from_user_id followed to_user_id.
# unfollow(from_user_id, to_user_id). from_user_id unfollowed to to_user_id.
# Have you met this question in a real interview?

# Example
# Example 1:
#
# Input:
#   postTweet(1, "LintCode is Good!!!")
#   getNewsFeed(1)
#   getTimeline(1)
#   follow(2, 1)
#   getNewsFeed(2)
#   unfollow(2, 1)
#   getNewsFeed(2)
# Output:
#   1
#   [1]
#   [1]
#   [1]
#   []
# Example 2:
#
# Input:
#   postTweet(1, "LintCode is Good!!!")
#   getNewsFeed(1)
#   getTimeline(1)
#   follow(2, 1)
#   postTweet(1, "LintCode is best!!!")
#   getNewsFeed(2)
#   unfollow(2, 1)
#   getNewsFeed(2)
# Output:
#   1
#   [1]
#   [1]
#   2
#   [2,1]
#   []

# 因为题目里涉及到对推文按照时间排序, 同时 Tweet 类本身不含时间信息, 所以我们需要额外地记录每条推文发出的时间.
# 可以定义一个类的静态变量作为计数器来实现.
#
# 然后分析我们需要的数据结构:
# 1. class Node {Tweet, int}; 对原有的Tweet类的扩展, 使其可以记录时间 (当然, 也可以用类的继承来实现)
# 2. map<int, vector<Node>> 用户id到这个用户发送了的推文的映射
# 3. map<int, set<int>> 用户id到这个用户关注的人的id的映射

# 然后对应每种方法的实现:
# 1. postTweet() 直接添加到map<int, vector<Node>>中即可
# 2. getTimeline() 根据map<int, vector<Node>>获得该用户的最新推文, 返回即可
# 3. getNewsFeed() 同时用到上面定义的两个映射, 比较暴力的做法是获取这些用户的所有推文, 排序, 拿出前十个; 或者可以利用堆进行 "多路归并"
# 4. follow() 在 map<int, set<int>> 中添加即可
# 5. unfollow() 在 map<int, set<int>> 中删除即可

# (本题解使用C++相关数据结构描述, 不过映射和集合在其他语言中也有对应的实现)

class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
        pass
    


class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.order = 0
        self.users_tweets = {}
        self.friends = {}

    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        tweet = Tweet.create(user_id, tweet_text)
        self.order += 1
        if user_id in self.users_tweets:
            self.users_tweets[user_id].append((self.order, tweet))
        else:
            self.users_tweets[user_id] = [(self.order, tweet)]
        return tweet

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        rt = []
        if user_id in self.users_tweets:
            rt = self.users_tweets[user_id][-10:]

        if user_id in self.friends:
            for friend in self.friends[user_id]:
                if friend in self.users_tweets:
                    rt.extend(self.users_tweets[friend][-10:])

        rt.sort(key=lambda x: x[0])
        return [tweet[1] for tweet in rt[-10:][::-1]]

    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        if user_id in self.users_tweets:
            return [tweet[1] for tweet in self.users_tweets[user_id][-10:][::-1]]
        else:
            return []

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.friends:
            self.friends[from_user_id] = set()
        self.friends[from_user_id].add(to_user_id)

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.friends:
            return

        self.friends[from_user_id].remove(to_user_id)