# linux

- 参考

  [dunwu/linux-tutorial](dunwu/linux-tutorial)







# linux base

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

  





# shell









# enjoy

- 格式化实体服务器 重装系统

  引导服务器从U盘启动：Del、F2、F10 

  使用 [rufus](https://rufus.ie/zh/#google_vignette) 制作 CentOS U盘启动盘











