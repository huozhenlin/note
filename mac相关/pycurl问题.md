```bash
pip3.5 uninstall pyOpenSSL  
pip3.5 install pyOpenSSL  
pip3.5 install --trusted-host pypi.org --trusted-host files.pythonhosted.org pycurl  
```  
# 说明:
mac下，在安装某些软件的时候提示如上错误，但是mac已经安装了openssl。

原因：openssl是mac不推荐的加密方式，因为mac有自己的一套加密方式，于是，其他软件安装的时候找不到openssl路径

解决办法：查看出问题的代码，比如：某个*.c文件提示  #include <openssl/ssl.h>找不到文件ssl.h。那么直接在找到openssl的安装路径(brew --prefix openssl)，在路径下找到代码ssl.h,然后拷贝一份放到*.c文件的同目录的openssl目录下