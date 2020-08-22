# coding=utf-8
import frida
import sys
ip45 = frida.get_usb_device()
session = ip45.attach("应用包名")

java = '''
Java.perform(function() {
	var TelephonyManager = Java.use("android.telephony.TelephonyManager");

    //IMEI hook
    TelephonyManager.getDeviceId.overload().implementation = function () {
               console.log("[*]Called - getDeviceId()");
               var temp = this.getDeviceId();
               console.log("real IMEI: "+temp);
               return "867979021642850";
    };
    // muti IMEI
    TelephonyManager.getDeviceId.overload('int').implementation = function (p) {
               console.log("[*]Called - getDeviceId(int) param is"+p);
               var temp = this.getDeviceId(p);
               console.log("real IMEI "+p+": "+temp);
               return "867979021642850";
    };


    //IMSI hook
    // 32001038210233399293
	TelephonyManager.getSimSerialNumber.overload().implementation = function () {
               console.log("[*]Called - getSimSerialNumber(String)");
               var temp = this.getSimSerialNumber();
               console.log("real IMSI: "+temp);
               return "123456789";
    };
    //////////////////////////////////////


    //ANDOID_ID hook
    var Secure = Java.use("android.provider.Settings$Secure");
    Secure.getString.implementation = function (p1,p2) {
    	if(p2.indexOf("android_id")<0) return this.getString(p1,p2);
    	console.log("[*]Called - get android_ID, param is:"+p2);
    	var temp = this.getString(p1,p2);
    	console.log("real Android_ID: "+temp);
    	return "844de23bfcf93801";

    }


    //android的hidden API，需要通过反射调用
    var SP = Java.use("android.os.SystemProperties");
    SP.get.overload('java.lang.String').implementation = function (p1) {
    	var tmp = this.get(p1);
    	console.log("[*]"+p1+" : "+tmp);
    	return tmp;
    }
    SP.get.overload('java.lang.String', 'java.lang.String').implementation = function (p1,p2) {


    	var tmp = this.get(p1,p2)
    	console.log("[*]"+p1+","+p2+" : "+tmp);
    	return tmp;
    } 
    
    // hook MAC
    var wifi = Java.use("android.net.wifi.WifiInfo");
    wifi.getMacAddress.implementation = function () {
    	var tmp = this.getMacAddress();
    	console.log("[*]real MAC: "+tmp);
    	return tmp;
    }

})
'''


def on_message(message, data):
    print(message)


script = session.create_script(java)
script.on('message', on_message)
script.load()
sys.stdin.read()

