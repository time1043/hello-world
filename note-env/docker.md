# docker

- 定位

  轻量级的虚拟机

  快速构建build、运行run、传送share应用的工具

  



- 参考

  [黑马博客文章](https://b11et3un53m.feishu.cn/wiki/MWQIw4Zvhil0I5ktPHwcoqZdnec)

- 官网

  [docker 官网](https://www.docker.com/)、[docker hub 镜像仓库](https://hub.docker.com/)、[在线docker环境](https://labs.play-with-docker.com/)、

  [docker官方文档](https://docs.docker.com/engine/install/centos/)、[docker命令文档查询](https://docs.docker.com/engine/reference/commandline/run/)、[docker 中文文档](http://www.dockerinfo.net/docker%E5%AE%89%E8%A3%85-windows)

  



# heima

## 快速入门

- 有无docker

  无docker的部署：手动的linux命令、shell脚本 (项目架构逐渐复杂)

  - 命令太多记不住、步骤太多容易出错、安装包太多不知哪里下

  用docker去部署：简单！！！

  - 一键部署 (k8s 容器编排技术)

  



### 无docker部署

- 部署MySQL centos ([post](https://juejin.cn/post/7110209311824936991) 没用过)

  准备环境：查看系统环境、[下载安装包](https://dev.mysql.com/downloads/mysql/ )

  开始安装：卸载自带的、安装、初始化服务、启动服务、验证

  ```bash
  # 准备环境 卸载
  lsb_release -a  
  yum list installed | grep mariadb && yum list installed | grep mysql
  yum -y remove mariadb-libs.x86_64
  
  # 开始安装
  rpm -ivh mysql-community-common-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-client-plugins-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-libs-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-libs-compat-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-devel-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-client-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-icu-data-files-8.0.29-1.el7.x86_64.rpm
  rpm -ivh mysql-community-server-8.0.29-1.el7.x86_64.rpm
  # mysql-community-devel 安装失败
  yum install openssl-devel -y
  
  # 查看安装完成后的安装包
  rpm -qa | grep mysql
  rpm -qa | grep mariadb
  
  # 初始化MySQL服务
  mysqld --initialize --user=mysql
  grep "password" /var/log/mysqld.log
  # 启动MySQL服务
  service mysqld start
  
  ```

- 部署MySQL ubuntu18 (没用过)

  ```bash
  # 查看mysql的依赖项
  dpkg --list|grep mysql
  # 卸载
  sudo apt-get remove mysql-common
  sudo apt-get autoremove --purge mysql-server-5.7
  dpkg -l|grep ^rc|awk '{print$2}'|sudo xargs dpkg -P
  
  # 下载安装
  wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
  sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb
  
  ```

  



### 安装docker

- [centos7 docker安装](https://docs.docker.com/engine/install/centos/) (成功)

  ```bash
  su root
  
  # 卸载旧版
  yum remove docker \
      docker-client \
      docker-client-latest \
      docker-common \
      docker-latest \
      docker-latest-logrotate \
      docker-logrotate \
      docker-engine
      
  # 配置Docker的yum库
  yum install -y yum-utils
  yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
  # 安装Docker
  yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  
  # 启动
  systemctl start docker
  systemctl stop docker
  systemctl restart docker
  systemctl enable docker
  # 校验
  docker run hello-world
  docker ps
  
  ```

- 配置国内镜像：[aliyun docker 镜像加速](https://cr.console.aliyun.com/cn-heyuan/instances/mirrors)

  ```bash
  sudo mkdir -p /etc/docker
  sudo tee /etc/docker/daemon.json <<-'EOF'
  {
    "registry-mirrors": ["https://xxxxxxxx.mirror.aliyuncs.com"]
  }
  EOF
  sudo systemctl daemon-reload
  sudo systemctl restart docker
  ```
  
- [ubuntu18 docker 安装](https://docs.docker.com/engine/install/ubuntu/)

  ```bash
  
  
  ```
  
  



### 用docker部署

- [部署MySQL docker](https://hub.docker.com/_/mysql) 

  ```bash
  docker run -d \
    --name mysql \
    -p 3306:3306 \
    -e TZ=Asia/Shanghai \
    -e MYSQL_ROOT_PASSWORD=123456 \
    mysql
    
  docker exec -it 231f0da2d3ac bash
  mysql -uroot -p123456
  
  ```

- 命令解读

  `docker run -d` ：**创建**并**运行**一个容器，`-d`则是让容器以**后台进程**运行
  
  `--name mysql ` : 给容器起名字mysql (容器名字唯一)
  
  `-p 宿主机端口:容器内端口`: 设置端口映射 (宿主机端口可任意指定 尽量与容器内一致)
  
  `-e KEY=VALUE` : 配置容器内进程运行时参数 (设置时区 设置MySQL默认密码)
  
  `REPOSITORY:TAG` : Docker会根据这个名字搜索并下载镜像 (不指定版本号默认latest)
  
  



## docker基础

### 基本概念

- [基本概念](https://docs.docker.com/guides/docker-concepts/the-basics/what-is-a-container/)

  images：安装包(包含依赖环境 隔离的)

  containers：镜像的实例

  repository：存放很多镜像

  ![Snipaste_2024-01-11_21-20-26](res/Snipaste_2024-01-11_21-20-26.png)

- 延展概念

  Dockerfile：镜像的清单

  DockerCompose：容器编排

  volumes：数据挂载





### 常见命令

- 常用命令

  ![Snipaste_2023-10-27_22-06-28](res/Snipaste_2023-10-27_22-06-28.png)

- 镜像操作：

  `docker pull` (从仓库拉取镜像)、`docker images` (查看本地所有镜像)、`docker rmi` (删除本地指定镜像)、

  `docker build` (从dockerfile构建镜像)、`docker save` (镜像文件本地保存)、`docker load` (镜像文件本地加载)、`docker push` (上传镜像到仓库中)、

- 容器操作：

  `docker run` (由镜像创建并运行容器)、`docker stop` (停止容器的运行)、`docker start` (恢复容器的运行)、`docker restart` (重启容器)

  `docker ps` (查看容器列表)、`docker rm` (删除指定的容器)、

  `docker exec` (进入到容器内部)、`docker logs` (查看容器运行日志进行排错)、`docker inspect` (查看容器详细信息)

- 数据卷命令：

  `docker volume create` (创建数据卷 不用操作)、`docker volume ls` (查看所有数据卷)、`docker volume rm` (删除指定数据卷)、

  `docker volume prune` (清除未被引用的数据卷)、`docker volume inspect` (查看某个数据卷的详情)、

  (容器与数据卷的挂载要在创建容器时配置，对于已创建容器，不能设置数据卷。而且创建容器的过程中，数据卷会自动创建)

- 网络命令：

  `docker network create` (创建一个网络)、`docker network ls` (查看所有网络)、`docker network rm ` (删除指定网络)、
  
  `docker network prune` (清除未使用的网络)、`docker network inspect` (查看网络详细信息)、
  
  `docker network connect` (使指定容器连接加入某网络)、`docker network disconnect` (使指定容器连接离开某网络)
  
- dockerCompose命令：

  



- 部署mysql (重做)

  ```bash
  docker pull mysql:8
  docker images
  
  docker run -d \
    --name mysql \
    -p 3306:3306 \
    -e TZ=Asia/Shanghai \
    -e MYSQL_ROOT_PASSWORD=123456 \
    mysql:8
    
  docker ps
  docker logs mysql
  
  docker exec -it mysql bash
  mysql -uroot -p123456  # it is inside the container
  mysql -h 192.168.64.138 -u root -p123456  # remote connection for win
  
  docker stop mysql
  
  ```

- [部署nginx](https://hub.docker.com/_/nginx)

  镜像操作

  ```bash
  docker pull nginx
  docker images 
  
  
  # save the image as a compressed file
  docker save --help  # docker save [OPTIONS -o] IMAGE [IMAGE...]
  docker save -o mynginx.tar nginx:latest
  
  # delete the image
  docker rmi nginx
  
  # load the image as a compressed file
  docker load --help  # docker load [OPTIONS -i -q]
  docker load -i mynginx.tar 
  
  ```

  容器操作

  ```bash
  docker run -d --name nginx -p 80:80 nginx
  docker ps
  docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}"
  # http://192.168.64.138/
  
  docker stop nginx
  docker start nginx
  docker ps 
  
  docker logs -f nginx  # -f 持续输出
  docker inspect nginx
  docker exec -it nginx bash 
  
  docker rm nginx
  docker rm -f nginx  # 发现无法删除，因为容器运行中，强制删除容器
  
  ```

  



- 自定义命令 (命令的别名)

  ```bash
  vim /root/.bashrc 
  
  # append
  alias dps='docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}"'
  alias dis='docker images
  
  source /root/.bashrc
  
  ```

  



### 数据卷挂载 volumes

- 问题

  容器内修改文件困难、容器内的数据持久化

- 解决方案

  数据卷挂载：只写名称

  本地目录挂载：带斜杆(相对路径 绝对路径)

  ![Snipaste_2023-10-28_09-17-40](res/Snipaste_2023-10-28_09-17-40.png)

  



- 安装nginx (数据卷挂载)

  ```bash
  docker run -d \
    --name nginx \
    -p 80:80 \
    -v html:/usr/share/nginx/html \
    nginx
  			
  docker volume ls
  docker volume inspect html 
  
  # verify
  ll /var/lib/docker/volumes/html/_data
  cd /var/lib/docker/volumes/html/_data
  vi index.html
  
  # verify
  docker exec -it nginx bash
  cd /usr/share/nginx/html/ 
  
  ```

  



- [安装mysql (数据卷挂载 不匿名)](https://hub.docker.com/_/mysql)

  数据目录(Where to Store Data)：`-v /my/own/datadir:/var/lib/mysql`

  配置文件(Using a custom MySQL configuration file)：`-v /my/custom:/etc/mysql/conf.d`

  初始化脚本(Initializing a fresh instance)：`/docker-entrypoint-initdb.d`

  ```bash
  mkdir -p /opt/data/mysql/data /opt/data/mysql/conf /opt/data/mysql/init  # rz -E
  
  docker run -d \
    --name mysql \
    -p 3306:3306 \
    -e TZ=Asia/Shanghai \
    -e MYSQL_ROOT_PASSWORD=123456 \
    -v /opt/data/mysql/data:/var/lib/mysql \
    -v /opt/data/mysql/conf:/etc/mysql/conf.d \
    -v /opt/data/mysql/init:/docker-entrypoint-initdb.d \
    mysql:8
    
  ```

  



### 自定义镜像 Dockerfile

- 对比

  原生配置：linux环境、安装配置JDK、上传Jar包、运行jar包

  打包镜像：Linux基础环境、安装配置JDK、拷贝jar包、配置启动脚本

- 镜像的结构

  `BaseImage`：Linux基础环境

  `Layer`：JDK、Jar

  `Entrypoint`：启动脚本

  ![Snipaste_2024-01-14_11-47-41](res/Snipaste_2024-01-14_11-47-41.png)

- [DockerFile语法](https://docs.docker.com/reference/dockerfile/) (描述镜像的结构)

  主要
  
  `fromcentos:6`  指定基础镜像
  
  `env key value`  设置环境变量
  
  `copy ./xx.jar /tmp/app.jar`  拷贝本地文件到镜像指定目录
  
  `run yum install gcc`  在镜像内部执行shell命令
  
  `expose 8080`  声明容器运行时的监听端口 (只是描述给镜像使用者看的)
  
  `entrypoint java -jar xx.jar`  配置容器启动时执行的命令，不可被 docker run 覆盖
  
  其他
  
  `maintainer your name <youremail@example.com>`  指定镜像的作者信息
  
  `cmd ["nginx", "-g", "daemon off;"]`  指定容器启动时执行的命令
  
  `workdir /app`  设置工作目录
  
  `volume /data`  创建挂载点，用于持久化数据
  
  `user nobody`  设置执行 run、cmd 和 entrypoint 指令时的用户名或 UID
  
  



- 基于Ubuntu镜像来构建一个Java应用

  ```dockerfile
  # 指定基础镜像
  FROM ubuntu:16.04
  
  # 配置环境变量，JDK的安装目录、容器内时区
  ENV JAVA_DIR=/usr/local
  ENV TZ=Asia/Shanghai
  # 拷贝jdk和java项目的包
  COPY ./jdk8.tar.gz $JAVA_DIR/
  COPY ./docker-demo.jar /tmp/app.jar  # change 
  # 设定时区
  RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
  # 安装JDK
  RUN cd $JAVA_DIR \
   && tar -xf ./jdk8.tar.gz \
   && mv ./jdk1.8.0_144 ./java8
  # 配置环境变量
  ENV JAVA_HOME=$JAVA_DIR/java8
  ENV PATH=$PATH:$JAVA_HOME/bin
  # 指定项目监听的端口
  EXPOSE 8080
  
  # 入口，java项目的启动命令
  ENTRYPOINT ["java", "-jar", "/app.jar"]
  
  ```

- 基础的系统加JDK环境 (别人轮子)

  ```dockerfile
  # 基础镜像
  FROM openjdk:11.0-jre-buster
  
  # 设定时区	
  ENV TZ=Asia/Shanghai
  RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
  # 拷贝jar包
  COPY docker-demo.jar /app.jar  # change 
  
  # 入口
  ENTRYPOINT ["java", "-jar", "/app.jar"]
  
  ```
  
  



- 由dockerfile创建image

  ```bash
  mkdir -p /opt/code
  chmod -R 777 /opt/code
  
  cd /opt/code/demo
  docker build -t docker-demo:0.1 .
  
  docker run -d \
    --name docker-demo-container \
    -p 8080:8080 \
    docker-demo:0.1
    
  dps
  docker logs docker-demo-container 
  # http://192.168.64.138:8080/hello/count
  
  ```

  



### 容器网络 network

- 问题

  Java项目需要访问其它各种中间件 (如MySQL Redis等) -> 容器之间互相访问
  
  容器的网络IP是虚拟的IP，其值并不固定与某一个容器绑定，若在开发写死某IP，在部署时很可能容器的IP会变化，连接会失败
  
- docker的网络设计

  所有容器默认以bridge连接到docker的一个虚拟网桥上

  ![](res/Snipaste_2024-04-22_11-07-17.png)

  ```bash
  # Check docker's default network configuration
  docker inspect mysql
  docker inspect --format='{{range .NetworkSettings.Networks}}{{println .IPAddress}}{{end}}' mysql  # 172.17.0.3
  
  docker exec -it docker-demo-container bash 
  ping 172.17.0.2
  
  
  # Customize docker's network configuration
  ip addr
  
  ```

- [docker 自定义网络](https://docs.docker.com/engine/reference/commandline/network/)

  自定义网桥、容器加入新网桥 (互联访问 且可通过**容器名**访问)

  ```bash
  # create network
  docker network --help
  docker network ls
  docker network create nttime1043
  ip addr
  
  
  # The container is connected to the network when it exists
  docker network connect --help
  docker network connect nttime1043 docker-demo-container 
  docker network connect nttime1043 mysql 
  
  docker inspect mysql
  
  
  # The container is connected to the network when it is created
  docker run -d \
    --name docker-demo-container \
    -p 8080:8080 \
    --network nttime1043 \
    docker-demo:0.1
  
  docker run -d \
    --name mysql \
    -p 3306:3306 \
    -e TZ=Asia/Shanghai \
    -e MYSQL_ROOT_PASSWORD=123456 \
    -v /opt/data/mysql/data:/var/lib/mysql \
    -v /opt/data/mysql/conf:/etc/mysql/conf.d \
    -v /opt/data/mysql/init:/docker-entrypoint-initdb.d \
    --network nttime1043 \
    mysql:8
  
  docker exec -it docker-demo-container bash
  ping mysql
  
  ```

  



## 项目部署

### 手动部署

- 部署java后端

  ```bash
  # The project is packaged as a jar
  
  mkdir /opt/code/hmall-min/
  # cp /opt/code/hmall/hm-common/target/hm-common-1.0.0.jar /opt/code/hmall-min/hm-common-1.0.0.jar
  cp /opt/code/hmall/hm-service/target/hm-service.jar /opt/code/hmall-min/hm-service.jar
  cp /opt/code/hmall/hm-service/Dockerfile /opt/code/hmall-min/Dockerfile
  cd /opt/code/hmall-min/
  docker build -t hmall:0.1 .
  
  docker run -d \
    --name hmall \
    -p 8080:8080 \
    --network nttime1043 \
    hmall:0.1
  
  docker logs -f hmall 
  # http://192.168.64.138:8080/hi
  # http://192.168.64.138:8080/search/list?pageNo=1&pageSize=5
  
  ```

- 部署前端

  ```bash
  # cp
  
  cd /opt/code/nginx/
  
  docker run -d \
    --name nginx \
    -p 18080:18080 \
    -p 18081:18081 \
    -v /opt/code/nginx/html:/usr/share/nginx/html \
    -v /opt/code/nginx/nginx.conf:/etc/nginx/nginx.conf \
    --network nttime1043 \
    nginx
  
  docker logs -f hmall 
  # http://192.168.64.138:18080/
  
  ```

  



### DockerCompose

- 两种部署方式

  手动部署：操作步骤多、没有体现项目整体性

  DockerCompose：多容器操作 (通过 `docker-compose.yml` [定义一组相关联的应用容器](https://docs.docker.com/compose/compose-file/compose-file-v3/))

  ![](res/Snipaste_2024-04-23_10-51-21.png)

  ![](res/Snipaste_2024-04-23_10-52-53.png)



- 整体部署

  ```bash
  mkdir -p /opt/workspacehyz  # mysql nginx
  cp /opt/code/hmall/hm-service/target/hm-service.jar /opt/workspacehyz/hm-service.jar
  cp /opt/code/hmall/hm-service/Dockerfile /opt/workspacehyz/Dockerfile
  ls  # docker-compose.yml  Dockerfile  hm-service.jar  mysql  nginx
  
  
  
  ```

  DockerCompose.yml

  ```yml
  version: "3.8"
  
  services:
    mysql:
      image: mysql
      container_name: mysql
      ports:
        - "3306:3306"
      environment:
        TZ: Asia/Shanghai
        MYSQL_ROOT_PASSWORD: 123
      volumes:
        - "./mysql/conf:/etc/mysql/conf.d"
        - "./mysql/data:/var/lib/mysql"
        - "./mysql/init:/docker-entrypoint-initdb.d"
      networks:
        - hm-net
    hmall:
      build: 
        context: .
        dockerfile: Dockerfile
      container_name: hmall
      ports:
        - "8080:8080"
      networks:
        - hm-net
      depends_on:
        - mysql
    nginx:
      image: nginx
      container_name: nginx
      ports:
        - "18080:18080"
        - "18081:18081"
      volumes:
        - "./nginx/nginx.conf:/etc/nginx/nginx.conf"
        - "./nginx/html:/usr/share/nginx/html"
      depends_on:
        - hmall
      networks:
        - hm-net
  networks:
    hm-net:
      name: hmall
  ```

  





# geekhour









# 应用方向

## 网站业务开发

### 用java调docker

- 参考

  [Java API 操作Docker浅谈](https://www.cnblogs.com/beyond-tester/p/17896443.html)



- docker服务器对外开放

  ```bash
  systemctl status docker.service  # 获取docker.service的位置
  vim /lib/systemd/system/docker.service
  
  # 替换文件中的ExecStart字段
  ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock
   
  systemctl daemon-reload
  systemctl restart docker
  systemctl status docker.service  # 已经暴露2375端口
  
  ```

- java编程

  DockerClientUtils

  ```java
  package time1043;
  
  import com.github.dockerjava.api.DockerClient;
  import com.github.dockerjava.api.command.CreateContainerResponse;
  import com.github.dockerjava.core.DockerClientBuilder;
  
  public class DockerClientUtils {
      /**
       * 连接Docker服务器
       *
       * @param dockerInstance Docker服务器地址
       * @return DockerClient
       */
      public DockerClient connectDocker(String dockerInstance) {
          DockerClient dockerClient = DockerClientBuilder.getInstance(dockerInstance).build();
          dockerClient.infoCmd().exec();
          return dockerClient;
      }
  
      /**
       * 创建容器
       *
       * @param client        Docker客户端
       * @param containerName 容器名称
       * @param imageName     镜像名称
       * @return CreateContainerResponse
       */
      public CreateContainerResponse createContainers(DockerClient client, String containerName, String imageName) {
  
          CreateContainerResponse container = client.createContainerCmd(imageName)
                  .withName(containerName)
                  .exec();
  
          return container;
  
      }
  
      /**
       * 启动容器
       *
       * @param client      Docker客户端
       * @param containerId 容器ID
       */
      public void startContainer(DockerClient client, String containerId) {
          client.startContainerCmd(containerId).exec();
      }
  
      /**
       * 启动容器
       *
       * @param client      Docker客户端
       * @param containerId 容器ID
       */
      public void stopContainer(DockerClient client, String containerId) {
          client.stopContainerCmd(containerId).exec();
      }
  
      /**
       * 删除容器
       *
       * @param client      Docker客户端
       * @param containerId 容器ID
       */
      public void removeContainer(DockerClient client, String containerId) {
          client.removeContainerCmd(containerId).exec();
      }
  }
  
  ```

  main

  ```java
  package time1043;
  
  import com.github.dockerjava.api.DockerClient;
  import com.github.dockerjava.api.command.CreateContainerResponse;
  
  public class Main {
      public static void main(String[] args) {
          // 创建 DockerClientUtils 实例 来操作 Docker 客户端
          DockerClientUtils dockerClientUtils = new DockerClientUtils();
          // 连接 Docker 服务器
          DockerClient dockerClient = dockerClientUtils.connectDocker("tcp://192.168.64.138:2375");
          System.out.println("The docker server is connected successfully");
  
          // 创建容器
          CreateContainerResponse containers = dockerClientUtils.createContainers(
                  dockerClient, "nginx", "nginx:latest"
          );
          // 启动容器
          dockerClientUtils.startContainer(dockerClient, containers.getId());
          System.out.println("Container started successfully");
  
          try {
              System.out.println("sleep 2 minutes...");
              Thread.sleep(2 * 60 * 1000);
              System.out.println("sleep end.");
          } catch (InterruptedException e) {
              e.printStackTrace();
          }
  
          // 停止容器
          System.out.println("Container stopped successfully");
          dockerClientUtils.stopContainer(dockerClient, containers.getId());
  
          // 删除容器
          System.out.println("Container deleted successfully");
          dockerClientUtils.removeContainer(dockerClient, containers.getId());
  
      }
  }
  ```

  









## 大数据搭建环境

### hadoop集群

- [docker搭建hadoop集群](https://juejin.cn/post/7102339789030064136)





## 自己折腾

### docker里装win

- [把 Windows 装进 Docker 容器里](https://soulteary.com/2024/03/11/install-windows-into-a-docker-container.html)

  ```bash
  docker pull dockurr/windows
  
  docker run -it \
    --rm --name windows \
    -p 8006:8006 \
    --device=/dev/kvm \
    --cap-add NET_ADMIN \ 
    --stop-timeout 120 \
    dockurr/windows
    
  ```

  



















