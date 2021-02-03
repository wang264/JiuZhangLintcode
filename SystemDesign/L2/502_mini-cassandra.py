# Description
# Cassandra is a NoSQL database (a.k.a key-value storage). One individual data entry in cassandra constructed by 3 parts:
#
# row_key. (a.k.a hash_key, partition key or sharding_key.)
# column_key.
# value
# row_key is used to hash and can not support range query. Let's simplify this to a string.
# column_key is sorted and support range query. Let's simplify this to integer.
# value is a string. You can serialize any data into a string and store it in value.
#
# Implement the following methods:
#
# insert(row_key, column_key, value)
# query(row_key, column_start, column_end) return a list of entries
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
#   insert("google", 1, "haha")
#   query("google", 0, 1)
# Output: [(1, "haha")]
# Example 2:
#
# Input:
#   insert("google", 1, "haha")
#   insert("lintcode", 1, "Good")
#   insert("google", 2, "hehe")
#   query("google", 0, 1)
#   query("google", 0, 2)
#   query("go", 0, 1)
#   query("lintcode", 0, 10)
# Output:
#   [(1, "haha")]
#   [(1, "haha"),(2, "hehe")]
#   []
#   [(1, "Good")]
#

# 注意: 一个 row_key 可以对应多个 Column; 而一个 row_key 和一个 column_key 是唯一确定对应的 value 的.
# 可以使用哈希表套哈希表实现: map<row_key, map<column_key, value>>
# 每次 insert 直接更新 value 即可.
# 而 query 则需要取出一个 row_key 对应的所有的 <column_key, value> 对, 如果 column_key 在给定范围内时, 放入答案序列中即可.


class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value


from collections import OrderedDict


class MiniCassandra:

    def __init__(self):
        # initialize your data structure here.
        self.hash = {}

    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
    def insert(self, raw_key, column_key, column_value):
        # Write your code here
        if raw_key not in self.hash:
            self.hash[raw_key] = OrderedDict()
        self.hash[raw_key][column_key] = column_value

    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns

    def query(self, raw_key, column_start, column_end):
        # Write your code here
        rt = []
        if raw_key not in self.hash:
            return rt

        self.hash[raw_key] = OrderedDict(sorted(self.hash[raw_key].items()))
        for key, value in self.hash[raw_key].items():
            if key >= column_start and key <= column_end:
                rt.append(Column(key, value))

        return rt
