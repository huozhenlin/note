#coding:utf-8
#values是硬币的面值values = [ 25, 21, 10, 5, 1]
#valuesCounts   钱币对应的种类数
#money  找出来的总钱数
#coinsUsed   对应于目前钱币总数i所使用的硬币数目

# from collections import defaultdict
# dict = defaultdict(int)
# def coinChange(values,valuesCounts,money,coinsUsed):
#     #遍历出从1到money所有的钱数可能
#     for cents in range(1,money+1):
#         minCoins= cents
#         #把所有的硬币面值遍历出来和钱数做对比
#         for kind in range(0,valuesCounts):
#             if (values[kind] <= cents):
#                 temp = coinsUsed[cents - values[kind]] +1
#                 if (temp < minCoins):
#                     minCoins = temp
#         coinsUsed[cents] = minCoins
#
#         print ('面值:{0}的最少硬币使用数为:{1}'.format(cents, coinsUsed[cents]))
# coinsUsed = dict
# coinChange([1,3,4], 3, 100, coinsUsed)

from collections import defaultdict
def coinChange(A=[3, 4, 5], M=27):
    """
    :param values: 面值
    :param coin: 面值种类数
    :param value: 找零值
    :return:
    """

    f = defaultdict(int) # 存放找第n块钱需要多少硬币
    f[0] = -0 # 无穷大
    for i in range(1, M+1):
        f[i] = float('inf')
        for j in range(0, len(A)):
            # 避免数据越界
            if i >= A[j] and (f[i-A[j]] + 1) != float('inf'):
                f[i] = min(f[i-A[j]] + 1, f[i])
        print('面值:{0}的最少硬币使用数为:{1}'.format(i, f[i]))

coinChange()