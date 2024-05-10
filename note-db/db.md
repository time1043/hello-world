# db

- Reference - docs

  [postgresql org](https://www.postgresql.org/), [postgresql docs](https://www.postgresql.org/docs/release/), 
  
  [postgresql-tutorial runoob](https://www.runoob.com/postgresql/postgresql-tutorial.html), 
  
- Reference - github

  [usql](https://github.com/xo/usql)

- Reference - blog

  [Database connection tool (usql, mycli...)](https://www.cnblogs.com/-wenli/p/11239042.html), [usql](https://www.hi-linux.com/posts/38677.html), 
  
  [How to Install and Run PostgreSQL Using Docker](https://www.percona.com/blog/installing-postgresql-using-docker/), 
  
  [Postgresql sql](http://forum.selectdb.com/t/topic/385), 
  
- Reference - course

  [PostgreSQL for everyone (bilibili)](https://www.bilibili.com/video/BV1tj421U7GK/), 
  
  python for everyone、django for everyone、web applications for everyone
  
  



## basic conception

### Traversal of the database (myself)

- Traversal of the database

  sql: Structured Query Language

- business-oriented (*Relational Database*)

  `PostgreSQL`: 

  `SQLite`: 

  `MySQL`: 

  `MariahDB`: 

  `Oracle`: 

  `SQL Server`: 

- other

  `MongoDB`: document-oriented

  `ElasticSearch`: search engine

- other - Column storage

  `HBase`: 

  `Clickhouse`: 

  `Doris`: 

- other 

  `Redis`: high-speed cache, k-v

- other - graph

  ``: 

  



### Traversal of the database (yuanzi)

- 数据库：储存数据、操作修改数据、检索查找数据

- 两类数据库

  *Relational Database*：采用了 关系模型(sql) 来组织数据的数据库、行列表

  - 常见有：PostgreSQL、MySQL、MariahDB(副本)、Oracle(付费)、SQLite(轻量 嵌入式)、SQL Server

  *non Relational Database*：

  - 常见有：redis、mongoDB、Cassandra、HBase

- PostgreSQL和MySQL的对比

  `MySQL`：国内使用最多；只支持部分sql标准、不那么严谨、老油条风格

  `PostgreSQL`：欧美使用多、社区活跃；支持所有sql标准、学院派的严谨、完全开源BSD/MIT、源码很清晰



- web业务 CRUD

  create、read、update、delete

  index、join、foreign key





### Traversal of the database (shan)

- 关系型数据库

  定义：就是按关系存储数据的，可以建立一对一，一对多，多对多的关系。再通俗一点就是由行和列组成的表。

  产品：`mysql`、`postgreSQL`

  场景：

  观看视频、发布视频的都是这个视频网站的用户

  关于用户的信息可能存在一张用户表中，用户id，用户昵称，个人信息介绍等

  视频可能被存储在视频表中，这个表中有视频id，视频标题，简介，以及视频ur等信息

  用户和视频应该是一对多的关系，怎么建立这种关系呢，可能是视频表中有一个用户id，来将视频和用户连接起来



- 非关系型数据库

  数据是以非表格的方式被组织起来。也可以说数据是半结构或非结构的。比如刚刚提到的redis，他就是以键值对形式存储的。另外还有列式、文档型和图存储。

- 键值对

  定义：存储格式就是字典，根据key来读取value

  产品：`redis`、`rocksDB`、`Abase`

  场景：这种比较适合不涉及复杂数据业务关系的，大量读写场景。(像我现在就有大量用到kv存储数据库，不过根据业务，支持的数据量、qPS，延迟等要求，我们选择了abase，这是字节开源的数据库)

- 列式存储

  定义：数据是按列存储

  产品：`hbase`、`clickhouse`、`doris`

  场景：大数据量，适合批量对某些列进行聚合计算；列压缩效率高;使用xx社交平台的几亿用户，有用户的个人信息(年龄，性别，地域等)，以及平台上的信息(粉丝量，最近一次登陆时间，最近一周活跃时长)等。然后要对用户进行一次营销活动，比如圈出平台最近10天，在上海地区的年轻人，并且喜欢看二次元的，然后在首页推出一个漫展的广告。

- 图数据库

  定义：存储实体及其关系，实体指的节点，关系就通过实体的边来描述；这样构成一张图，另外顶点和边还用属性来描述其详细信息。

  产品：`Neo4i`、`ByteGraph`

  场景：支持数据量大，比如用于目前的社交网络、知识图谱，数据量能达上亿级别；另外处理很复杂的关系，也不用设计关系表，不用考虑复杂的连表操作;而且数据量大的时候，做多层关系，查询效率也高。比如现在现在要建立视频和用户的关系，可以设计两种类型顶点，分别表示视频和用户;边可以定义用户、视频之间的关系

- 文档型

  定义：以JSON/XML格式进行存储

  产品：`mongoDB`，`Elasticsearch`



## Prepare the environment

### Database connection tool

- Install

  ```bash
  # linux 
  cd /opt/software
  wget https://github.com/xo/usql/releases/download/v0.7.0/usql-0.7.0-linux-amd64.tar.bz2
  tar xjvf usql-0.7.0-linux-amd64.tar.bz2
  sudo mv usql /usr/local/bin
  
  # win scoop
  scoop install usql
  usql --version
  
  ```
  
  



- connect MySQL

  ```bash
  # defult
  usql my://
  # username password
  usql my://user:pass@host/dbname
  # username password port
  usql mysql://user:pass@host:port/dbname
  # socket
  usql /var/run/mysqld/mysqld.sock
  
  
  # Example
  usql my://root:123456@localhost
  create database test;
  use test;
  
  create table if not exists `test`(
    `test_id` int,
    `name` varchar(100) not null
  )engine=InnoDB default charset=utf8;
  
  insert into test (test_id, name) values (1, 'hello');
  select * from test;
  
  
  # Example
  usql my://root:000000@localhost/wordpress -f script.sql
  
  ```

- connect PostgreSQL

  ```bash
  # defult
  usql pg://
  # username password 
  usql pg://user:pass@host/dbname
  # username password port
  usql postgres://user:pass@host:port/dbname
  # socket
  usql /var/run/postgresql
  
  ```

- connect Oracle 

  ```bash
  # defult
  usql or://
  # username password 
  usql or://user:pass@host/sid
  # username password port
  usql oracle://user:pass@host:port/sid
  
  ```

- connect SQL Server

  ```bash
  # defult
  usql ms://
  # username password
  usql ms://user:pass@host/dbname
  # username password port
  usql mssql://user:pass@host:port/dbname
  # socket
  usql ms://user:pass@host/instancename/dbname
  
  ```

  



### Database server (container )

- Install MySQL

  ```bash
  
  ```

- Install PostgreSQL

  ```bash
  
  ```

  











# PostgreSQL (myself)

## Prepare the environment

- docker (server)

  [dockerHub:postgreSQL](https://hub.docker.com/_/postgres), [windocker install postgres](https://www.cnblogs.com/an-shiguang/p/17840671.html)
  
  ```bash
  # win docker 
  docker search postgres 
  docker run -d \
    --name mypostgres \
    -e POSTGRES_DB=database \
    -e TZ=PRC \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=123456 \
    -p 5432:5432 \
    -v D:\\DockerContainers\\PostgreSQL\\pastgresData:/var/lib/postgresql/data \
    postgres:16-alpine3.19
    
  docker exec -it mypostgres bash
  psql -U root -d database
  
  create database hyzdb;  
  \c hyzdb;  
  
  
  # win usql
  usql postgres://root:123456@localhost:5432/database
  
  ```
  
  



# PostgreSQL (yuanzi)

- docker 

  ```bash
  docker exec -it mypostgres bash
  createdb yzzy
  psql yzzy
  
  ```

  



## General sql

- 基础命令

  ```bash
  \h  # 显示sql命令说明
  \?  # 显示pgsql命令说明
  \l  # 数据库列表
  \q  # 退出
  
  \c hyzdb  # 切换数据库
  create database hyzdb;  # 创建数据库
  drop database yzzy;  # 删除数据库
  
  \d  # 查看该数据库下的表情况
  \d user_tb  # 查看该表的情况
  
  ```

  表的创建删除 [PostgreSQLdata type](https://www.postgresql.org/docs/current/datatype.html)、[PostgreSQL 数据类型](http://www.postgres.cn/docs/9.3/datatype.html)

  ```sql
  # 创建表
  create table user_tb2 (
      id bigserial not null primary key,
      name varchar(200) not null,
      gender varchar(7) not null,
      birthday date not null,
      email varchar(250)
  );
  
  # 删除表
  drop table user_tb2;
  
  ```

  表数据

  ```sql
  # 查询数据
  select * from user_tb2;
  
  # 插入数据
  insert into user_tb2 (name, gender, birthday, email) 
  values 
  ('alice', 'female', '1990-05-15', 'alice@example.com'),
  ('bob', 'male', '1985-10-20', 'bob@example.com');
  insert into user_tb2 (name, gender, birthday) values ('charlie', 'male', '1995-03-25');
  
  # 更新数据
  update user_tb2 set id = 10 where id = 1;
  
  # 删除数据 (不推荐硬删除 推荐逻辑删除)
  delete from user_tb2 where id = 2;
  # 逻辑删除 (添加表字段)
  alter table user_tb2 add column removed boolean not null default(false); 
  # 添加主键
  alter table user_tb2 add primary key(id);
  
  ```
  
  mock数据 [mockaroo](https://mockaroo.com/)
  
  ```bash
  docker cp user_tb.sql mypostgres:/hyzdata/user_tb.sql
  docker exec -it mypostgres bash
  psql -U root -d yzzy -f /hyzdata/user_tb.sql
  
  ```
  
  查询语句
  
  ```sql
  # 排序 (order by  asc desc)
  select * from user_tb order by first_name desc;
  # 去重 (distinct)
  select distinct country_of_birth from user_tb 
  order by country_of_birth;
  
  # 条件 (where  and or) 
  select * from user_tb where country_of_birth = 'China' and gender = 'Male';
  
  # 比较 comparison
  select 1 > 2;
  select 4 >= 1;
  select 2 <> 2;  # 不等于
  
  # 翻页 (limit offset)
  from user_tb limit 5 offset 10;
  
  # in between like ilike(大小写不敏感)
  select * from user_tb where country_of_birth in ('China','Sweden');
  select * from user_tb where date_of_birth between '2000-11-11' and '2003-09-09';
  select * from user_tb where first_name like '%ll';
  select * from user_tb where first_name like '__ll';
  
  # 分组 (group by  having)
  select country_of_birth, count(*) from user_tb group by country_of_birth;
  select country_of_birth, count(*) from user_tb group by country_of_birth having count(*) > 10;
  
  # 聚合函数 (min max avg round sum)
  
  ```
  
  join
  
  ```sql
  # 交叉连接 (cross join)
  
  # 内连接 (inner join)
  
  # 外连接 (left outer join  right outer join  full outer join)
  
  ```
  











## Speciality













# PostgreSQL (runoob)

## Basic Operation

- 前置操作

  win usql

  ```bash
  usql postgres://root:123456@localhost:5432/database
  usql postgres://root:123456@localhost:5432/runoobdb
  
  # show databases (\l)
  select datname from pg_database;
  select * from pg_database;
  # create database
  create database runoobdb;
  # use databse (\c runoobdb)
  
  # drop database (dropdb runoobdb;)
  drop database runoobdb;
  
  
  # show table
  select table_name from information_schema.tables where table_schema = 'public';
  
  
  
  ```

  win docker 

  ```bash
  docker exec -it mypostgres bash
  psql -U root -d database
  
  create database runoobdb;  
  \c runoobdb
  
  
  # create table
  create table company(
     ID INT PRIMARY KEY     NOT NULL,
     NAME           TEXT    NOT NULL,
     AGE            INT     NOT NULL,
     ADDRESS        CHAR(50),
     SALARY         REAL
  );
  
  CREATE TABLE DEPARTMENT(
     ID INT PRIMARY KEY      NOT NULL,
     DEPT           CHAR(50) NOT NULL,
     EMP_ID         INT      NOT NULL
  );
  
  \d
  \d company
  
  # drop table 
  drop table department, company;
  
  ```

  

### Data Type





### schema

- schema

  一个表的集合

  包含视图、索引、数据类型、函数和操作符等

- 作用

  模式通常用于组织和隔离数据库对象，防止对象名称冲突

- 优势

  允许多个用户使用一个数据库并且不会互相干扰。

  将数据库对象组织成逻辑组以便更容易管理。

  第三方应用的对象可以放在独立的模式中，这样它们就不会与其他对象的名称发生冲突































# MongoDB (geekhour)

## Basic Conception

- 定位

  分布式文件存储(可扩展 高性能)、文档存储、nosql

- mongoDB和mysql应用场景

  mongDB：实时分析、内容管理、非结构化数据、物联网、移动app

  mysql：数据结构固定、关系型数据库、结构化数据、多表关联查询、传统应用

- mongoDB的特点 (更加灵活 专注业务实现)

  不需要事先创建好数据库和集合

  不需要预先定义好集合中字段的类型和长度、同一个集合中数据也不需要有相同的结构

  ![](res/Snipaste_2024-03-07_07-09-27.png)
  
  



## Prepare the environment

- win安装配置

  [mongoDB官网](https://www.mongodb.com/zh-cn)、[社区版下载](https://www.mongodb.com/try/download/community)、[shell下载](https://www.mongodb.com/try/download/shell)

  图形化GUI工具连接mongoDB：compass (官方)、navicat

  mongoShell连接mongoDB

  vscode插件：`mongodb://localhost:27017`

- 常用语句

  test是mongoDB默认的数据库，是空的数据库，并没有被创建

  只有真正往里面插入数据，数据库才会被创建

  ```
  help  
  
  show dbs  # show databases
  use database  # 切换数据库 数据库不存在也可以
  
  db.集合名称  # 创建集合
  db.users.insertOne({name: "zhou"})  # 在集合中插入一条数据
  db.users.find()  # 查询集合中的数据
  
  db.users.insertOne({name:"zhang", age:18})  # 文档的数据结构可以不同
  db.users.insertMany([{name:"li", age: 20}, {name: "wang", age:40}])  # 插入多条数据
  ```

  












# Redis (geekhour)

## basic conception

- 概念

  Remote dictionary server：开源的、基于**内存**的 数据存储系统

  应用：DB Cache、MQ (DB **IO**开销大)

- 优势

  性能记高

  数据类型丰富，单键/值对最大支持512M大小的数据

  简单易用，支持所有主流编程语言

  支持数据持久化、主从复制、哨兵模式等高可用特性
  
  



## Prepare the environment

- 安装

  docker

  ```bash
  docker search redis
  docker pull redis
  docker run --restart=always -p 6379:6379 \
    --name myredis -d redis:5.0.14 \
    --requirepass 123456
  
  docker exec -it myredis bash
  redis-server  # 服务端 开机自启
  redis-cli -a 123456  # 客户端
  
  ```

- 使用方式

  CLI：Command Line Interface ([Redis-CLI](https://redis.io/docs/manual/cli))

  API：Application Programming Interface (programming language)

  GUI：Graphical User Interface ([Redis Insight](https://redis.io/docs/connect/insight/))





## basic operation

- 常用命令

  



- 数据类型

  五种基本数据类型：`String`、`List`、`Set`、`SortedSet`、`Hash`

  五种高级数据类型：`Stream`、`Geospatial HyperLogLog`、`Bitmap`、`Bitfield`

- 键值对数据

  键是大小写敏感的、默认使用字符串来存储数据(二进制安全)、默认不支持中文(二进制形式)

- String

  ```bash
  # 设置 读取 删除 判断
  set name zhou
  get name  # "zhou"
  set Name Zhou
  get Name  # "Zhou"
  
  del name  # 删除
  exists name  # 判断一个键是否存在
  
  keys *me  # 查看数据库有哪些键 
  flushall  # 删除所有的键 (慎用)
  
  # 中文显示问题
  quit
  redis-cli --raw
  
  
  # 查看键的过期时间
  ttl name  # time to live
  # 设置一个带有过期时间的键值对
  expire name 10
  setex name 10 zhou
  # 只有当键不存在才创建
  setnx name zhou
  
  ```

- List (有序列表)

  ```bash
  # 添加
  lpush letter a
  lpush letter b c  # 最后添加在最前
  rpush letter z  # 尾部添加
  # 获取
  lrange letter 0 -1
  # 删除
  lpop letter  # 头部弹出
  rpop letter 2  # 尾部弹出
  ltrim letter 0 3  # 保留 不在范围的都删掉
  # 查看列表长度
  llen letter
  
  
  # 实现简单的消息队列 (其他实现 stream)
  lpush  # 头添加
  rpop  # 尾弹出
  
  ```

- Set (无序集合 元素不能重复)

  ```bash
  # 添加
  sadd course Redis  # 不能添加重复的元素
  # 获取
  smembers course
  # 判断
  sismember course Redis
  # 删除
  srem course Redis
  
  # 集合的交集并集运算
  sinter
  sunion
  sdiff
  
  ```

- SortedSet ZSet (有序集合)

  每个元素都会关联一个浮点类型的分数 按照此分数从小到大排序 

  分数可以重复

  ```bash
  # 添加
  zadd result 680 tsinghua 679 peking 650 zhu
  # 获取
  zrange result 0 -1  # 仅元素 (全部)
  zrange result 0 -1 withscores  # 加分数 (全部)
  zscore result tsinghua  # 知元素查分数 (单个)
  zrank result tsinghua  # 知元素查index (单个)
  zrevrank result tsinghua  # 反转 reverse
  # 删除某个元素
  # 对某个元素的分数增加
  
  ```

- Hash (字符类型的字段和值的映射表 键值对的集合 适合存储对象)

  ```bash
  # 添加
  hset person name zhou 
  hset person age 22
  # 获取
  hget person name 
  hgetall person
  hkeys person  # 获取所有键
  hlen person  # 获取所有键值对数量
  # 删除
  hdel person age 
  # 判断
  hexists person name 
  
  ```

  



- 发布订阅模式

  弊端：消息无法持久化、无法记录历史消息

  ```bash
  # 将消息发送到指定频道
  publish time1043 flink
  # 订阅这个频道
  subscribe time1043  # 可以多个订阅
  
  ```

- Stream (轻量级的消息队列 解决消息持久化)

  ```bash
  # 添加
  xadd time1043 1-0 course github  # 手动设置id
  xadd time1043 * course spark  # *表示自动生成消息id kv
  xadd time1043 * course docker  # "1712571786871-0"
  # 查看
  xlen time1043  # 个数
  xrange time1043 - +  # 详细内容 -+ 开始结束
  # 删除
  xdel time1043 1712571786871-0
  xtrim time1043 maxlen 0  # 删除所有
  # 消费
  xread count 2 block 1000 streams time1043  # 没有消息的就阻塞1000s 0即从头开始读取
  ```

  





- 事务

  



- 数据持久化

  



- 主从复制

  



- 哨兵模式

  



- 集群部署

  











# MySQL











# Oracle







# DaMeng 

- Reference

  [dameng docs](https://eco.dameng.com/document/dm/zh-cn/start/index.html)

  



## Prepare the environment

### win

- win GUI



- win docker 

  ```bash
  cd /d/DockerContainers/DaMeng/
  mdir dm8_test
  
  docker load -i dm8_20230808_rev197096_x86_rh6_64_single.tar
  docker images
  
  docker run -d \
    -p 30236:5236 \
    --restart=always \
    --name dm8_test \
    --privileged=true \
    -e PAGE_SIZE=16 \
    -e LD_LIBRARY_PATH=/opt/dmdbms/bin \
    -e EXTENT_SIZE=32 -e BLANK_PAD_MODE=1 -e LOG_SIZE=1024 -e UNICODE_FLAG=1 -e LENGTH_IN_CHAR=1 \
    -e INSTANCE_NAME=dm8_test \
    -v D:\\DockerContainers\\DaMeng\\dm8_test:/opt/dmdbms/data \
    dm8_single:dm8_20230808_rev197096_x86_rh6_64
  
  docker logs -f dm8_test  # 查看日志
  docker inspect dm8_test  # 查看数据库初始化的参数
  
  docker stop dm8_test
  docker start dm8_test
  docker restart dm8_test
  
  
  docker exec -it dm8_test bash
  source /etc/profile
  
  cd /opt/dmdbms && ls  # bin  bin2  data  log
  cd /opt/dmdbms/bin
  ./disql SYSDBA/SYSDBA001
  
  ```

- notice

  > 1.如果使用 docker 容器里面的 disql，进入容器后，先执行 source /etc/profile 防止中文乱码。
  >
  > 2.新版本 Docker 镜像中数据库默认用户名/密码为 SYSDBA/SYSDBA001。

  



### linux





## playground

- 检查数据库版本及服务状态

  ```sql
  select * from v$version;  # 查看数据库版本 
  select status$ from v$instance;  # 查看达梦数据库当前状态
  select group_id, id, path, status$ from v$datafile;  # 查询数据文件位置 	
  
  ```

- 创建用户并授权

  ```sql
  create user DM identified by "dameng123";  # 创建用户
  
  grant resource to dm;  # 授予 RESOURCE 角色
  grant select on dmhr.employee to dm;  # 授予 dmhr 用户下 employee 表的 select 权限
  grant select on dmhr.department to dm;  # 授予 dmhr 用户下 department 表的 select 权限
  
  select username, account_status, created from dba_users where username='dm';  # 查看用户信息
  
  ```

- 切换用户

  ```sql
  conn dm/dameng123;  # 切换到DM用户
  select user from dual;  # 查看当前登录用户
  
  ```

  

### 基本表

- 创建表并添加约束

  ```sql
  # 创建 employee 表
  create table employee
  (
    employee_id integer,
    employee_name varchar2(20) not null,
    hire_date date,
    salary integer,
    department_id integer not null
  );
  
  # 创建 department 表
  create table department
  (
    department_id integer primary key,
    department_name varchar(30) not null
  );
  
  
  alter table employee modify(hire_date not null);  # 非空约束
  alter table employee add constraint pk_empid primary key(employee_id);  # 主键约束
  alter table employee add consttaint fk_dept foreign key (department_id) references department (department_id);  # 外键约束
  
  select table_name, constraint_name, constraint_type from all_constraints where owner='dm' and table_name='employee';  # 查看表主键外键
  
  ```

- 验证数据表 CRUD 功能

  ```sql
  # 存在主外键约束 须按顺序执行插入语句 
  insert into department values (666, '数据库产品中心');
  insert into employee values (9999, '王达梦','2008-05-30 00:00:00', 30000, 666);
  commit;
  
  # 修改数据
  update employee set salary='35000' where employee_id=9999;
  commit;
  
  # 查询数据
  select salary, employee_id from employee;
  
  # 删除数据
  delete from employee;  # 删除表数据
  delete from department where department_id=666;  # 条件
  commit;
  
  ```

- 批量插入及选择排序

  ```sql
  # 在 t1 表中批量插入 100000 条数据记录
  create table t1 as
  select rownum as id
  ,trunc(dbms_random.value(0, 100)) as random_id
  ,dbms_random.string('x',20) as random_string
  from dual
  connect by level <= 100000;
  
  select * from t1;
  select count(*) from t1;
  
  # 排序数据
  select * from t1 
  where rownum < 5 
  order by id desc; 	
  
  ```

- 分组查询

  ```sql
  # insert into 批量插入数据
  insert into department (department_id, department_name)
  select department_id, department_name from dmhr.department;
  
  insert into employee (employee_id, employee_name, hire_date, salary, department_id)
  select employee_id, employee_name, hire_date, salary, department_id from dmhr.employee;
  
  # 分组查询
  select dept.department_name as 部门, count(*) as 人数
  from employee emp, department dept
  where emp.department_id=dept.department_id
  group by dept.department_name
  having count(*) > 20;
  
  ```

  



### 视图、索引及事务

- 视图

  ```sql
  # 定义视图
  create or replace view v1 as 
  select dept.department_name, emp.employee_name, emp.salary, emp.hire_date
  from employee emp, department dept
  where salary > 10000
  and hire_date >= '2013-08-01'
  and emp.department_id = dept.department_id;
  
  # 通过视图简化查询
  select * from v1 where hire_date > '2014-09-01';
  
  ```

- 索引

  ```sql
  # 创建普通索引
  create index ind_emp_salary on employee(salary);
  
  # 查看创建的索引
  select table_name, index_name, index_type 
  from user_indexes where index_name = 'ind_emp_salary';
  
  # 删除索引
  drop index ind_emp_salary;
  
  ```

- 事务特性

  ```sql
   # 创建保存点
  insert into employee values (999, '罗小刚', '2020-05-30 00:00:00', 50000, 101);  # 插入数据
  savepoint my_insert; 
  
  update employee set department_id=102 where employee_id=999;  # 使用 UPDATE 语句更新数据记录，不提交
  select employee_id, department_id from employee where employee_id=999;  # 不提交查看数据记录
  
  # 回滚到保存点
  rollback to my_insert;
  
  ```

  



### 序列、物化视图及函数

- 序列

  ```sql
  # 创建序列
  create sequence seq1
  start with 1 increment by 1 maxvalue 10000
  cache 5 nocycle;
  
  # 查询下一个序列号
  select seq1.nextval() from dual;
  
  # 查询当前序列号
  select seq1.currval() from dual;
  
  ```

- 物化视图

  ```sql
  # 定义物化视图
  create materialized view mv1 build immediate refresh
  complete on commit as 
  select department_id as 部门号, count(*) as 人数
  from employee group by department_id;
  
  # 使用物化视图 检索数据
  select * from mv1 where 部门号='101';
  
  
  insert into employee values (8888, '苏林', '2020-05-31 00:00:00', 60000, 101);
  commit;	
  
  # 使用物化视图 检索数据
  select * from mv1 where 部门号='101';
  
  ```

- 自定义函数

  ```sql
  # 创建生成随机数函数
  create or replace function random_password(pass_len in number) ruturn varchar2 as
  l_pw varchar2(128);
  begin l_pw = dbms_random.string('x', pass_len);
  return l_pw;
  end;
  
  # 调用函数生成随机数
  select random_password(12) from dual;
  
  ```

- 自定义存储过程

  例如：将某一部门下所有入职时间大于指定时间的员工的薪资上浮 15%

  ```sql
  select employee_id, employee_name, salary 
  from dm.employee 
  where department_id = 102 and hire_date >= to_date('2012-03-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss');
  
  # 创建存储过程 
  create or replace procedure proc (dept_in dm.employee.department_id%type, hire_in varchar2(24))
  as cursor by_dept_cur is
  select * from dm.employee where department_id = dept_in;
  begin for rec in by_dept_cur
    loop
      if rec.hire_date > to_date(hire_in, 'yyyy-mm-dd hh24:mi:ss')
      then
      update dm.employee set salary = salary + salary * 0.15
      where employee_id = rec.employee_id;
      end if;
    end loop;
  commit;
  end;
  
  # 调用存储过程
  begin 
  proc(102, '2012-03-01 00:00:00');
  end;
  
  # 查询验证
  
  ```

  



- 触发器

  表级触发器是基于表中数据的触发器，它通过针对相应表对象的插入/删除/修改等 DML 语句的触发。

  例如：在员工表上建立表级触发器，当姓名字段被更新时触发器动作

  ```sql
  # 创建表 trg , 记录员工姓名更新前后的值
  create table trg(name_old varchar, name_new varchar);
  
  # 创建触发器 trg1
  create or replace trigger trg1
  before 
  update of employee_name on employee
  for each row 
  declare
  begin
  insert into trg values(:old.employee_name, :new.employee_name);
  end;
  
  # 修改动作
  update employee set employee_name='达梦' where employee_id=1001;
  commit;
  
  # 查询验证
  select name_old, name_new from trg;
  
  ```

  

- 分区表

  间隔分区可以在输入相应分区的数据后自动创建分区，是范围分区的扩展。

  例如：将 dmhr 用户下 employee 表中员工信息按入职时间以年为间隔转换为分区表

  ```sql
  # 创建间隔分区表
  create table emp_part
  (
    employee_id int primary key,
    employee_name varchar(20),
    identity_card varchar(18),
    email varchar(50) not null,
    phone_num varchar(20),
    hire_date date not null,
    job_id varchar(10) not null,
    salary int,
    commission_pct int,
    manager_id int,
    department_id int
  )
  partition by range(hire_date)
  interval (numtoyminterval(1, 'year'))
  (
    partition p_before_2007 values less than (to_date('2007-01-01','yyyy-mm-dd'))
  )
  storage
  (
    fillfactor 85,
    branch(32, 32)
  );
  
  # 插入数据
  insert into emp_part select * from dmhr.employee;
  commit;
  
  # 查询分区信息
  select table_name, partition_name, high_value from user_tab_partitions
  where table_name = 'emp_part' order by high_value;
  
  # 检索某个分区数据
  select * from emp_part partition(p_before_2007);
  
  # 插入数据，自动新增分区表
  insert into emp_part(employee_id, employee_name, identity_card, email, phone_num, hire_date, job_id, salary, commission_pct, manager_id, department_id) values
  (9990,'武达梦','340102196202303999','wudm@dameng.com','15312348566','2020-05-30','11',50000.00,0,1001,101);
  commit;
  
  # 查询新增数据分区
  select table_name, partition_name, high_value from user_tab_partitions
  where table_name = 'emp_part' order by high_value;
  
  ```

  

- with 子句

  with function 子句用于在 SQL 语句中临时声明并定义存储函数，这些存储函数可以在其作用域内被引用

  with as 子句可以优化查询流程，获得清晰的格式

  ```sql
  # with function 子句 (通过员工编号获取对应的薪资)
  with function GetSalary(emp_id int) return int as
  declare
  sal int;
  begin
  select salary into sal from dmhr.employee where employee_id = emp_id;
  return sal;
  end;
  select GetSalary(2001) from dual;
  
  # with as 子句(统计入职时间最早和最迟的员工的编号、姓名和入职时间)
  with t as (select max(hire_date) max_hd, min(hire_date) min_hd from dmhr.employee)
  select employee_name, employee_id, hire_date from dmhr.employee
  where hire_date in 
  (
      select t.max_hd from t
      union all
      select t.min_hd from t
  );
  
  ```

  1
  
  ```sql
  # 查看当前用户所有表
  select table_name,tablespace_name from user_tables;
  # 创建表空间
  create tablespace TEST datafile '/home/dmdba/opt/dmdbms/data/DAMENG/TEST.DBF' size 50;
  # 创建表
  create table DMTEST.EMP(EMP_ID INTEGER,EMP_NAME  VARCHAR(20));
  # 创建用户并指定表空间
  create user test1 identified by 123456789 default tablespace test;
  ```
  
  



- 数据库自身信息

  查询实例信息、查询数据库当前状态、查询DB_MAGIC、

  查询是否归档、查询授权截止有效期、查看等待情况、

  查看数据库配置端口、查询数据库最大连接数、查询命令执行计划、

  查询用户密码限制登录次数和密码过期天数、查询数据库字符集、

  修改密码策略、查看密码策略、查看每个用户的密码策略

  ```sql
  select name inst_name from v$instance;  # 查询实例信息
  select status$ from v$instance;  # 查询数据库当前状态
  select db_magic from v$rlog;  # 查询DB_MAGIC
  
  select arch_mode from v$database;  # 查询是否归档
  select EXPIRED_DATE from v$license;  # 查询授权截止有效期
  select class_name,total_waits count from v$wait_class;  # 查看等待情况
  
  select para_name,para_value from v$dm_ini where para_name like '%PORT%';  # 查看数据库配置端口
  select SF_GET_PARA_VALUE(2,'MAX_SESSIONS');  # 查询数据库最大连接数
  explain select * from test_table;  # 查询命令执行计划
  
  select u.username,p.FAILED_NUM,p.life_time from SYSUSERS p,dba_users u where  p.FAILED_NUM not in ('0') order by 1,2 ;  # 
  select SF_GET_UNICODE_FLAG();  # 
  
  select * from v$dm_ini a where a.PARA_NAME = 'PWD_POLICY';  # 查看密码策略
  SP_SET_PARA_VALUE(1,'PWD_POLICY',3);  # 修改密码策略
  select username,password_versions,account_status from dba_users;  # 查看每个用户的密码策略
  
  ```

- 数据库文件/空间信息

  查询归档信息、查看控制文件、查询日志文件、查询数据库占用空间、

  查询数据文件位置、查询表空间大小、

  查看表空间使用情况、查询当前用户模式

  ```sql
  select * from v$dm_arch_ini;  # 查询归档信息
  select para_value name from v$dm_ini where para_name='CTL_PATH';  # 查看控制文件
  select GROUP_ID ,FILE_ID,PATH,CLIENT_PATH from v$rlogfile;  # 查询日志文件
  select sum(bytes/1024/1024)|| 'M' from dba_data_files;  # 查询数据库占用空间
  
  select group_id, id, path, status$ from v$datafile;  # 查询数据文件位置 	
  select FILE_NAME,FILE_ID,TABLESPACE_NAME,BYTES/1024/1024||'M'  from dba_data_files;  # 查询表空间大小
  
  select t1.NAME tablespace_name,
      t2.FREE_SIZE*SF_GET_PAGE_SIZE()/1024/1024 ||'M' free_space,
      t2.TOTAL_SIZE*SF_GET_PAGE_SIZE()/1024/1024 ||'M' total_space,
      t2.FREE_SIZE*100/t2.total_size "% FREE" 
      from V$TABLESPACE t1, V$DATAFILE t2 where t1.ID=t2.GROUP_ID;  # 查看表空间使用情况
  SELECT SYS_CONTEXT ('userenv', 'current_schema') FROM DUAL;  # 查询当前用户模式
  
  ```

- 数据库用户/角色信息

  查询数据库有哪些用户、查询数据库用户信息、查看数据库对象、查询用户对象、

  查看角色类型、查看用户的角色和权限、表空间脱机/在线

  ```sql
  select username from dba_users;
  select username,user_id,default_tablespace,profile from dba_users;  
  
  ```

- 数据库运维信息

  创建表空间、查询总表数量、关闭数据库、创建用户

  ```sql
  create tablespace TEST datafile '/home/dmdba/opt/dmdbms/data/DAMENG/TEST.DBF' size 50;
  
  select count(*) from dba_tables;
  
  shutdown normal;  # 关闭数据库
  shutdown immediate;  # 正常方式关闭数据库
  shutdown abort;  # 立即方式关闭数据库。数据库并不立即关闭，而是在执行某些清除工作后才关闭（终止会话、释放会话资源），需要10到20S。
  
  create user test1 identified by 123456789 default tablespace test;
  
  ```

- 数据库表/列/视图信息

  查询当前用户所有表、查询表的大小、创建新表、增加表的列、删除表的列、

  增加表注释、查询表注释、增加列注释、查询列注释、

  重命名表名、创建视图

  ```sql
  select table_name,tablespace_name from user_tables;  # 
  SELECT TABLE_USED_SPACE ('SYS','SYSOBJECTS') ;
  create table tests ( id char not null) ;
  alter table test_rename add ids int;  # 增加表的列
  alter table test_table drop ids;  # 删除表的列
  
  comment on table test_rename is 'AAAAAAA';
  select comments from user_tab_comments where table_name = 'TEST_RENAME';
  comment on column test_rename.id is 'Primary'; 
  select * from user_col_comments where owner = 'SYSDBA' and table_name = 'TEST_RENAME' and column_name = 'ID';
  
  alter table tests rename to test_rename;
  create view v_test as select C1,C2 from T1 where C3='r';
  
  ```





















































