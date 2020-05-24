import requests
import time
import datetime
import execjs
import os

from ws4py.client.threadedclient import WebSocketClient


class CG_Client(WebSocketClient):
    refer = "https://hotels.ctrip.com/hotel/beijing1"

    def opened(self):
        print("连接成功")
        self.send("Python")

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        print("resp", resp)
        today = datetime.datetime.now() # 今天，如 "2020-05-11"
        last_time = today + datetime.timedelta(hours = -24)
        tomorrow = last_time.strftime('%Y-%m-%d') # 明天，如 '2020-05-10'
        data = {
            "__VIEWSTATEGENERATOR": "DB1FBB6D",
            "cityName": "%E5%8C%97%E4%BA%AC",
            "StartTime": today,
            "DepTime": tomorrow,
            "RoomGuestCount": "1,1,0",
            "txtkeyword": "",
            "Resource": "",
            "Room": "",
            "Paymentterm": "",
            "BRev": "",
            "Minstate": "",
            "PromoteType": "",
            "PromoteDate": "",
            "operationtype": "NEWHOTELORDER",
            "PromoteStartDate": "",
            "PromoteEndDate": "",
            "OrderID": "",
            "RoomNum": "",
            "IsOnlyAirHotel": "F",
            "cityId": "1",
            "cityPY": "beijing",
            "cityCode": "010",
            "cityLat": "39.9105329229",
            "cityLng": "116.413784021",
            "positionArea": "",
            "positionId": "",
            "hotelposition": "",
            "keyword": "",
            "hotelId": "",
            "htlPageView": "0",
            "hotelType": "F",
            "hasPKGHotel": "F",
            "requestTravelMoney": "F",
            "isusergiftcard": "F",
            "useFG": "F",
            "HotelEquipment": "",
            "priceRange": "-2",
            "hotelBrandId": "",
            "promotion": "F",
            "prepay": "F",
            "IsCanReserve": "F",
            "k1": "",
            "k2": "",
            "CorpPayType": "",
            "viewType": "",
            "checkIn": today,
            "checkOut": tomorrow,
            "DealSale": "",
            "ulogin": "",
            "hidTestLat": "0%7C0",
            "AllHotelIds": "",
            "psid": "",
            "isfromlist": "T",
            "ubt_price_key": "htl_search_noresult_promotion",
            "showwindow": "",
            "defaultcoupon": "",
            "isHuaZhu": "False",
            "hotelPriceLow": "",
            "unBookHotelTraceCode": "",
            "showTipFlg": "",
            "traceAdContextId": "",
            "allianceid": "0",
            "sid": "0",
            "pyramidHotels": "",
            "hotelIds": "",
            "markType": "0",
            "zone": "",
            "location": "",
            "type": "",
            "brand": "",
            "group": "",
            "feature": "",
            "equip": "",
            "bed": "",
            "breakfast": "",
            "other": "",
            "star": "",
            "sl": "",
            "s": "",
            "l": "",
            "price": "",
            "a": "0",
            "keywordLat": "",
            "keywordLon": "",
            "contrast": "0",
            "PaymentType": "",
            "CtripService": "",
            "promotionf": "",
            "allpoint": "",
            "page_id_forlog": "102002",
            "contyped": "0",
            "productcode": "",
            "eleven": resp.data.decode("utf-8"),
            "orderby": "3",
            "ordertype": "0",
            "page": "1",

        }
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "referer": CG_Client.refer,
            "cookie": '_ga=GA1.2.36116837.1532746091; _RSG=hOKpPODzqW0TIuiz80oo0A; _RDG=2867744103ed082c0e304e28b524544aba; _RGUID=0834f4d6-19cd-462b-a032-c8023db3849d; HotelDomestic_CitySight=105=2821419; _HGUID=PXST%06T%04VMQY%03%04MTVR%02M%01PSRM%03XPRS%04%02SXTY%04; _abtest_userid=57accdbe-bfc6-4331-b588-addf359ae51e; login_type=0; UUID=475B909CCD9B4B7DBC47FA657E4249A5; IsPersonalizedLogin=T; GUID=09031049411948336619; magicid=cevIaS7Cmyi+9uDU5gHNSCt8+s6cjR8FMTaFUnrykozBaLSQv4yIN4/TI76Mhhde; hoteluuid=OT9hVAFplTMpCXm5; login_uid=FA045FF2B557259934E68FFC12419522; MKT_CKID=1575449888489.jlq6e.3oos; __utmz=13090024.1576477940.41.3.utmcsr=ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; nfes_isSupportWebP=1; clientid=51482081210773029412; ASP.NET_SessionId=gxqyc44utoutj0v3rmwscvic; OID_ForOnlineHotel=15327460909811eqb6kz1588230664762102032; MKT_Pagesource=PC; fcerror=859228016; _zQdjfing=3a923ad5c08665b02e3365ac3365ac3a923a4ea0841336fa275ad0; Union=AllianceID=1095794&SID=2280904&OUID=; Session=SmartLinkCode=U2280904&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _gid=GA1.2.786169211.1589785184; MKT_CKID_LMT=1589785185048; ASP.NET_SessionSvc=MTAuMTQuMjA2LjF8OTA5MHxvdXlhbmd8ZGVmYXVsdHwxNTg5MDA0OTY5NDAw; IntlIOI=F; IntHotelCityID=274split%25u9996%25u5C14%25uFF0C%25u97E9%25u56FDsplitseoulsplit2020-05-19split2020-05-20splitsplitsplit2split2split1; __utma=13090024.36116837.1532746091.1587347790.1589785198.98; __utmc=13090024; HotelDomesticVisitedHotels1=36259023=0,0,0,6,/200114000000w439k946E.jpg,&667677=0,0,4.4,2089,/200o10000000pbdvgE30E.jpg,&1109498=0,0,4.2,1539,/200n0k000000bhu7o8AB0.jpg,&39493926=0,0,4.9,2452,/200a1600000105mnaDE93.jpg,&1775498=0,0,4.5,197,/200l1700000134da0969A.jpg,&56796268=0,0,5,99,/200c1c000001dqnxrE4E5.jpg,; HotelCityID=99split%E9%93%B6%E5%B7%9Dsplityinchuansplit2020-05-18split2020-05-19split0; _RF1=27.38.251.191; _gat=1; _jzqco=%7C%7C%7C%7C1586744357116%7C1.931833407.1532746091763.1589821079528.1589821967883.1589821079528.1589821967883.undefined.0.0.3086.3086; __zpspc=9.527.1589821079.1589821967.2%233%7Cwww.google.com%7C%7C%7C%7C%23; appFloatCnt=669; _bfi=p1%3D102002%26p2%3D102002%26v1%3D4344%26v2%3D4342; hoteluuidkeys=ZLkIaoiQoe40v1AyTYDYQMY1bEnYhYU9ePTE41jFBW7YZYkSjtowZnJfTjcYQYNDeBswLPIT1jMYlY74rqfw6lrPBjLYhY7PvN8Yh7yOQjn3vsSefTYZOjH5ydYDYD7vz6vTXY5UwNMjT4etkiNTY9YhY0Y5YgcrctEtOwsHxcsYntjLMjTtWoY7YbYLYTGEXAKp9wa3imFR1djArdXYOqJhAyArAMYHbWlUvZ3xnDe3gYoMxqdx50YqDihmw0oj61Ed1JsHWPOjOrPmJAUiHcwqLv8BRA6jclYUQjnrT4yX3i9zwQnRgcEZpj03xkaxocEm8E6FEtnWH6e4Ow6sEmMjZAeqNi4PYBmrzFeZqek1xU1i6NiSDxaZW4Pj5ce5zwfsKtcwcMi7gRsGjD0eB4E79ycpvN1iaZEhgyc7vsdK68ETAKU3w74i0oRNajkrpqYt8J7Oy4rL7jFgeXzjqNKBFjFTwfDxzaxhdxk4x4QEQOEOGEBhWb8es0wMhEZGjOMe0Nis4Y0Fr8fEmNyUkvdhilDEQ9ymlvDtKdoW8ZELtjzmegmx7tj9rAhE36WHBef0jGpYqkjh5xOAxPbxp6xO6E9lEkLE1DWhQeUkw5bEqQjcGesmi0cYU3roDeP3ecGY8fE6zw4lWP7i33KO3EQ3Et6EoHWhLeTtwBFE3GjDseLniFsYdOrMpezTekzE8PYhqEd6wpGWkmisYoY5UYqpigLihSis5jgYfYS5WOUJq5v6QysNJ1BiBfi4sJLY0YUaRLTJHNjcDvA5j4SYNnRn7vNHjLPWH7yhpWcQj9YzYpPRkBwthvNgKlnjSfY54ytQEdAW1dw8Pr7HEB4Ellx9cRqNJ3YOYPLRNzJc5iD4YZFy1lEBUwcPWS4vqpWsAvHfjZdRFYMYtzj31wSnvFA; _bfa=1.1532746090981.1eqb6kz.1.1589808972221.1589821076411.726.4345.153001; _bfs=1.5; hotelhst=1383169248'
        }
        url = "https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"
        a = requests.post(url, data=data, headers=headers)
        print(a.text)
        ws.close()

def getTime():
    # 或者事件戳
    return str(time.time).replace(".", "")[:-4]

def getCallbackParam():
    # 获取callback参数
    f = open("./callback.js")
    context = execjs.compile(f.read())
    return context.call("getCallback")


def getContent():
    t = getTime()
    callback = getCallbackParam()
    url = "https://hotels.ctrip.com/domestic/cas/oceanball?callback=%s&_=%s" % (
        callback,
        t,
    )
    headers = {
        "user-agent": "Mozilla/5.0 (darwin) AppleWebKit/537.36 (KHTML, like Gecko) jsdom/16.2.2",
        "referer": CG_Client.refer
    }
    r = requests.get(url, headers=headers)

    code = """
        window["%s"] = function (e) {
        var f = e();
        console.log(f);
        ws.send(f);
    };;
    """ % callback + r.text
    ws.send(code)

ws = None
try:
    ws = CG_Client('ws://127.0.0.1:8014/')
    ws.connect()
    getContent()
    ws.run_forever()

except KeyboardInterrupt:
    ws.close()