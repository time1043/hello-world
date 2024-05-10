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

  





































  





































































































