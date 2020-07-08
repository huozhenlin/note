#! /usr/bin/python3
# -*- coding: utf-8 -*-

# *=*=*=*=*=*=*=*=*=*=*

# author: sugar
# datetime: 2020/7/2 14:42

# *=*=*=*=*=*=*=*=*=*=*
import time
import requests
import hashlib

url = 'https://api.yonghuivip.com/api/item/get'

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'YhStore/5.35.0.35 cn.yonghui.hyd/2020042835 (client/phone; Android 23; Xiaomi/Redmi Note 4)',
    'X-YH-Biz-Params': 'lat=22.539404&lng=113.948477&cityid=13&sellerid=7&shopid=9479',
    'Host': 'api.yonghuivip.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

prarm = {
    'isfood': '0',
    'shopid': '9479',
    'pickself': '0',
    'lat': '22.539404',
    'lng': '113.948477',
    'code': 'R-1081971',
    'v': '5.35.0.35',
    'platform': 'Android',
    'deviceid': '8b5a347b-b3b5-4ee7-87e7-11ac73a4c5ae',
    'distinctId': '2578915d18ff736e',
    'channel': 'official',
    'timestamp': str(int(time.time() * 1000)),
}

par_str = 'YONGHUI601933' + ''.join('{}{}'.format(k, v) for k, v in prarm.items())

sign = hashlib.md5(par_str.encode()).hexdigest()
prarm['sign'] = sign

res = requests.get(url, params=prarm, headers=headers, verify=False)
print(res.json())

if __name__ == '__main__':
    print('main over')
