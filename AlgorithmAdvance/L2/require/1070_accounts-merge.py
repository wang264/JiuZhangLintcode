# Description
#
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a
# name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email
# that is common to both accounts. Note that even if two accounts have the same name, they may belong to different
# people as people could have the same name. A person can have any number of accounts initially, but all of their
# accounts definitely have the same name.
#
# and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
# After merging the accounts, return the accounts in the following format: the first element of each account is the
# name,and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Notice:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
#
# Example
# Example 1:
# Input:
# [
#     ["John", "johnsmith@mail.com", "john00@mail.com"],
#     ["John", "johnnybravo@mail.com"],
#     ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#     ["Mary", "mary@mail.com"]
# ]
#
# Output:
# [
#     ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#     ["John", "johnnybravo@mail.com"],
#     ["Mary", "mary@mail.com"]
# ]
#
# Explanation:
# The first and third John 's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as noneof their email addresses are used by other accounts.
# You could return these lists in any order,
# for example the answer
#
# [
#     ['Mary', 'mary@mail.com'],
#     ['John', 'johnnybravo@mail.com'],
#     ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
# ]
# is also acceptable.


# self.father = dict() from one email ---> its father node
# self.owner = dict() from one email ---> owner(name) of that email(the name)
# self.root_node_to_its_sons = dict() from root node --> list of its son
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def __init__(self):
        self.father = {}
        self.owner = {}
        self.root_node_to_its_sons = {}

    def accountsMerge(self, accounts):
        # reset instance variables
        self.father = {}
        self.owner = {}
        self.root_node_to_its_sons = {}

        result = []

        # set up the father for each email. and also the owner of each email
        for account in accounts:
            n = len(account)
            account_name = account[0]
            for i in range(1, n):
                self.father[account[i]] = account[i]
                self.owner[account[i]] = account_name

        # for each account, connect them together, ie.  connect them to the first email in each account
        for account in accounts:
            n = len(account)
            for i in range(2, n):
                # the first email will be the father of all other emails in that account
                self.union(account[1], account[i])

        for account in accounts:
            n = len(account)
            for i in range(1, n):
                this_email = account[i]
                root_for_this_email = self.find(this_email)
                if root_for_this_email not in self.root_node_to_its_sons.keys():
                    self.root_node_to_its_sons[root_for_this_email] = list()

                self.root_node_to_its_sons[root_for_this_email].append(this_email)

        # iterate through dict root_node_to_its_sons so we can generate the result,
        for root_node, sons_of_root_node in self.root_node_to_its_sons.items():
            account_name = self.owner[root_node]
            emails = sorted(set(sons_of_root_node))
            result.append([account_name]+emails)

        return result

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a

    def find(self, x):
        root = x
        # if x is root node, directly return it
        if self.father[x] == x:
            return x
        # find the root node
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root

sol = Solution()
sol.accountsMerge(accounts=[
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "john_newyork@mail.com", "johnsmith@mail.com"],
    ["Mary", "mary@mail.com"]
])

assert sol.accountsMerge(accounts=[
    ["John", "A", "B"],
    ["John", "D"],
    ["John", "C", "A"],
    ["Mary", "E"]
]) == [['John', 'A', 'B', 'C'], ['John', 'D'], ['Mary', 'E']]
