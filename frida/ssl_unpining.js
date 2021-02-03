// start with:
//   frida -U -l pinning.js -f [APP_ID] --no-pause
Java.perform(function () {
    console.log('');
    console.log('===');
    console.log('* Injecting hooks into common certificate pinning methods *');
    console.log('===');

    var X509TrustManager = Java.use('javax.net.ssl.X509TrustManager');
    var SSLContext = Java.use('javax.net.ssl.SSLContext');

    // build fake trust manager
    var TrustManager = Java.registerClass({
        name: 'com.sensepost.test.TrustManager',
        implements: [X509TrustManager],
        methods: {
            checkClientTrusted: function (chain, authType) {
            },
            checkServerTrusted: function (chain, authType) {
            },
            getAcceptedIssuers: function () {
                return [];
            }
        }
    });

    // pass our own custom trust manager through when requested
    var TrustManagers = [TrustManager.$new()];
    var SSLContext_init = SSLContext.init.overload(
        '[Ljavax.net.ssl.KeyManager;', '[Ljavax.net.ssl.TrustManager;', 'java.security.SecureRandom'
    );
    try {
    SSLContext_init.implementation = function (keyManager, trustManager, secureRandom) {
        console.log('! Intercepted trustmanager request');
        SSLContext_init.call(this, keyManager, TrustManagers, secureRandom);
    }} catch (e) {
        console.log('* Unable to hook into SSLContext_init')
    }

    console.log('* Setup custom trust manager');

    // okhttp3
    try {
        var CertificatePinner = Java.use('okhttp3.CertificatePinner');
        CertificatePinner.check.overload('java.lang.String', 'java.util.List').implementation = function (str) {
            console.log('! Intercepted okhttp3: ' + str);
        };

        console.log('* Setup okhttp3 pinning')
    } catch(err) {
        console.log('* Unable to hook into okhttp3 pinner')
    }

    // trustkit
    try {
        var Activity = Java.use("com.datatheorem.android.trustkit.pinning.OkHostnameVerifier");
        Activity.verify.overload('java.lang.String', 'javax.net.ssl.SSLSession').implementation = function (str) {
            console.log('! Intercepted trustkit{1}: ' + str);
            return true;
        };

        Activity.verify.overload('java.lang.String', 'java.security.cert.X509Certificate').implementation = function (str) {
            console.log('! Intercepted trustkit{2}: ' + str);
            return true;
        };

        console.log('* Setup trustkit pinning')
    } catch(err) {
        console.log('* Unable to hook into trustkit pinner')
    }

    // TrustManagerImpl
    try {
        const ArrayList = Java.use("java.util.ArrayList");
        var TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
        TrustManagerImpl.checkServerTrusted.overload('[Ljava.security.cert.X509Certificate;', 'java.lang.String').implementation =
            function (chain, authType) {
                console.log('! Intercepted TrustManagerImpl');
            };

        TrustManagerImpl.checkServerTrusted.overload('[Ljava.security.cert.X509Certificate;', 'java.lang.String', 'java.lang.String').implementation =
            function (chain, authType, host) {
                console.log('! Intercepted TrustManagerImpl');
                return ArrayList.$new();
            };

        TrustManagerImpl.checkServerTrusted.overload('[Ljava.security.cert.X509Certificate;', 'java.lang.String', 'javax.net.ssl.SSLSession').implementation =
            function (chain, authType, session) {
                console.log('! Intercepted TrustManagerImpl');
                return ArrayList.$new();
            };

        if (Java.androidVersion > "6.0.1") {
            TrustManagerImpl.checkServerTrusted.overload('[Ljava.security.cert.X509Certificate;', 'java.lang.String', 'java.net.Socket').implementation =
            function (chain, authType, socket) {
                console.log('! Intercepted TrustManagerImpl');
            };
            TrustManagerImpl.checkServerTrusted.overload('[Ljava.security.cert.X509Certificate;', 'java.lang.String', 'javax.net.ssl.SSLEngine').implementation =
            function (chain, authType, engine) {
                console.log('! Intercepted TrustManagerImpl');
            };
        }
        console.log('* Setup TrustManagerImpl pinning');
    } catch (err) {
        console.log('* Unable to hook into TrustManagerImpl : ' + err.message);
    }

    // Appcelerator
    try {
        var PinningTrustManager = Java.use('appcelerator.https.PinningTrustManager');
        PinningTrustManager.checkServerTrusted.implementation = function () {
            console.log('! Intercepted Appcelerator');
        };

        console.log('* Setup Appcelerator pinning')
    } catch (err) {
        console.log('* Unable to hook into Appcelerator pinning')
    }

     // HttpsUrlConnection
    try {
        var HttpsURLConnection = Java.use('javax.net.ssl.HttpsURLConnection');
        HttpsURLConnection.setDefaultHostnameVerifier.implementation = function (verifier) {
            console.log('* Setup setDefaultHostnameVerifier');
        };
        HttpsURLConnection.setHostnameVerifier.implementation = function (verifier) {
            console.log('* Setup setHostnameVerifier');
        };
        HttpsURLConnection.setSSLSocketFactory.implementation = function (socketFactory) {
            console.log('* Setup setSSLSocketFactory')
        };
    } catch (err) {
        console.log('* Unable to hook into HttpsUrlConnection')
    }
});