# 给一个图中的n个节点, 记为 1 到 n . 在开始的时候图中没有边。
# 你需要完成下面两个方法:
#
# connect(a, b), 添加连接节点 a, b 的边.
# query(a, b), 检验两个节点是否联通

# 算法：并查集
#
# 并查集是一种可以动态维护若干个不重叠的集合，并支持合并与查询两种操作的一种数据结构
#
# 一般我们建立一个数组fa 或者用map表示一个并查集，fa[i]表示i的父节点。
#
# 初始化：每一个点都是一个集合，因此自己的父节点就是自己fa[i]=i
# 查询：每一个节点不断寻找自己的父节点，若此时自己的父节点就是自己，那么该点为集合的根结点，返回该点。
# 修改：合并两个集合只需要合并两个集合的根结点，即fa[RootA]=RootB，其中RootA,RootB是两个元素的根结点。
# 路径压缩：实际上，我们在查询过程中只关心根结点是什么，并不关心这棵树的形态(有一些题除外)。因此我们可以在查询操作的时候将访问过的每个点都指向树根，这样的方法叫做路径压缩，单次操作复杂度为O(logn),经过路径压缩后可将查询时间优化到O(1)
# 凡是这种动态的加入，查询某个集合的问题都可以考虑并查集
#
# 初始化father数组
# find数组中，当father[x]！=[x]时，不断循环查询，找到最小x,同时更新路径上的所有点的最小指向（路径压缩）来达到最快的查询速度
# connet中，若a,b未连接，通过father数组将a,b指向同一个块
# querry中，只需要通过find判断两者是否在同一个块即可
# 复杂度分析
#
# 时间复杂度O(n)
# 用了路径压缩，查询效率为O(1)
# 空间复杂度O(n)
# 需要一个大小为n的数组去记录每一个点的father

class ConnectingGraph:
    """
    @param: n: An integer
    """

    def __init__(self, n):  # 初始化
        self.father = {}
        for i in range(n + 1):
            self.father[i] = i

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):  # 合并
        roota, rootb = self.find(a), self.find(b);
        if roota != rootb:
            self.father[roota] = rootb;

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """

    def query(self, a, b):  # 询问
        return self.find(a) == self.find(b)

    def find(self, x):  # 查询
        # already root node
        if self.father[x] == x:
            return x

        # first we find the root node
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # then we do path compression
        while x != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

    """
    #递归写法
    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    """
