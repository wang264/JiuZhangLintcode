#####基于数学方程的方法 假设最少尝试次数为x，那么，第一个鸡蛋必须要从第x层扔下，因为：如果碎了，
#前面还有x - 1层楼可以尝试，如果没碎，后面还有x-1次机会。如果没碎，第一个鸡蛋，第二次就可以
#从x +（x - 1）层进行尝试，为什么是加上x - 1，因为，当此时，第一个鸡蛋碎了，第二个鸡蛋还有可
#以从x+1 到 x + (x - 1) - 1层进行尝试，有x - 2次。如果还没碎，那第一个鸡蛋，第三次
#从 x + (x - 1) + (x - 2)层尝试。碎或者没碎，都有x -3次尝试机会，依次类推。那么，
#x次的最少尝试，可以确定的最高的楼层是多少呢？
#x + (x - 1) + (x - 2) + … + 1 = x(x+1) / 2
#那反过来问，当最高楼层是100层，最少需要多少次呢？x(x+1)/2 >= 100,
#得到x>=14，最少要尝试14次。

class Solution:
    # @param {int} n an integer
    # @return {int} an integer
    def dropEggs(self, n):
        # Write your code here
        import math
        x = int(math.sqrt(n * 2))
        while x * (x + 1) / 2 < n:
            x += 1
        return x