> 资源链接


[Mirror of google-chrome](http://npm.taobao.org/mirrors/chromedriver/)  

> 安装selenium  


```python
pip3 install selenium = 3.14.0
```
> 安装驱动  


```shell
1. chomd -X chromedriver
2. mv chromedirver /usr/local/share/chromedriver 
3. ln -s /usr/share/chromedriver /usr/bin/chromedriver
```
> 安装google浏览器  


[下载链接](https://www.chrome64bit.com/index.php/google-chrome-64-bit-for-linux)

> 测试  


```python
from selenium import webdriver


url = 'http://www.baidu.com'
chrome = webdriver.Chrome()
chrome.get(url)
print(chrome.page_source)
```

> Tips


1. 如何给chrome添加参数，如设置代理? 

```pyhton
chromeOptions = selenium.webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server={}".format(random.choice(list(self.ips))))
chromeOptions.add_argument(
    'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"')
```

2. 浏览器不加载图片

```python
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
chromeOptions.add_experimental_option("prefs", prefs)
```