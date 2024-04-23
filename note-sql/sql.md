# sql

- 参考

  [leetcode 50 sql](https://leetcode.cn/studyplan/sql-free-50/)

  



## 窗口函数

- 窗口函数

  作用：允许在一个查询中执行复杂的分析计算，而不需要复杂的子查询或多步查询
  
- 窗口函数表达式

    ```
    function(args) over ( 
      [partitionn by expression] 
      [order by expression [asc|desc]] 
      [frame frame_start, frame_end]
    )
    
    
    # function: row_number, rank, densen_rank; sum, avg, count, min, max
    # over: define rules for window functions
    
    # partitionn by expression：（可选）根据一个或多个列的值将数据分成不同的分区。在每个分区内部，窗口函数会独立地计算每一行的结果
    # order by expression [ASC|DESC]：（可选）定义窗口内部的行的排序规则。默认升序ASC，可指定 DESC 降序
    # order by 在没有 partitionn by 的情况下是必需的，因为窗口函数需要知道如何对行进行排序
    
    
    # frame frame_start, frame_end：（可选）定义窗口的行范围，即“帧”。帧定义了窗口函数应用的行集。帧可以是以下几种类型：
    # range：基于行之间的范围，比如 range between unbounded preceding and current row 表示从查询结果的第一行到当前行。
    # rows：基于行数，比如 rows between 1 preceding and 1 following 表示包括当前行及其前后各一行。
    # groups：基于数据的分组，通常与 order by 子句结合使用。
    
    # frame_start 可以是以下几种：
    # unbounded preceding：表示从分区的第一行开始。
    # expression preceding：表示从当前行之前的第 expression 行开始。
    # current row：表示从当前行开始。
    
    # frame_end 可以是以下几种：
    # unbounded following：表示到分区的最后一行结束。
    # expression following：表示从当前行之后的第 expression 行结束。
    # current row：表示到当前行结束。
    # 若不指定 frame 子句，窗口函数将使用默认的 range between unbounded preceding and current row。
    
    ```
    
    

- 环比和同比

  环比：相邻月的增长  (2021-06 2021-05)

  同比：相同月的增长  (2021-06 2020-06)





### 排序函数

- 排序函数

  `row_number()` 序号**不重复**、序号连续 (1,2,3,...)

  `rank()` 序号可重复、序号**不连续** (1,2,2,4,...)

  `dense_rank()` 序号可重复、序号**连续** (1,2,2,3,...)

  



- 非等值 子连接

  构造辅助表、计数

- 题目

- 环境

  ```sql
  drop table if exists product_info;
  create table product_info (
      product varchar(30) not null,
      price int not null
  );
  
  insert into product_info (product, price) values
  ('A',100),('B',300),('C',200),('D',1000);
  
  ```

- sql

  ```sql
  # 非等值 子连接
  select p1.product
  ,p1.price
  ,(
  	select count(p2.price)
      from product_info p2
      where p2.price > p1.price
  ) + 1 as rank_1
  from product_info p1;
  
  ```

  





### 聚合函数实现滑动窗口计算

- 常用聚合函数

  `count(col)` 返回所有非空值的个数、`count(*)` 、`count(字段)` 空值不计入

  `avg(col)`、`sum(col)`、`max(col)`、`min(col)`、`first(col)`、`last(col)`



- 聚合函数实现滑动窗口计算

  rows模式：按照物理行进行划分

  range模式：按数值逻辑来进行划分

  

- 滑动行范围的常用表达

- {range|rows} frame_start

- {range|rows} between frame_start and frame_end

  unbounded preceding

  expression preceding -- only allowed in rows mode

  current row

  expression following -- only allowed in rows mode

  unbounded following 

  



- 题目

  > 求最近三月的平均金额 
  >
  > 滚动求从上架开始到本月的平均avg

- 环境

  ```sql
  -- 删除已存在的product表
  drop table if exists product;
  
  -- 创建product表
  create table `product` (
      `product` varchar(255) not null,
      `year_month_my` date not null, -- 格式如 'yyyy-mm'
      `department` varchar(255) not null,
      `gmv` decimal(6, 2) not null  -- 假设gmv是金额，保留两位小数
  );
  
  -- 插入数据，确保每个产品在不同的year_month中有6条记录
  insert into `product` (`product`, `year_month_my`, `department`, `gmv`)  values
  -- 2021
  ('bags', '2021-01-01', 'fashion', 1000.00),('bags', '2021-02-01', 'fashion', 1025.00),
  ('bags', '2021-03-01', 'fashion', 1050.00),('bags', '2021-04-01', 'fashion', 1075.00),
  ('bags', '2021-05-01', 'fashion', 1100.00),('bags', '2021-06-01', 'fashion', 1125.00),
  ('bags', '2021-07-01', 'fashion', 1150.00),('bags', '2021-08-01', 'fashion', 1175.00),
  ('bags', '2021-09-01', 'fashion', 1200.00),('bags', '2021-10-01', 'fashion', 1225.00),
  ('bags', '2021-11-01', 'fashion', 1250.00),('bags', '2021-12-01', 'fashion', 1275.00),
  ('makeup', '2021-01-01', 'beauty', 450.00),('makeup', '2021-02-01', 'beauty', 470.00),
  ('makeup', '2021-03-01', 'beauty', 490.00),('makeup', '2021-04-01', 'beauty', 510.00),
  ('makeup', '2021-05-01', 'beauty', 530.00),('makeup', '2021-06-01', 'beauty', 550.00),
  ('makeup', '2021-07-01', 'beauty', 570.00),('makeup', '2021-08-01', 'beauty', 590.00),
  ('makeup', '2021-09-01', 'beauty', 610.00),('makeup', '2021-10-01', 'beauty', 630.00),
  ('makeup', '2021-11-01', 'beauty', 650.00),('makeup', '2021-12-01', 'beauty', 670.00),
  -- 2022
  ('bags', '2022-01-01', 'fashion', 1300.00),('bags', '2022-02-01', 'fashion', 1325.00),
  ('bags', '2022-03-01', 'fashion', 1350.00),('bags', '2022-04-01', 'fashion', 1375.00),
  ('bags', '2022-05-01', 'fashion', 1400.00),('bags', '2022-06-01', 'fashion', 1425.00),
  ('bags', '2022-07-01', 'fashion', 1450.00),('bags', '2022-08-01', 'fashion', 1475.00),
  ('bags', '2022-09-01', 'fashion', 1500.00),('bags', '2022-10-01', 'fashion', 1525.00),
  ('bags', '2022-11-01', 'fashion', 1550.00),('bags', '2022-12-01', 'fashion', 1575.00),
  ('makeup', '2022-01-01', 'beauty', 700.00),('makeup', '2022-02-01', 'beauty', 720.00),
  ('makeup', '2022-03-01', 'beauty', 740.00),('makeup', '2022-04-01', 'beauty', 760.00),
  ('makeup', '2022-05-01', 'beauty', 780.00),('makeup', '2022-06-01', 'beauty', 800.00),
  ('makeup', '2022-07-01', 'beauty', 820.00),('makeup', '2022-08-01', 'beauty', 840.00),
  ('makeup', '2022-09-01', 'beauty', 860.00),('makeup', '2022-10-01', 'beauty', 880.00),
  ('makeup', '2022-11-01', 'beauty', 900.00),('makeup', '2022-12-01', 'beauty', 920.00),
  -- 2023
  ('bags', '2023-01-01', 'fashion', 1600.00),('bags', '2023-02-01', 'fashion', 1625.00),
  ('bags', '2023-03-01', 'fashion', 1650.00),('bags', '2023-04-01', 'fashion', 1675.00),
  ('bags', '2023-05-01', 'fashion', 1700.00),('bags', '2023-06-01', 'fashion', 1725.00),
  ('bags', '2023-07-01', 'fashion', 1750.00),('bags', '2023-08-01', 'fashion', 1775.00),
  ('bags', '2023-09-01', 'fashion', 1800.00),('bags', '2023-10-01', 'fashion', 1825.00),
  ('bags', '2023-11-01', 'fashion', 1850.00),('bags', '2023-12-01', 'fashion', 1875.00),
  ('makeup', '2023-01-01', 'beauty', 950.00),('makeup', '2023-02-01', 'beauty', 970.00),
  ('makeup', '2023-03-01', 'beauty', 990.00),('makeup', '2023-04-01', 'beauty', 1010.00),
  ('makeup', '2023-05-01', 'beauty', 1030.00),('makeup', '2023-06-01', 'beauty', 500.00),
  ('makeup', '2023-07-01', 'beauty', 500.00),('makeup', '2023-08-01', 'beauty', 520.00),
  ('makeup', '2023-09-01', 'beauty', 550.00),('makeup', '2023-10-01', 'beauty', 600.00),
  ('makeup', '2023-11-01', 'beauty', 650.00),('makeup', '2023-12-01', 'beauty', 700.00);
  
  ```

- sql

  ```sql
  # 求最近三月的平均金额 (12 -> 10 11 12 往上2行 到当前行; avg)
  # 滚动求从上架开始到本月的平均avg (默认是分组的开始行 到当前行)
  select product
  ,year_month_my
  ,gmv
  ,avg(gmv) over (partition by department, product order by year_month_my rows 2 preceding) as `avg_gmv 滚动3月平均`
  ,avg(gmv) over (partition by department, product order by year_month_my) as `avg_gmv 从开始到现在`
  from product;
  
  ```

  





### 分布函数

- 分布函数

  `percent_rank()` (分组内当前行的rank值-1)/(分组内总行数-1)

  `cume_dist()` 小于等于当前值的行数/分组内总行数





### 前后函数求环比

- 前后函数

  `lead(expression, n)` 返回当前行的后n行 

  `lag(expression, n)` 返回当前行的前n行

  



- 题目

  > 求每个产品的gmv的环比增幅

- sql

  ```sql
  # 上一行的数据 lag(gmv, 1)
  
  # 求每个产品的gmv的环比增幅
  select product
  ,year_month_my
  ,gmv
  ,lag(gmv, 1) over (partition by department, product order by year_month_my) as lag_gmv
  ,cast(gmv as double) / lag(gmv, 1) over(partition by department, product order by year_month_my) - 1 as growth_rate
  from product;
  
  # 同比
  select product
  ,year_month_my
  ,gmv
  ,lag(gmv, 12) over (partition by department, product order by year_month_my) as lag_gmv
  ,cast(gmv as double) / lag(gmv, 12) over(partition by department, product order by year_month_my) - 1 as growth_rate
  from product;
  
  ```

- 新问题

  日期不连续？通过join万年历表





## leetcode sql

### leetcode 178. 分数排名

- [题目](https://leetcode.cn/problems/rank-scores/) (排序函数)

  ```
  表: Scores
  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | score       | decimal |
  +-------------+---------+
  在 SQL 中，id 是该表的主键。
  该表的每一行都包含了一场比赛的分数。Score 是一个有两位小数点的浮点值。
   
  查询并对分数进行排序。排名按以下规则计算:
  分数应按从高到低排列。
  如果两个分数相等，那么两个分数的排名应该相同。
  在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。
  
  按 score 降序返回结果表。
  
  ```

- 思路

  分数应按从高到低排列。 (desc)

  如果两个分数相等，那么两个分数的排名应该相同。 (可重复)

  在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。 (连续 `dense_rank()`)



- 环境

  ```sql
  drop table if exists scores;
  create table scores (
    id int primary key,
    score decimal(10, 2) -- 10位数字，其中2位是小数
  );
  
  insert into scores (id, score) values (1, 85.99);
  insert into scores (id, score) values (2, 92.50);
  insert into scores (id, score) values (3, 92.50); -- 与第二行分数相同
  insert into scores (id, score) values (4, 78.80);
  insert into scores (id, score) values (5, 95.00);
  insert into scores (id, score) values (6, 95.00); -- 与第五行分数相同
  
  ```

- 写sql

  ```sql
  select id
  ,score
  ,dense_rank() over(order by score desc) as `rank`
  from scores;
  
  ```

  



### leetcode 184. 部门工资最高的员工

- [题目](https://leetcode.cn/problems/department-highest-salary/) (排序函数)

  ```
  表： Employee
  +--------------+---------+
  | 列名          | 类型    |
  +--------------+---------+
  | id           | int     |
  | name         | varchar |
  | salary       | int     |
  | departmentId | int     |
  +--------------+---------+
  在 SQL 中，id是此表的主键。
  departmentId 是 Department 表中 id 的外键（在 Pandas 中称为 join key）。
  此表的每一行都表示员工的 id、姓名和工资。它还包含他们所在部门的 id。
  
  表： Department
  +-------------+---------+
  | 列名         | 类型    |
  +-------------+---------+
  | id          | int     |
  | name        | varchar |
  +-------------+---------+
  在 SQL 中，id 是此表的主键列。
  此表的每一行都表示一个部门的 id 及其名称。
   
  
  查找出每个部门中薪资最高的员工。
  按 任意顺序 返回结果表。
  
  ```

- 思路

  根据departmentId分组、按salary排序

  可重复且不必连续 (`rank()` `dense_rank()`)

  排序后再取第一名



- 环境

  ```sql
  drop table if exists employee;
  drop table if exists department;
  
  create table department (
    id int primary key,
    name varchar(255)
  );
  create table employee (
    id int primary key,
    name varchar(255),
    salary int,
    departmentid int,
    foreign key (departmentid) references department(id)
  );
  
  
  insert into department (id, name) values (1, 'research and development');
  insert into department (id, name) values (2, 'human resources');
  insert into department (id, name) values (3, 'marketing');
  
  insert into employee (id, name, salary, departmentid) values (1, 'alice', 80000, 1);
  insert into employee (id, name, salary, departmentid) values (2, 'bob', 80000, 1);
  insert into employee (id, name, salary, departmentid) values (3, 'charlie', 50000, 2);
  insert into employee (id, name, salary, departmentid) values (4, 'david', 60000, 2);
  insert into employee (id, name, salary, departmentid) values (5, 'eva', 90000, 3);
  insert into employee (id, name, salary, departmentid) values (6, 'frank', 95000, 3);
  
  ```

- 写sql

  ```sql
  # rank dense_rank
  select department, employee, salary
  from (
      select 
      d.name department
      ,e.name employee
      ,e.salary
      ,rank() over(partition by departmentid order by salary desc) salary_rank
      from employee e
      join department d on d.id = e.departmentid
  ) temp
  where salary_rank=1;
  
  
  select e1.id, e1.name, e1.salary, e1.departmentid
  from employee e1
  inner join (
      select departmentid, max(salary) as max_salary
      from employee
      group by departmentid
  ) e2 on e1.departmentid = e2.departmentid and e1.salary = e2.max_salary;
  
  ```

  



### leetcode 173. 最多连胜的次数

- 题目

  ```
  
  选手的 连胜数 是指连续获胜的次数，且没有被平局或输球中断。
  编写解决方案来计算每个参赛选手最多的连胜数。
  结果可以以 任何顺序 返回。
  
  1. 连胜的最大次数
  2. 连胜的最大天数 (数据量很大)
  
  ```

- 思路

  按 player_id, match_day 排序

  开窗 `row_number()` 打标记 (按match_day 按result win1)

  ```
  +-----------+------------+--------+
  | player_id | match_day  | result |
  +-----------+------------+--------+
  |         1 | 2024-03-01 | Win    |  1    1  1 -> 0 
  |         1 | 2024-03-02 | Win    |  1    2  2 -> 0
  |         1 | 2024-03-03 | Win    |  1    3  3 -> 0
  |         1 | 2024-03-04 | Draw   |  0    4  1 -> 3
  |         1 | 2024-03-05 | Win    |  1    5  4 -> 1
  
  ```

  

- 环境

  ```sql
  drop table if exists matches;
  create table matches (
  	player_id int,
      match_day date,
      result varchar(20)
  );
  
  insert into matches (player_id, match_day, result) values
  (2, '2024-03-08', 'Loss'),
  (3, '2024-03-09', 'Win'),
  (3, '2024-03-10', 'Win'),
  (3, '2024-03-11', 'Draw'),
  (3, '2024-03-12', 'Loss'),
  (1, '2024-03-01', 'Win'),
  (1, '2024-03-02', 'Win'),
  (1, '2024-03-03', 'Win'),
  (1, '2024-03-04', 'Draw'),
  (1, '2024-03-05', 'Win'),
  (2, '2024-03-06', 'Win'),
  (2, '2024-03-07', 'Win'),
  (3, '2024-03-17', 'Win'),
  (3, '2024-03-14', 'Win'),
  (3, '2024-03-15', 'Win'),
  (4, '2024-03-01', 'Win'),
  (4, '2024-03-14', 'Win'),
  (4, '2024-03-15', 'Win'),
  (4, '2024-03-16', 'Loss');
  
  ```

- sql

  ```sql
  # 按 player_id, match_day 排序
  select *
  from matches
  order by player_id, match_day;
  
  # 开窗 打标记
  select player_id
  ,if(result='win', '1', '0') as if_win
  ,row_number() over(partition by player_id order by match_day) as num_flag1
  ,row_number() over(partition by player_id, result order by match_day) as num_flag2
  from (
      select *
      from matches
      order by player_id, match_day
  ) as t1;
  
  # num_flag1-num_flag2
  select player_id
  ,num_flag1-num_flag2
  ,sum(if_win) as cnt
  from (
      select player_id
      ,if(result='win', '1', '0') as if_win
      ,row_number() over(partition by player_id order by match_day) as num_flag1
      ,row_number() over(partition by player_id, result order by match_day) as num_flag2
      from matches
  ) as t2
  group by player_id, num_flag1-num_flag2;
  
  # group by player_id
  select player_id
  ,max(cnt) 
  from (
      select player_id
      ,num_flag1-num_flag2
      ,sum(if_win) as cnt
      from (
          select player_id
          ,if(result='win', '1', '0') as if_win
          ,row_number() over(partition by player_id order by match_day) as num_flag1
          ,row_number() over(partition by player_id, result order by match_day) as num_flag2
          from matches
      ) as t2
      group by player_id, num_flag1-num_flag2
  ) as t3
  group by player_id;
  
  ```

  



### ByteDance 求最大在线峰值人数

- 题目

  

- 思路

  





## 数据库产品

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

  定义：以ISON/XML格式进行存储

  产品：`mongoDB`，`Elasticsearch`









# PostgreSQL

- 参考

  python for everyone、django for everyone、web applications for everyone

  postgres for everyone





## 概念

- 数据库：储存数据、操作修改数据、检索查找数据

- 两类数据库

  *Relational Database*：采用了 关系模型(sql) 来组织数据的数据库、行列表

  - 常见有：PostgreSQL、MySQL、MariahDB(副本)、Oracle(付费)、SQLite(轻量 嵌入式)、SQL Server

  *non Relational Database*：

  - 常见有：redis、mongoDB、Cassandra、HBase

- PostgreSQL和MySQL的对比

  MySQL：国内使用最多；只支持部分sql标准、不那么严谨、老油条风格

  PostgreSQL：欧美使用多、社区活跃；支持所有sql标准、学院派的严谨、完全开源BSD/MIT、源码很清晰



- web业务 CRUD

  create、read、update、delete

  index、join、foreign key



- 安装 win  [PostgreSQL官网](https://www.postgresql.org/) 

- docker

  ```bash
  docker exec -it mypostgres bash
  createdb yzzy
  psql yzzy
  
  ```

  



## 通用sql

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
  
  



## 特性












# MySQL







# Oracle













# dameng

- 参考

  [dameng docs](https://eco.dameng.com/document/dm/zh-cn/start/index.html)



## 安装dameng

### win 

- win 安装

  





### win docker 

- win docker安装

  ```bash
  cd /d/systemEnvironment/docker-containers/
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
    -v D:\\systemEnvironment\\docker-containers\\dm8_test:/opt/dmdbms/data \
    dm8_single:dm8_20230808_rev197096_x86_rh6_64
  
  docker logs -f dm8_test  # 查看日志
  docker inspect dm8_test  # 查看数据库初始化的参数
  
  # 停止 启动 重启
  docker stop dm8_test
  docker start dm8_test
  docker restart dm8_test
  
  
  # 进入容器内部
  docker exec -it dm8_test bash
  source /etc/profile
  
  # dm目录结构
  cd /opt/dmdbms
  ls  # bin  bin2  data  log
  
  # 登录数据库
  cd /opt/dmdbms/bin
  ./disql SYSDBA/SYSDBA001
  
  ```

- 注意

  > 1.如果使用 docker 容器里面的 disql，进入容器后，先执行 source /etc/profile 防止中文乱码。
  >
  > 2.新版本 Docker 镜像中数据库默认用户名/密码为 SYSDBA/SYSDBA001。

  



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

  



```
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

  



# Redis 

- 概念

  Remote dictionary server：开源的、基于**内存**的 数据存储系统

  应用：DB Cache、MQ (DB **IO**开销大)

- 优势

  性能记高

  数据类型丰富，单键/值对最大支持512M大小的数据

  简单易用，支持所有主流编程语言

  支持数据持久化、主从复制、哨兵模式等高可用特性



- 安装

  docker

  ```bash
  docker search redis
  docker pull redis
  docker run --restart=always -p 6379:6379 \
  			--name myredis -d redis:7.0.12 \
  			--requirepass 123456
  
  docker exec -it myredis bash
  redis-server  # 服务端 开机自启
  redis-cli -a 123456  # 客户端
  
  ```

- 使用方式

  CLI：Command Line Interface ([Redis-CLI](https://redis.io/docs/manual/cli))

  API：Application Programming Interface (programming language)

  GUI：Graphical User Interface ([Redis Insight](https://redis.io/docs/connect/insight/))



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

  







































































































