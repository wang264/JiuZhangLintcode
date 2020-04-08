# 437. Copy Books
# 中文English
# Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.
#
# These books list in a row and each person can claim a continous range of books. For example,
# one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book,
# 2nd book and 4th book (without 3rd book).
#
# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
# What's the best strategy to assign books so that the slowest copier can finish at earliest time?
#
# Return the shortest time that the slowest copier spends.
#
# Example
# Example 1:
#
# Input: pages = [3, 2, 4], k = 2
# Output: 5
# Explanation:
#     First person spends 5 minutes to copy book 1 and book 2.
#     Second person spends 4 minutes to copy book 3.
# Example 2:
#
# Input: pages = [3, 2, 4], k = 3
# Output: 4
# Explanation: Each person copies one of the books.
# Challenge
# O(nk) time
#
# Notice
# The sum of book pages is less than or equal to 2147483647

import sys


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    # f[k][i] = the minimum amount of time for k persons to finish first i books.

    # 枚举最后一个人。
    # f[k][j] = min(   max(f[k-1][j], A[j]+...A[i-1] )   for 0<=j<=i) )
    def copyBooks_slow(self, pages, k):
        # write your code here
        n = len(pages)
        f = [[0] * (n + 1) for _ in range(k + 1)]
        if k > n:
            k = n
        for j in range(1, n + 1):
            f[0][j] = sys.maxsize  # it take infinity time for 0 people to read any none zero amount of book.

        f[0][0] = 0  # it take 0 minute for 0 people to read 0 books.
        for kk in range(1, k + 1):
            for i in range(1, n + 1):
                f[kk][i] = sys.maxsize
                for j in range(0, i + 1):  # 0<=j<=i 枚举最后一个人抄的书，可以不抄。
                    # max(f[k-1][j], sum(pages[j:i])) 前j本书给前面的k-1个人读，最后一个人读第j+1到第i本。
                    if f[kk - 1][j] == sys.maxsize:
                        continue
                    f[kk][i] = min(f[kk][i], max(f[kk - 1][j], sum(pages[j:i])))

        return f[k][n]

    def copyBooks(self, pages, k):
        # write your code here
        n = len(pages)
        f = [[0] * (n + 1) for _ in range(k + 1)]
        if k > n:
            k = n

        for j in range(1, n + 1):
            f[0][j] = sys.maxsize  # it take infinity time for 0 people to read any none zero amount of book.

        f[0][0] = 0  # it take 0 minute for 0 people to read 0 books.
        for kk in range(1, k + 1):
            for i in range(1, n + 1):
                f[kk][i] = sys.maxsize
                sum_range = 0
                for j in reversed(range(0, i + 1)):  # 0<=j<=i 枚举最后一个人抄的书，可以不抄。
                    # max(f[k-1][j], sum(pages[j:i])) 前j本书给前面的k-1个人读，最后一个人读第j+1到第i本。
                    if f[kk - 1][j] != sys.maxsize:
                        f[kk][i] = min(f[kk][i], max(f[kk - 1][j], sum_range))
                    if j >= 1:
                        sum_range += pages[j - 1]

        return f[k][n]


