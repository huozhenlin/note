#coding:utf-8
#values是硬币的面值values = [ 25, 21, 10, 5, 1]
#valuesCounts   钱币对应的种类数
#money  找出来的总钱数
#coinsUsed   对应于目前钱币总数i所使用的硬币数目

from collections import defaultdict
dict = defaultdict(int)
def coinChange(values,valuesCounts,money,coinsUsed):
    #遍历出从1到money所有的钱数可能
    count = 0
    for cents in range(1,money+1):
        minCoins= cents
        #把所有的硬币面值遍历出来和钱数做对比
        for kind in range(0,valuesCounts):
            if (values[kind] <= cents):
                temp = coinsUsed[cents - values[kind]] +1
                if (temp < minCoins):
                    minCoins = temp

            count += 1
        coinsUsed[cents] = minCoins

        print ('面值:{0}的最少硬币使用数为:{1}'.format(cents, coinsUsed[cents]))
coinsUsed = dict
coinChange([1,3,4], 3, 100, coinsUsed)