# 前言  
puppeteer(木偶)，是Google Chrome团队出品的一款无界面Chrome工具，它提供了丰富的API，让开发者像
鼠标一样控制浏览器的各种行为。它是一个node库，所以安装nodejs以及npm包管理器  

## 安装nodejs及npm  
```bash
apt-get install nodejs  
apt-get install npm
```
## 查看node版本号 
```bash
node -v
``` 
## 升级node版本  [详细教程](https://newsn.net/say/node-n.html)
* 全局安装n模块  
```bash
npm install n -g
```
* 切换node版本  
```bash
sudo n
```
有时候明明版本切换了，终端仍显示旧的版本号怎么办？
原因1：node被nvm接管了。因此，可以通过以下命令切换回来  
```bash
export NODE_HOME=/usr/local
export PATH=$NODE_HOME/bin:$PATH
export NODE_PATH=$NODE_HOME/lib/node_modules:$PATH
```  

## 安装puppeteer  
由于安装puppeteer的时候，会额外去下载chromeium包，chromium下载服务器在国外，因此，很多puppeteer
安装失败的原因就是chromeium下载失败。解决办法有哪些呢？  
1. 只安装puppeteer不安装chromeium  [详细教程](https://juejin.im/post/5b4a043751882519790c7ad7)
```bash
npm install puppeteer --ignore-scripts
```
然后在脚本中通过配置项 executablePath，指定 Chromium 所在的位置。示例：  
```javascript
const puppeteer = require('puppeteer');


(async () => {
    const browser = await puppeteer.launch({
        executablePath: '../../chromium/Chromium.app/Contents/MacOS/Chromium'
    });
    const page = await browser.newPage();
    await page.goto('https://y.qq.com');
    await page.screenshot({path: 'yqq.png'});
    browser.close();
})(); 

```
手动下载Chromuim。墙里下载不到Chromuim怎么办。看仓库源码可以发现下载地址是这样的  
```javascript
const downloadURLs = {
    linux: 'https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/%d/chrome-linux.zip',
    mac: 'https://storage.googleapis.com/chromium-browser-snapshots/Mac/%d/chrome-mac.zip',
    win32: 'https://storage.googleapis.com/chromium-browser-snapshots/Win/%d/chrome-win32.zip',
    win64: 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/%d/chrome-win32.zip'
}
```
选择对应的平台，将 %d 替换成具体的编号,编号可以从 puppeteer/package.json 中的 puppeteer.chromium_revision查看 
2. 切换npm源，使用国内源  [详细教程](https://blog.csdn.net/weixin_34013044/article/details/90964131)  

永久使用  
```bash
npm config set registry https://registry.npm.taobao.org
``` 
临时使用  
```bash
npm --registry https://registry.npm.taobao.org install express
```  

## 其他问题  
在mac上安装完chromium后能立即使用，在ubuntu上可能存在这些问题  
1. 共享资源库找不到  [详细教程](https://askubuntu.com/questions/1091101/error-libgtk-3-so-0-not-installed-even-though-its-in-usr-lib-x86-64-linux-gnu)  
```bash
sudo apt-get install libgtk-3.so.0
sudo ldconfig
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libgtk-3-0:i386
```  

2. 仅有终端操作的ubuntu，启动chromeium报错  
```bash
(node:17781) UnhandledPromiseRejectionWarning: Error: Failed to launch chrome!
[0719/113011.202956:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.


TROUBLESHOOTING: https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md

    at onClose (/home/zhenlinhuo/spider/node_modules/puppeteer/lib/Launcher.js:340:14)
    at Interface.helper.addEventListener (/home/zhenlinhuo/spider/node_modules/puppeteer/lib/Launcher.js:329:50)
    at Interface.emit (events.js:187:15)
    at Interface.close (readline.js:379:8)
    at Socket.onend (readline.js:157:10)
    at Socket.emit (events.js:187:15)
    at endReadableNT (_stream_readable.js:1081:12)
    at process._tickCallback (internal/process/next_tick.js:63:19)
(node:17781) UnhandledPromiseRejectionWarning: Unhandled promise rejection. This error originated either by throwing inside of an async function without a catch block, or by rejecting a promise which was not handled with .catch(). (rejection id: 1)
(node:17781) [DEP0018] DeprecationWarning: Unhandled promise rejections are deprecated. In the future, promise rejections that are not handled will terminate the Node.js process with a non-zero exit code.
```  
这个问题，只需要配置chromium启动项  
```javascript
browser = await puppeteer.launch({
        args: ['--no-sandbox'],
        headless: true

    });

```