sol = Solution()
pages = [8720, 1593, 4278, 1018, 9515, 5536, 8694, 869, 8423, 9920, 3425, 9689, 9908, 1404, 8371, 6019, 7531, 943, 9280,
         8058, 1445, 7485, 9223, 5067, 736, 6065, 1724, 3269, 130, 1297, 1701, 5585, 1209, 5901, 3760, 3216, 5307, 8534,
         9575, 7135, 1251, 3531, 5162, 7432, 8559, 2024, 9738, 2621, 7926, 3865, 9904, 4763, 2031, 4561, 5870, 6033,
         6442, 6405, 9886, 8455, 8970, 6746, 7923, 5222, 274, 3875, 5821, 816, 3459, 9916, 9447, 4252, 1871, 5784, 8272,
         9526, 1531, 5647, 6676, 2416, 6281, 7878, 4382, 5376, 3618, 1158, 3717, 5573, 5602, 5919, 7579, 6628, 929,
         6897, 8324, 8657, 8342, 8190, 7384, 2466, 8715, 2499, 9144, 7349, 3236, 2852, 4613, 1917, 5345, 9288, 9205,
         3363, 5008, 156, 4716, 6924, 3490, 605, 3872, 577, 5393, 7941, 7390, 7042, 8242, 5376, 5939, 3910, 4727, 4053,
         4850, 5531, 2658, 3876, 9379, 6157, 7544, 2845, 5499, 459, 3119, 2984, 5567, 5706, 1507, 5971, 8369, 8177,
         5985, 1215, 8258, 2925, 9193, 7999, 334, 4761, 2586, 7770, 195, 5804, 3898, 7214, 6625, 2975, 4078, 5441, 9944,
         4161, 9225, 7012, 6383, 4441, 4474, 7030, 7292, 6938, 48, 6253, 4707, 2078, 8449, 7011, 65, 7205, 4841, 2066,
         5097, 3875, 6431, 2626, 6325, 789, 5047, 324, 3528, 1325, 2443, 281, 3094, 1908, 9686, 8720, 9310, 6817, 1856,
         2137, 7718, 1180, 5988, 8766, 3408, 8439, 2555, 2214, 2678, 1991, 7393, 6323, 9586, 8430, 3298, 9828, 9386,
         5406, 12, 7231, 8808, 3655, 208, 6314, 246, 6279, 9172, 9980, 5042, 5659, 7293, 5428, 2789, 6454, 2887, 5948,
         6895, 847, 1443, 754, 4889, 9509, 2008, 7163, 5297, 3845, 7290, 636, 1900, 7035, 2718, 6348, 9216, 2577, 9852,
         3935, 412, 6605, 3786, 2158, 9280, 9835, 8941, 2575, 2868, 9006, 6860, 8101, 3714, 7940, 268, 8199, 5597, 9898,
         982, 2825, 5125, 9865, 3008, 7575, 8914, 7330, 4410, 2063, 214, 3625, 1588, 8894, 7882, 503, 8305, 2701, 8230,
         1336, 1946, 1318, 2314, 7348, 3387, 670, 3682, 7588, 9411, 3812, 2509, 1106, 6148, 9162, 3716, 9041, 4980,
         2057, 251, 1778, 7969, 2805, 5764, 1266, 6531, 5219, 8550, 1921, 9687, 8127, 826, 4642, 9398, 4097, 512, 3296,
         2618, 5132, 2890, 3471, 2757, 6336, 5853, 789, 980, 9109, 5240, 9449, 758, 8198, 3420, 4998, 4239, 995, 5805,
         1997, 9124, 1265, 694, 8920, 1770, 3965, 9473, 6176, 9059, 6479, 3190, 8678, 7136, 9005, 6420, 1664, 8229,
         8838, 6959, 8267, 3220, 8445, 7166, 7999, 6727, 4942, 8306, 5704, 2005, 9106, 6139, 1954, 8219, 1707, 150,
         9456, 2125, 9215, 6515, 3446, 2391, 5560, 2031, 4940, 7600, 5852, 6911, 6330, 571, 1691, 4217, 9403, 8555,
         4183, 7995, 8398, 7931, 7509, 127, 2514, 7970, 47, 7970, 2914, 9730, 86, 12, 723, 4736, 8464, 1108, 5422, 5102,
         57, 3366, 9275, 7030, 7054, 1230, 9787, 9268, 8967, 2653, 1453, 5486, 7214, 3899, 9681, 315, 965, 7969, 8778,
         7791, 2656, 3646, 988, 261, 3800, 1317, 9497, 386, 243, 7713, 9333, 1563, 9973, 4759, 4799, 6150, 2865, 5293,
         9948, 8505, 1550, 1240, 321, 2195, 1521, 2108, 1552, 3275, 6184, 2752, 9108, 3932, 1909, 5232, 2702, 3743,
         1181, 7464, 1925, 4419, 8051, 796, 893, 1317, 4384, 8060, 4508, 4579, 5755, 6765, 1733, 117, 7343, 2719, 154,
         5986, 5197, 2767, 7902, 2574, 606, 2351, 558, 2739, 5230, 310, 3186, 9391, 6219, 8236, 6141, 668, 9697, 1218,
         4273, 8812, 3986, 2631, 6865, 6216, 9427, 3287, 5480, 1000, 8315, 3384, 4275, 630, 9182, 8713, 9918, 3415,
         3572, 9152, 6451, 8058, 9499, 1922, 1988, 1525, 3348, 6806, 6996, 9026, 7077, 6816, 6489, 3395, 3714, 3595,
         1134, 7325, 3761, 4924, 1157, 4308, 9439, 2307, 9943, 821, 4355, 5258, 5927, 9518, 6464, 3397, 942, 8028, 3266,
         639, 62, 2752, 5404, 2183, 2678, 8969, 7628, 6666, 8509, 1246, 5546, 6889, 6537, 3432, 47, 4987, 7518, 1844,
         7433, 2957, 9424, 8790, 620, 6029, 7828, 8353, 5974, 8560, 4415, 4788, 1794, 9941, 7061, 4465, 5854, 316, 5598,
         7581, 5248, 1008, 7063, 1562, 3062, 1903, 7599, 3556, 3807, 7722, 7223, 1664, 8909, 4789, 1482, 9222, 2706,
         1275, 3133, 5968, 588, 6682, 8964, 3264, 2602, 9032, 559, 7110, 974, 8997, 9697, 9367, 2028, 4764, 3815, 8957,
         8214, 1710, 5591, 1100, 4609, 9684, 9279, 7118, 256, 5260, 633, 4223, 5345, 3597, 5404, 380, 1414, 5893, 3404,
         8497, 7643, 7964, 7377, 5257, 1343, 5333, 9756, 8275, 9046, 3683, 3874, 6575, 4983, 1321, 9673, 8735, 624,
         4445, 3940, 8732, 620, 3404, 3246, 6625, 4801, 3359, 8994, 7877, 2082, 1077, 8220, 8439, 3208, 362, 3282, 399,
         4196, 104, 2410, 9877, 9678, 6326, 1443, 1647, 8627, 5171, 9869, 4092, 9068, 7882, 5249, 3254, 8011, 9659,
         7355, 3520, 6863, 6891, 2744, 7413, 6916, 1100, 3316, 8290, 4895, 7062, 6393, 78, 8002, 3826, 8206, 1122, 2555,
         2084, 5833, 6819, 9490, 6316, 9488, 8609, 4711, 3897, 2446, 7384, 27, 8203, 137, 5780, 1161, 9041, 8716, 3669,
         3225, 1991, 9653, 7780, 313, 2234, 3678, 9120, 1253, 9659, 3745, 3469, 5496, 6550, 8747, 7934, 5594, 5987,
         5323, 1277, 6221, 6939, 9121, 4829, 331, 3666, 9932, 5244, 3512, 704, 4269, 1726, 2382, 8691, 7536, 8362, 7610,
         9446, 1255, 2997, 7226, 1821, 1726, 7208, 6087, 3478, 5167, 1880, 4998, 5870, 9032, 3941, 7188, 1880, 8584,
         179, 4042, 239, 3004, 2414, 4613, 8279, 6636, 2603, 9247, 3039, 7669, 2180, 7440, 3274, 5366, 2395, 2214, 3257,
         4791, 2081, 1631, 6292, 4254, 3733, 9828, 3644, 3522, 2550, 4424, 9989, 7654, 118, 3505, 216, 5902, 4131, 2754,
         3333, 4072, 5624, 4975, 1160, 3900, 7783, 1200, 1361, 9290, 9284, 1251, 9817, 6255, 4832, 8680, 3667, 8141,
         8951, 1507, 6395, 4189, 9869, 7080, 2084, 5060, 5153, 5762, 5680, 7705, 8415, 2142, 5837, 6711, 8460, 3254,
         5306, 869, 2364, 7737, 3892, 9618, 605, 2948, 9414, 371, 4397, 3807, 1720, 9327, 961, 3598, 573, 6542, 8806,
         3522, 2166, 3899, 9642, 8781, 1321, 6424, 7085, 5827, 3592, 9206, 8494, 9878, 8889, 8246, 3800, 7856, 4523,
         2859, 7029, 7764, 7891, 1825, 2165, 2544, 9758, 6080, 6399, 121, 759, 1222, 5545, 2181, 9505, 7805, 6212, 2743,
         3059, 9952, 2826, 5660, 4951, 9826, 6066, 3340, 2614, 9186, 8971, 8866, 832, 319, 4276, 1441, 5118, 5409, 2587,
         9550, 2542, 3995, 4005, 2197, 6265, 6070, 9324, 8711, 9977, 5444, 296, 8550, 3154, 5899, 3510, 1093, 6249,
         8534, 4619, 1096, 3509, 5261, 6209, 1289, 8425, 3941, 4955, 3570, 5466]
sol.copyBooks(pages=pages, k=165)
