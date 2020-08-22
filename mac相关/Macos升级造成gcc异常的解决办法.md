# 前序  
macos升级至10.15后，python抱pycurl包错误  
```bash
huozhenlindeMacBook-Air:tornado-api-zhenlinhuo-py3 huozhenlin$ pip3 install pycurl
Collecting pycurl
  Using cached https://files.pythonhosted.org/packages/ac/b3/0f3979633b7890bab6098d84c84467030b807a1e2b31f5d30103af5a71ca/pycurl-7.43.0.3.tar.gz
Installing collected packages: pycurl
  Running setup.py install for pycurl ... error
    ERROR: Command errored out with exit status 1:
     command: /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-zgaf0dpq/pycurl/setup.py'"'"'; __file__='"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-zgaf0dpq/pycurl/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-record-9_1i0yzh/install-record.txt --single-version-externally-managed --compile
         cwd: /private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-zgaf0dpq/pycurl/
    Complete output (21 lines):
    Using curl-config (libcurl 7.64.1)
    Not using an SSL library
    running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.9-x86_64-3.6
    creating build/lib.macosx-10.9-x86_64-3.6/curl
    copying python/curl/__init__.py -> build/lib.macosx-10.9-x86_64-3.6/curl
    running build_ext
    building 'pycurl' extension
    creating build/temp.macosx-10.9-x86_64-3.6
    creating build/temp.macosx-10.9-x86_64-3.6/src
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch x86_64 -g -DPYCURL_VERSION="7.43.0.3" -DHAVE_CURL_SSL=1 -I/Library/Frameworks/Python.framework/Versions/3.6/include/python3.6m -c src/docstrings.c -o build/temp.macosx-10.9-x86_64-3.6/src/docstrings.o
    dyld: Symbol not found: _OBJC_IVAR_$_NSFont._fFlags
      Referenced from: /Applications/Xcode.app/Contents/SharedFrameworks/DVTDocumentation.framework/Versions/A/../../../../SharedFrameworks/DVTKit.framework/Versions/A/DVTKit
      Expected in: /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
     in /Applications/Xcode.app/Contents/SharedFrameworks/DVTDocumentation.framework/Versions/A/../../../../SharedFrameworks/DVTKit.framework/Versions/A/DVTKit
    gcc: error: unable to locate xcodebuild, please make sure the path to the Xcode folder is set correctly!
    gcc: error: You can set the path to the Xcode folder using /usr/bin/xcode-select -switch
    Warning: libcurl is configured to use SSL, but we have not been able to determine which SSL backend it is using. If your Curl is built against OpenSSL, LibreSSL, BoringSSL, GnuTLS, NSS or mbedTLS please specify the SSL backend manually. For other SSL backends please ignore this message.error: command 'gcc' failed with exit status 71
    ----------------------------------------
ERROR: Command errored out with exit status 1: /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-zgaf0dpq/pycurl/setup.py'"'"'; __file__='"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-zgaf0dpq/pycurl/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-record-9_1i0yzh/install-record.txt --single-version-externally-managed --compile Check the logs for full command output.
WARNING: You are using pip version 19.2.1, however version 19.2.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
huozhenlindeMacBook-Air:tornado-api-zhenlinhuo-py3 huozhenlin$ pip3 install --install-option="--with-openssl" --install-option="--openssl-dir=/usr/local/opt/openssl" pycurl
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pip/_internal/commands/install.py:243: UserWarning: Disabling all use of wheels due to the use of --build-options / --global-options / --install-options.
  cmdoptions.check_install_build_global(options)
Collecting pycurl
  Using cached https://files.pythonhosted.org/packages/ac/b3/0f3979633b7890bab6098d84c84467030b807a1e2b31f5d30103af5a71ca/pycurl-7.43.0.3.tar.gz
Installing collected packages: pycurl
  Running setup.py install for pycurl ... error
    ERROR: Command errored out with exit status 1:
     command: /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-cicrgd7n/pycurl/setup.py'"'"'; __file__='"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-cicrgd7n/pycurl/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-record-3dyxo0fo/install-record.txt --single-version-externally-managed --compile --with-openssl --openssl-dir=/usr/local/opt/openssl
         cwd: /private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-cicrgd7n/pycurl/
    Complete output (21 lines):
    Using curl-config (libcurl 7.64.1)
    Using SSL library: OpenSSL/LibreSSL/BoringSSL
    running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.9-x86_64-3.6
    creating build/lib.macosx-10.9-x86_64-3.6/curl
    copying python/curl/__init__.py -> build/lib.macosx-10.9-x86_64-3.6/curl
    running build_ext
    building 'pycurl' extension
    creating build/temp.macosx-10.9-x86_64-3.6
    creating build/temp.macosx-10.9-x86_64-3.6/src
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch x86_64 -g -DPYCURL_VERSION="7.43.0.3" -DHAVE_CURL_SSL=1 -DHAVE_CURL_OPENSSL=1 -DHAVE_CURL_SSL=1 -I/usr/local/opt/openssl/include -I/Library/Frameworks/Python.framework/Versions/3.6/include/python3.6m -c src/docstrings.c -o build/temp.macosx-10.9-x86_64-3.6/src/docstrings.o
    dyld: Symbol not found: _OBJC_IVAR_$_NSFont._fFlags
      Referenced from: /Applications/Xcode.app/Contents/SharedFrameworks/DVTDocumentation.framework/Versions/A/../../../../SharedFrameworks/DVTKit.framework/Versions/A/DVTKit
      Expected in: /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
     in /Applications/Xcode.app/Contents/SharedFrameworks/DVTDocumentation.framework/Versions/A/../../../../SharedFrameworks/DVTKit.framework/Versions/A/DVTKit
    gcc: error: unable to locate xcodebuild, please make sure the path to the Xcode folder is set correctly!
    gcc: error: You can set the path to the Xcode folder using /usr/bin/xcode-select -switch
    error: command 'gcc' failed with exit status 71
    ----------------------------------------
ERROR: Command errored out with exit status 1: /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-cicrgd7n/pycurl/setup.py'"'"'; __file__='"'"'/private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-install-cicrgd7n/pycurl/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/xw/y43yg20s23x7t1_1gwsjq1_h0000gn/T/pip-record-3dyxo0fo/install-record.txt --single-version-externally-managed --compile --with-openssl --openssl-dir=/usr/local/opt/openssl Check the logs for full command output.

```

1. 卸载pycurl  
```bash
pip3 uninstall pycurl
```

2. 切换xcode  
```bash
sudo xcode-select --switch /Library/Developer/CommandLineTools/
```
3. 安装pycurl  
```bash
pip3 install pycurl --compile --no-cache-dir
```

## 参考连接  
https://blog.csdn.net/mysteryhaohao/article/details/101196619  
https://www.jianshu.com/p/fd8953f36fc4  
https://www.jianshu.com/p/8c8933eebdf3  
https://wfuzz.readthedocs.io/en/latest/user/installation.html  
