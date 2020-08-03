# 前言  
在macos的操作系统上，ntfs格式的固态硬盘连接电脑后只有读权限，而没有
写权限，这时候，网上有很多提供了支持写硬盘功能的软件。  

其实，我们可以通过命令的方式让macos系统支持读写操作  

首先，我们需要知道我们移动硬盘的名字，可通过一下名字寻找  

```bash
mount | grep ntfs
```

其次，在硬盘的可进行写操作的位置创建空目录

```bash
cd /Users/huozhenlin/
mkdir mn
```

接着，以可读可写的方式挂载移动硬盘

```bash
sudo mount_ntfs -o rw,nobrowse /dev/disk2s1 /Users/huozhenlin/mn
```

最后，你可以在系统的访达软件中进入你的挂载目录从而找到你的移动硬盘，当然，你也可以通过mv,cp等命令往里面写入文件  

若你想推出移动硬盘，你可以通过系统自带的推出功能，也可以通过命令的方式，如下  

```bash
umount /dev/disk2s1 # 若不成功或者提示硬盘繁忙，可通过最后一条命令直接推出，若提示权限不足，可通过sudo提权
diskutil unmount force /dev/disk2s1 
```

