# linux









# linux base

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

  







# shell





















