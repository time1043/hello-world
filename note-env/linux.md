# linux

- Reference

  [dunwu/linux-tutorial](https://github.com/dunwu/linux-tutorial), 
  
- Reference-course

  [linux (heima22)](https://www.bilibili.com/video/BV1n84y1i7td/), [Ubuntu (atguigu24)](https://www.bilibili.com/video/BV1JF4m1A7mN/), [Debian](https://www.bilibili.com/video/BV1YN4y1F7Kx/?)









# linux (heima22)

## 基本概念







## 环境搭建

### vmware下的centos

- vmware的安装

- 检查虚拟机网卡

  ```bash
  # 或 win R
  ncpa.cpl
  
  # VMnet1 VMnet8
  ```

- cenos7(linux系统)

  [cenos7.iso](https://vault.centos.org/7.6.1810/isos/x86_64/)

- 遇见蓝屏修改设置

  `window虚拟机监控程序平台`、`虚拟机平台`



- FinalShell远程连接

  [FinalShell](http://www.hostbuf.com/downloads/finalshell_install.exe)

  ```bash
  # linux中查看设备配置
  ifconfig  # 192.168.93.101
  
  ```

- 虚拟机快照

  



### WSL下的ubuntu

- 相关配置

  `使用于linux的window子系统`

- 安装ubuntu

  Microsoft Store

- 出现报错，需要更新

- 在window terminal中配置ubuntu

  



## linux基本命令

### 文件系统操作

- 列出目录下的内容、目录切换、目录查看、目录创建：ls cd pwd mkdir



### 用户权限管理





### Vim编辑器





### 本机情况

- 进程查看和关闭：`ps`、`kill`

  操作系统管理运行的程序：注册进程

  ```bash
  ps -ef
  tail
  
  ps -ef | grep tail
  kill -9 41885
  
  ```

- 系统资源占用：`top`

  ```bash
  top
  
  ```

- 磁盘信息监控：`df`、`iostat`

  ```bash
  df -h
  iostat -x
  
  ```

- 网络状态空间：`sar`

  ```bash
  sar -n DEV
  
  ```

  



- 环境变量 (无论在哪里都能执行该程序)

  PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/yingzhu/.local/bin:/home/yingzhu/bin

  ```
  env
  ```

  



- 上传和下载：rz sz

  工具拖拽

  ```
  sudo yum -y install lrzsz
  sz hyz.txt 
  
  ```

- 压缩解压：`tar`、`zip`、`unzip`

  ```bash
  tar -zcvf test.tar.gz hyz.txt test3.txt test4.txt 03-d10.py 
  
  ```

  





### 网络传输

- 检查服务器联通：`ping`

  ```bash
  sudo vim /etc/sysconfig/network-scripts/ifcfg-ens33
  ping baidu.com
  ping -c 3 39.156.66.10
  
  ```

- 下载文件：`wget`

  ```bash
  wget http://archive.apache.org/dist/hadoop/common/-3.3.0/hadoop-3.3.0.tar.gz
  ls
  
  ```

- 发起网络请求：`curl`

  ```bash
  curl cip.cc
  
  ```

  



- 查看端口占用情况：`nmap`、`netstat`

  ```bash
  nmap 192.168.93.101
  netstat -anp | grep 580
  
  ```

  





## 案例

### centos安装mysql5.7









### centos安装mysql8.0





### ubuntu安装mysql5.7



### ubuntu安装mysql8.0







# Ubuntu (atguigu24)





# Debian



















# Summary

## linux base

- linux命令分类

  文件系统、权限管理、硬件信息





- 给普通用户sudo权限

  ```bash
  # 切换至root
  su root
  
  ll /etc/sudoers
  chmod u+w /etc/sudoers
  
  vim /etc/sudoers  # yy p
  
  chmod u-w /etc/sudoers
  ll /etc/sudoers
  
  ```

  




- xshell连接

  ```bash
  yum search ifconfig
  yum install net-tools.x86_64 -y
  
  ```

  



- 包管理器 yum

  ```bash
  # 国内镜像
  curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
  yum -y install wget
  
  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
  wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo  
  
  yum clean all
  yum makecache
  ```

  





- 【场景】查看服务器配置

  ```bash
  free -h  # 查看内存使用情况
  df -h  # 查看磁盘空间使用情况
  uname -a  # 查看操作系统信息
  
  ```

  查看是否安装

  ```bash
  docker --version
  docker info
  ps aux | grep docker
  whereis docker
  
  ```

  





## shell













# enjoy

- 格式化实体服务器 重装系统

  引导服务器从U盘启动：Del、F2、F10 

  使用 [rufus](https://rufus.ie/zh/#google_vignette) 制作 CentOS U盘启动盘











