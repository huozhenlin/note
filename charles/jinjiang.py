import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; AOSP on HammerHead Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36;webank/h5face;webank/1.0;netType:NETWORK_WIFI;appVersion:429;packageName:com.plateno.botaoota;/wehotel botao v=4.2.9",

    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "channelCode": "CA00001"
}


def get_cityCode():
    """获取cityCode"""
    url = 'https://booking.bestwehotel.com/apph5/proxy/trip-basic/basic/getCity'
    body = {
        "country": 0,
        "sceneType": 0,
        "channelCode": "CA00001",
        "languageCode": 0,
        "clientInfo": {
            "appName": "botao",
            "appVersion": "4.2.9",
            "channelId": "306267",
            "deviceId": "359250053008551",
            "hardwareModel": "hammerhead",
            "os": "android",
            "partakeChannel": "a00",
            "scr": "9b48d7ab86736a099740f90d47e7c7a4",
            "sellerId": "306267",
            "shareCardNo": "",
            "systemVersion": "5.1",
            "versionCode": "429"
        }
    }
    response = requests.post(url=url, data=json.dumps(body), headers=headers)
    print(response.text)


def get_hoteList():
    url = 'https://booking.bestwehotel.com/apph5/proxy/trip-search/search/findHotel'
    body = {
        "cityCode": "AR05223",
        "checkInDate": 1585731946233,
        "checkOutDate": 1585818346233,
        "page": 1,
        "pageSize": 20,
        "channelCode": "CA00001"
    }
    response = requests.post(url=url, data=json.dumps(body), headers=headers)
    print(response.text)

get_cityCode()
get_hoteList()
