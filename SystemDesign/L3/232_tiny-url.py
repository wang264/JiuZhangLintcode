# Description
# Given a long url, make it shorter.
#
# You should implement two methods:
#
# longToShort(url) Convert a long url to a short url which starts with http://tiny.url/.
# shortToLong(url) Convert a short url to a long url.
# You can design any shorten algorithm, the judge only cares about two things:
#
# The short key's length should equal to 6 (without domain and slash). And the acceptable characters are [a-zA-Z0-9]. For example: abcD9E
# No two long urls mapping to the same short url and no two short urls mapping to the same long url.
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input: shortToLong(longToShort("http://www.lintcode.com/faq/?id=10"))
# Output: "http://www.lintcode.com/faq/?id=10"
# Explanation:
#   When longToShort() called, you can return any short url.
#   For example, "http://tiny.url/abcdef".
#   And "http://tiny.url/ABCDEF" is ok as well.
# Example 2:
#
# Input:
#   shortToLong(longToShort("http://www.lintcode.com/faq/?id=10"))
#   shortToLong(longToShort("http://www.lintcode.com/faq/?id=10"))
# Output:
#   "http://www.lintcode.com/faq/?id=10"
#   "http://www.lintcode.com/faq/?id=10"


# 　用老师讲的随机得到short url的方式实现，更加推荐而且代码更简洁
class TinyUrl:

    def __init__(self):
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # key: longURL, value: shortURL
        self.longURL = {}
        # key: shortURL, value: longURL
        self.shortURL = {}

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def longToShort(self, url):
        # write your code here
        if url in self.longURL:
            return self.longURL[url]
        shorted = self.generateShortURL(url)
        while shorted in self.shortURL:
            shorted = self.generateShortURL(url)
        self.longURL[url] = shorted
        self.shortURL[shorted] = url
        return shorted

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, url):
        # write your code here
        if url in self.shortURL:
            return self.shortURL[url]
        return None

    def generateShortURL(self, url):
        import random
        shorted = ''
        for _ in range(6):
            shorted += random.choice(self.chars)
        return 'http://tiny.url/' + shorted


#
# 用两个哈希表, 一个是短网址映射到长网址, 一个是长网址映射到短网址.
# 短网址是固定的格式: "http://tiny.url/" + 6个字符, 字符可以是任意的.
# 为了避免重复, 我们可以按照字典序依次使用, 或者在随机生成的基础上用一个集合来记录是否使用过.


class TinyUrl_1:

    def __init__(self):
        self.dict = {}

    def getShortKey(self, url):
        return url[-6:]

    def idToShortKey(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            s = ch[id % 62] + s
            id /= 62
        while len(s) < 6:
            s = 'a' + s
        return s

    def shortkeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id

    # @param {string} url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, url):
        # Write your code here
        ans = 0
        for a in url:
            ans = (ans * 256 + ord(a)) % 56800235584L

        while ans in self.dict and self.dict[ans] != url:
            ans = (ans + 1) % 56800235584L

        self.dict[ans] = url
        return "http://tiny.url/" + self.idToShortKey(ans)

    # @param {string} url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, url):
        # Write your code here
        short_key = self.getShortKey(url)
        return self.dict[self.shortkeyToid(short_key)]
