# resource-manager

- Reference - org

  [scoop](https://scoop.sh/), 

- Reference - blog

  [scoop inntroduction](https://www.mobaijun.com/posts/908521329.html), [scoop introduction](https://blog.bling.moe/post/11/), [scoop introduction](https://p3terx.com/archives/scoop-the-best-windows-package-manager.html), 



- operating system

  scoop: 

  yum: 

  apt: 

- programming language

  cargo: 

  maven: 

  gradle: 

  pip, conda: 

  gomod: 





## scoop

- Install Scoop

  ```powershell
  # 设置用户安装路径
  $env:SCOOP='D:\devenv\scoop'
  [Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')
  # 设置全局安装路径 (admin)
  $env:SCOOP_GLOBAL='D:\devenv\scoop_global'
  [Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')
  
  # check: view current user environment variables
  Get-ChildItem env:
  Get-ChildItem env: | Where-Object { $_.Name -eq 'SCOOP' }
  # check: view global environment variables
  [Environment]::GetEnvironmentVariable('SCOOP', 'User')
  [Environment]::GetEnvironmentVariable('SCOOP_GLOBAL', 'Machine')
  
  # 设置允许 PowerShell 执行本地脚本
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  # install Scoop (no admin)
  iwr -useb get.scoop.sh | iex
  # checl
  scoop -v
  
  
  # mirror
  iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex
  scoop config SCOOP_REPO 'https://gitee.com/glsnames/scoop-installer'
  scoop update
  
  # scoop install <app_name>
  scoop install sudo
  scoop install usql
  
  ```

- common commands

  `scoop search <app>` - 搜索软件

  `scoop install <app>` - 安装软件

  `scoop info <app>` - 查看软件详细信息

  `scoop list` - 查看已安装软件

  `scoop uninstall <app>` - 卸载软件，`-p`删除配置文件。

  `scoop update` - 更新 scoop 本体和软件列表

  `scoop update <app>` - 更新指定软件

  `scoop update *` - 更新所有已安装的软件

  `scoop checkup` - 检查 scoop 的问题并给出解决问题的建议

  `scoop help` - 查看命令列表

  `scoop help <command>` - 查看命令帮助说明

  ```powershell
  
  ```

  







## win11 (yingzhu)

- first

  chrome, pan.baidu, typora, todesk

  scoop, git, 





- Idea

  win11 as the host, only **the database connection tool** (`usql`) is installed, not the database server (such as `mysql server`). 





### /e

- /e/book (pan.baidu synchronization)

- /e/course (pan.baidu synchronization)

- /e/saturday (tv)

- /e/temporary

  



### /d/code2

- dir (json yaml?)

- /d/code2/

  /d/code2/hello-world 

  /d/code2/java-code 

  - (`algorithm-project`, `bigdata`, `movie-recommendations`, `offline-dw-ecommerce`; )
  - (`campus-intelligent-training-system`; )
  - (`springboot-init`, `user-center`, `gonna-oj`, `question-well`; )

  /d/code2/go-code 

  - (`gin-vue-blog2`; )

  /d/code2/rust-code 

  - (`reservation`; )

  /d/code2/python-code 

  - (`artificial-intelligence`; `spider-project`; `web-learning-python`; )
  - (`automatic-drive`; )

  /d/code2/typora-node 

  - (`english-learning`; )

  /d/code2/temporary (...)

  ```bash
  # english、article
  mkdir -p /d/code2/typora-note/  
  git clone https://github.com/Time1043/english-learning.git
  
  mkdir -p /d/code2/go-code/ 
  git clone https://github.com/Time1043/gin-vue-blog2.git
  
  mkdir -p /d/code2/java-code/ 
  git clone https://github.com/Time1043/user-center.git
  git clone https://github.com/Time1043/oj-system.git
  git clone https://github.com/Time1043/big-data.git
  git clone https://github.com/Time1043/algorithm-project.git
  
  mkdir -p /d/code2/python-code/
  git clone https://github.com/Time1043/web-learning-python.git
  git clone https://github.com/Time1043/spider-project.git
  
  mkdir -p /d/code2/rust-code/ 
  
  
  ```

  



### /d/code2

- `/d/soft/` (software)

  /d/soft/social (`QQ`, `weChat`)

  /d/soft/pan (`baidu`, quark, feishu)

  /d/soft/write (`Typora`, draw.io, Koodo, `Foxit PhantomPDF`)

  /d/soft/translate (`wangyi`, baidu, Xtranslator, `GoogleTranslateIpCheck`)

  /d/soft/player (`PotPlayer`, `bandicam`)

  /d/soft/tool (`7z`, `Everything`, `geek`, `Snipaste`, `Reduce Memory`, DeskPins, utool, SpaceSniffer)

  /d/soft/help (`Clash`, v2, Win)

  



### /d/devenv/

- `/d/DockerContainers` 

  (`PostgreSQL`, `MongoDB`, `Redis`, `MySQL`, `SQLServer`; DM)

- `/d/devenv/` (development environment)

  /d/devenv/scoop; /d/devenv/scoop_global

  /d/devenv/git

  /d/devenv/apache-maven-3.8.1; /d/devenv/gradle; /d/devenv/miniconda3

  /d/devenv/scala; /d/devenv/java; /d/devenv/go; /d/devenv/nvm, /d/devenv/nodejs; /d/devenv/texlive

  /d/devenv/bigdat (`hadoop-3.1.0`, `prettyZoo`)

  /d/devenv/help (`protoc-25.0-win64`, `chromedriver-win64`)

  /d/devenv/bigdata-package (...)

- `/d/ide` (integrated development environment)

  /d/ide/vm (`VMware`, `Virtual Machines`, `xshell`, `finalshell`)

  /d/ide/Microsoft (`Visual Studio`, `VS Code`)

  /d/ide/sample (`Sublime`, `postman`)

  /d/ide/JetBrains (`IDEA`, `PyCharm`, `WebStorm`, GoLand)

  /d/ide/mobile (`wechatdev`; Android, Huawei)

  ```bash
  mkdir -p /d/DockerContainers/ && cd /d/DockerContainers/
  mkdir PostgreSQL MongoDB Redis MySQL SQLServer
  
  
  
  
  mkdir -p /d/software/Microsoft  # Microsoft Visual Studio、Microsoft VS Code
  mkdir -p /d/software/JetBrains/  # IntelliJ IDEA 2023.3.2、PyCharm 2023.2.6、GoLand 2023.3、WebStorm 2023.2.6
  mkdir -p /d/software/Android/  # Android Studio、Sdk
  mkdir -p /d/software/Huawei/  # DevEco Studio、Sdk、nodejs、ohpm
  mkdir -p /d/software/sample/  # Sublime Text、postman
  
  mkdir -p /d/SFforLinux  # VMware、xshell7、finalshell
  
  
  https://code.visualstudio.com/
  https://www.jetbrains.com/idea/download/other.html
  https://www.jetbrains.com/webstorm/download/other.html
  https://www.jetbrains.com/pycharm/download/other.html
  https://www.jetbrains.com/go/download/other.html
  
  ```

- 1

  ```yaml
  directories:
    - name: /d/software/Microsoft
      subdirectories:
        - name: Microsoft Visual Studio
        - name: Microsoft VS Code
  
    - name: /d/software/JetBrains
      subdirectories:
        - name: IntelliJ IDEA 2023.3.2
        - name: PyCharm 2023.2.6
        - name: GoLand 2023.3
        - name: WebStorm 2023.2.6
  
    - name: /d/software/Android
      subdirectories:
        - name: Android Studio
        - name: Sdk
  
    - name: /d/software/Huawei
      subdirectories:
        - name: DevEco Studio
        - name: Sdk
        - name: nodejs
        - name: ohpm
  
    - name: /d/software/sample
      subdirectories:
        - name: Sublime Text
        - name: postman
  
  ```

  



### git 

- git 集成到 terminal 中

- git 支持扩展命令

  tree, [make](https://sourceforge.net/projects/ezwinports/files/),  









### Docker





### vscode









### Maven (Java, Scala)

#### Maven

- Download and extract [apache-maven-3.6.1.rar](https://maven.apache.org/download.cgi)

- Configuring environment variables

  Create a system environment variable: `MAVEN_HOME` - `D:\devenv\apache-maven-3.6.1`

  Configuring the system PATH: `%MAVEN_HOME%\bin`

  ```bash
  mvn -verison
  
  ```

- Configuring repository

  "D:\devenv\apache-maven-3.8.8\conf\settings.xml"

  local repository (default: `C:\Users\huangyingzhu\.m2\repository` -> Custom) 

  ```xml
    <localRepository>D:\systemEnvironment\apache-maven-3.8.8\mvn_resp</localRepository>
  ```

  IDEA：settings -> maven -> maven home path, user settings file

- Configuring repository ali mirror (no need)

  ```xml
    
    <mirrors>
      <!-- mirror
       | Specifies a repository mirror site to use instead of a given repository. The repository that
       | this mirror serves has an ID that matches the mirrorOf element of this mirror. IDs are used
       | for inheritance and direct lookup purposes, and must be unique across the set of mirrors.
       |
      <mirror>
        <id>mirrorId</id>
        <mirrorOf>repositoryId</mirrorOf>
        <name>Human Readable Name for this Mirror.</name>
        <url>http://my.repository.com/repo/path</url>
      </mirror>
       -->
      <mirror>
        <id>maven-default-http-blocker</id>
        <mirrorOf>external:http:*</mirrorOf>
        <name>Pseudo repository to mirror external repositories initially using HTTP.</name>
        <url>http://0.0.0.0/</url>
        <blocked>true</blocked>
      </mirror>
    </mirrors>
  
  ```

  



#### Java

- Three different ways

  [oracle](https://www.oracle.com/java/technologies/downloads/#java8), IDEA, scoop

- Configuring environment variables

  Create a system environment variable: `JAVA_HOME` - `D:\DElang\Java\jdk1.8.0_271`

  Configuring the system PATH: `%JAVA_HOME%\bin`、`%JAVA_HOME%\jre\bin`

  ```bash
  java
  javac
  
  ```

  



#### Scala













### miniconda (python)

#### miniconda









#### pip

- pip venv

  [pip org](https://pypi.org/)



- pip mirror

  ```bash
  pip config --global set global.index-url http://pypi.douban.com/simple 
  pip config --global set install.trusted-host pypi.douban.com
  
  ```

- common command

  ```bash
  pip install package_name  # 安装包
  pip install --upgrade package_name  # 升级包  pip install -U package_name
  pip uninstall package_name  # 卸载包
  pip –help  # 帮助手册
  
  pip show --files package_name  # 查看某个已安装包
  pip list  # 查看该环境下已安装的包
  pip list --outdated  # 检查哪些包需要更新  pip list -o
  
  pip freeze > requirements.txt  # 查看已经安装的包及版本信息 重定向
  pip install -r requirements.txt  # 根据虚拟环境清单安装指定包
  
  ```

  



#### conda

- conda env

  [tsinghua mirror](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)、[ali mirror](https://developer.aliyun.com/mirror/anaconda)



- conda mirror

  ```bash
  # 创建文件.condarc
  conda config --set show_channel_urls yes 
  
  
  # 复制到文件中  清华镜像
  channels:
    - defaults
  show_channel_urls: true
  default_channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
  custom_channels:
    conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  
  # 或 北外镜像
  channels:
    - defaults
  show_channel_urls: true
  default_channels:
    - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
    - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
    - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
  custom_channels:
    conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
    msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud
    bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud
    menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud
    pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
    pytorch-lts: https://mirrors.bfsu.edu.cn/anaconda/cloud
    simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud
  
  # 或 阿里镜像
  channels:
    - defaults
  show_channel_urls: true
  default_channels:
    - http://mirrors.aliyun.com/anaconda/pkgs/main
    - http://mirrors.aliyun.com/anaconda/pkgs/r
    - http://mirrors.aliyun.com/anaconda/pkgs/msys2
  custom_channels:
    conda-forge: http://mirrors.aliyun.com/anaconda/cloud
    msys2: http://mirrors.aliyun.com/anaconda/cloud
    bioconda: http://mirrors.aliyun.com/anaconda/cloud
    menpo: http://mirrors.aliyun.com/anaconda/cloud
    pytorch: http://mirrors.aliyun.com/anaconda/cloud
    simpleitk: http://mirrors.aliyun.com/anaconda/cloud
  
  
  # 清除索引缓存
  conda clean -i
  
  ```

- demo: torch

  ```bash
  # 如果需要pytorch 还需要添加pytorch的镜像
  conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/pytorch/
  
  # 换回conda的默认源 直接删除channels即可
  conda config --remove-key channels
  
  ```

- common command

  ```bash
  conda info -e  # 查看虚拟环境列表
  conda create -n testPY37 python=3.7  # 创建虚拟环境
  conda info -e
  conda activate testPY37  # 激活虚拟环境
  
  conda install tensorflow=2.3 cudatoolkit=10.1 cudnn  # 在虚拟环境下装包
  conda list  # 在虚拟环境下查看装包情况
  conda deactivate  # 退出虚拟环境
  conda remove -n testPY37 --all  # 删除该虚拟环境
  conda info -e
  
  ```

  



- jupyter

  创建并激活conda环境

  ```bash
  conda info -e
  conda create -n testPY37 python=3.7
  conda info -e
  conda activate testPY37
  
  ```

  导包ipykernel后在jupyter写内核

  ```bash
  conda install ipykernel  
  python -m ipykernel install --user --name testPY37 --display-name testPY37 
  
  ```

  打开jupyter

  ```
  jupyter notebook
  conda install -c conda-forge jupyterlab
  
  ```

- Extended implementation

  jupyter自动打开

  jupyter导出pdf

  



- jupyter基础用法

- jupyter魔法命令 

  





### golang

#### go

- scoop 安装 go

  ```bash
  # win scoop
  scoop search go
  scoop install go@1.20.12
  scoop uninstall go
  
  # linux
  tar -C /usr/local -xzf go1.15.5.linux-amd64.tar.gz
  # PATH
  
  
  go env
  go env -w GO111MODULE=on
  go env -w GOPROXY=https://goproxy.cn,direct
  
  go mod init helloworld  # go.mod
  
  
  go help module-get
  go help gopath-get
  
  go get golang.org/x/text@latest  # 拉取最新的版本(优先择取 tag)
  go get golang.org/x/text@master  # 拉取 master 分支的最新 commit
  go get golang.org/x/text@v0.3.2  # 拉取 tag 为 v0.3.2 的 commit
  go get golang.org/x/text@342b2e  # 拉取 hash 为 342b231 的 commit
  
  go get -u  # 更新现有的依赖
  go mod download  # 下载 go.mod 文件中指明的所有依赖
  go mod tidy  # 整理现有的依赖
  go mod graph  # 查看现有的依赖结构
  
  go mod edit  # 编辑 go.mod 文件
  go mod vendor  # 导出现有的所有依赖 (淡化)
  go mod verify  # 校验一个模块是否被篡改过
  
  ```

  





### nodejs (nvm fnm)

#### nodejs version management

- solution

  [nvm (Node Version Manager)](https://github.com/nvm-sh/nvm): shell

  [fnm (Fast Node Manager)](https://github.com/Schniz/fnm): Rust



- nvm 

  ```bash
  # Have been installed
  nvm list 
  nvm list installed 
  # downloadable
  nvm list available 
  
  ```
  
- fnm

  ```bash
  
  ```

  



#### nodejs

- Reference

  [nodejs18.19 download package](https://nodejs.org/download/release/v18.19.1/), [Node.js blog](https://blog.csdn.net/WHF__/article/details/129362462)



- Config

  新建两个目录：`D:\systemEnvironment\nodejs\node_cache`, `D:\systemEnvironment\nodejs\node_global`

  新建系统环境变量：`NODE_PATH`, `D:\systemEnvironment\nodejs\node_global\node_modules`

  ```bash
  node -v  # v18.19.0
  npm -v  # 10.2.3
  
  mkdir 
  
  # cmd管理员
  npm config set prefix "D:\systemEnvironment\nodejs\node_global"
  npm config set cache "D:\systemEnvironment\nodejs\node_cache"
  ```

- 国内镜像

  ```bash
  npm config get registry  # 查看镜像
  npm config set registry http://registry.npmjs.org/
  # npm config set registry https://registry.npm.taobao.org/  # 已弃用
  
  ```

- demo

  ts

  ```bash
  npm install -g typescript  # -g 将TypeScript安装为全局命令 以便你可以在命令行的任何位置使用tsc命令
  tsc --version
  ```

  http-server

  ```bash
  npm install -g http-server
  http-server  # 启动命令
  ```

  





















































