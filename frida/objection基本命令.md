# 注入app  
```bash
objection -g packageName explore --startup-command 'android hooking watch xxx'  #spawn方式注入
objection -g packageName explore # 普通注入

```

# 查看具体某类的所有方法  
```bash
android hooking watch  class com.fxicrazy.sjml.ui.welcome.WelcomeActivit
```

# 直接生成hook代码  
```bash
android hooking generate simple com.google.android.apps.chrome.compositor.Invalidator

```
# 获取当前活动  

```bash
android hooking get current_activity
```

# 文献  
1. https://blog.csdn.net/liutianheng654/article/details/105429025?utm_medium=distribute.pc_relevant.none-task-blog-baidulandingword-1&spm=1001.2101.3001.4242
2. https://book.hacktricks.xyz/mobile-apps-pentesting/android-app-pentesting/frida-tutorial/objection-tutorial  
