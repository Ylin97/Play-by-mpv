# 说明   
此脚本依赖于 mpv、python3 和 you-get，使用前先确保您的电脑已安装它们。   

# 获取脚本  
从 github 下载或克隆仓库：[https://github.com/Ylin97/Play-by-mpv.git](https://github.com/Ylin97/Play-by-mpv.git)   
点击仓库右上方**绿色**的 ```Code```，然后选择下载 zip 压缩包或复制仓库地址，进行 ```clone```：   
```  
$ cd ~
$ mkdir Play-by-mpv
$ cd Play-by-mpv
$ git clone https://github.com/Ylin97/Play-by-mpv.git  
```

# 安装依赖  
## 安装 mpv 播放器  
从官网下载：[https://mpv.io/installation/](https://mpv.io/installation/)  
对于 Windows 用户，将下载的 ```.7z``` 压缩包解压到想要放置 mpv 程序的文件夹，然后进入解压得到的 mpv 文件夹里面的 ```installer``` 子文件夹，在里面**以管理员身份运行** ```mpv-install.bat```。  

## 安装 python3 
从 [https://www.python.org/downloads/](https://www.python.org/downloads/) 下载最新的版本，然后按照官方的安装说明进行安装。Windows 用户安装时最好选择 **Customize** 方式，并在里面选择 **为所有用户安装**，同时注意把 ```pip``` 工具装上。   

## 安装 you-get 
Windows用户：
以**管理员身份**打开 ```PowerShell``` 或 ```命令提示符```。  
+ 方式一：按住 Win+X 键在弹出菜单中选择 Windows PowerShell(管理员)   
+ 方式二：依次点击 **桌面左下角Windows图标**，然后找到 **Windows附件--命令提示符**，在命令提示符上右键鼠标，选择 **更多--以管理员身份运行**。  

在 PowerShell 或 命令提示符里面输入：   
```  
pip3 install you-get
```  
然后输入 ```you-get -V```，如果输出了 you-get 的版本信息，则说明安装成功。如果不是以管理员身份运行，you-get 会提示它被当前用户的目录下，例如：  ```C:\Users\Username\AppData\Roaming\Python\Python39\Scripts```，此时先执行 ```pip3 uninstall you-get``` 将 you-get 卸载，然后以管理员身份重新打开 PowerShell 或者 命令提示符，再执行 ```pip3 install you-get```。   

# 用法  
在 Bilibili 或 AcFun 网站复制视频播放页地址，然后进入 Play-by-mpv 目录：  

Window:  
打开 PowerShell 或 命令提示符，执行：  
```   
python .\play_by_mpv.py <url>       # url为复制的视频地址
```  
例如，```python .\play_by_mpv.py # https://www.bilibili.com/bangumi/play/ss38233```

Linux:  
打开终端，执行：  
```  
./play_by_mpv.py <url>              # url为复制的视频地址
```  
例如，```./play_by_mpv # https://www.bilibili.com/bangumi/play/ss38233```    


# 视频地址缓存  
当某次解析播放成功后，其解析得到的视频地址会添加到 Play-by-mpv 目录下的 ```.cache``` 文件里，默认缓存大小为 30 个地址，可以更改同目录下的 ```config.conf``` 文件，将 ```cache_size``` 改为你想要的值。