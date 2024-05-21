# System Design

- Reference - course

  [System Design for Beginners Course (freeCodeCamp.org)](https://www.youtube.com/watch?v=m8Icp_Cid5o), 

- 参考课程：

  [Alex Xu的系统设计面试课程](https://schelley.co/alex)、[SystemExpert](https://algoexpert.io/schelley) 、[System Design Interview模拟面试](https://schelley.co/coach) 

  Java: 带你实现一个多线程网络爬虫, 教你用Maven做大型项目

  Python (后端方向): 带你用Python Flask框架做项目, 开发网站后端

  Python (数据科学方向): 带你用Python分析数据, 助你成为data scientist

  Python (AI方向): 由前Google工程师和3Blue1Brown作者授课, 带你用Python搭建AI应用

  编程入门: 由前Google资深工程师带你做项目, 学编程

  JavaScript (全栈方向): 带你用JavaScript做full stack开发

  JavaScript (纯前端方向): 带你用JavaScript开发网站前端

  C++: 带你用C++做5个硬核项目

  Algorithms: 带你实现Google Map导航算法，深入理解算法原理和应用

  Android: 由Google Android团队工程师授课, 教你零基础开发Android应用

  Machine Learning入门: 带你用PyTorch入门机器学习

  自动量化交易: 带你用深度学习实现AI trading

- 参考文档：

  [Facebook和YouTube的分布式关系性数据库](https://schelleyyuki.com/distributed-sql-database)



- Q：Google、Facebook 是如何支撑全球几十亿用户？

- 系统设计

  **Load Balancing**：访问不是直接拿给某个 `web server` 处理、而是先经过 `load balancer` 均匀分发流量 (保护web server)

  - 优点：均匀分发、轻松扩容(high scalability、high availability)
  - 实现：route robin、least connection、hashing

  **Database Design**：设计数据库模型 data model -> 数据库的选型

  - 数据模型高度结构化 (youtube metadata) -> 关系型数据库 集群 (Vitess)
  - 数据模型凌乱结构不统一(电商网站的产品目录) -> NOSQL (cassandra HBase MongoDB) 
  - 设计 data partitioning 方案

  **Caching**：database是网站最慢的部分，若web server直接给db发请求，访问量一大则 db IO过载 (保护database 减少db查询)

  - 常见：Mencache、redis
  - 应用：1963 cache 引入 cpu 设计

  **Content Delivery Network**：把网站的静态内容分发到全球，用户浏览器从最近的CDN节点拿东西

  **Asynchronous Processing**：不用等待任务完成就可以开启新的任务 (耗时的任务 ytb上传视频)

  - 实现：message queue (RabbitMQ、kafka)
  - 应用：分布式系统、后端开发、前端开发

  ![Snipaste_2024-04-07_19-52-13](res/Snipaste_2024-04-07_19-52-13.png)