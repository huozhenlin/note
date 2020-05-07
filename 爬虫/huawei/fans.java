import android.util.Base64;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class fans {
    private static final String bic = "HmacSHA256";
    private static final String arg1 = "GET&/huawei/apk/clientreq.php&channelID=0001&EmuiVer=EmotionUI_1.6&interface=gethandphotoevent&MachineID=Redmi%2BNote%2B2&num=10&seq=1&start=61&ver=10&versionCode=100004031&&appid=7910&timestamp=1588820053";
    private static final String arg2 = "70a35b3dba211ede465f11bfc1c2a41da084cc379263ea89675f926ac116ca65";
    private static final String result = "ZIrF5C0Iae6jSTdtT3/j1jT+5gVTxZr2qF1l0eunKIA=";


    private byte[] L(String str, String str2) {
        try {
            SecretKeySpec secretKeySpec = new SecretKeySpec(str2.getBytes("UTF-8"), bic);
            Mac instance = Mac.getInstance(bic);
            instance.init(secretKeySpec);
            return instance.doFinal(str.getBytes("UTF-8"));
        } catch (Exception e) {
//            zf.e(e.getMessage());
            return new byte[0];
        }
    }

    private String K(String str, String str2) {
        return Base64.encodeToString(L(str, str2), 2);
    }

    public static void main(String args[]){
        System.out.println(result.equals(new fans().K(arg1, arg2)));
    }
}
