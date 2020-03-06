class ListCharNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class DataStream:
    def __init__(self):
        # dictionary for each 'char', point to the previous node
        self.charToPrev = dict()
        # to record the duplicated chars, will be in this list after we see it the second time.
        self.dupChars = set()
        self.dummy = ListCharNode('.')
        self.tail = self.dummy

    def add(self, c):
        ######################################################
        # 第三次或以上見到，我們能直接判斷了
        if c in self.dupChars:
            return
        ######################################################
        # 如果是第一次看到，我們加到鏈表中
        if c not in self.charToPrev:
            node = ListCharNode(c)
            self.charToPrev[c] = self.tail
            self.tail.next = node
            self.tail = node
            return
        ######################################################
        # 第二次看到的時候，我們把Node從鏈表中刪除。如果那個節點是Tail的話，我們把Tail往前移。
        # delete the existing node
        prev = self.charToPrev[c]
        prev.next = prev.next.next
        if prev.next is None:
            # tail node removed
            self.tail = prev
        else:
            self.charToPrev[prev.next.val] = prev

        self.charToPrev.pop(c)
        self.dupChars.add(c)

    def firstUniqueChar(self):
        return self.dummy.next.val


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        ds = DataStream()
        for i in range(len(str)):
            ds.add(str[i])

        return ds.firstUniqueChar()
        # if ask for the index
        # return str.find(ds.firstUniqueChar())