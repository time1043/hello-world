# go

- Reference - org

  [Go dev](https://go.dev/), [Go docs](https://go.dev/doc/), [Go tutorail](https://go.dev/doc/tutorial/), [Go workspaces](https://go.dev/doc/tutorial/workspaces), 
  
  [GORM org](https://gorm.io/index.html), [GORM org zh](https://gorm.io/zh_CN/docs/index.html), 
  
- Reference - course

  [Go Programming Tutorial - 3 Beginner Projects (freeCodeCamp.org)](https://www.youtube.com/watch?v=k_V5VvYSlS4), 
  
  [Go Programming – Golang Course with Bonus Projects (freeCodeCamp.org)](https://www.youtube.com/watch?v=un6ZyFkqFKo), 
  
  [Go Programming Tutorial (yangxu)](https://www.bilibili.com/video/BV1fD4y1m7TD/), [Go Web (yangxu)](https://www.bilibili.com/video/BV1Xv411k7Xn/), 
  
  [Go Seminar (ByteDance)](https://www.bilibili.com/video/BV1RD421N7XY/), 
  
  [Gin mall](https://www.bilibili.com/video/BV1Zd4y1U7D8/), [Gin mall (github)](https://github.com/CocaineCong/gin-mall), 
  
- Reference - blog

  [go version manager](https://polarisxu.studygolang.com/posts/go/managing-multiple-go-versions/), [go learning!!! ](https://www.topgoer.com/), [go bible](https://golang-china.github.io/gopl-zh/ch10/ch10.html), 
  
  [go ff](https://docs.fengfengzhidao.com/#/?id=fengfeng-docs-%e6%9e%ab%e6%9e%ab%e7%9f%a5%e9%81%93%e5%ae%98%e6%96%b9%e6%96%87%e6%a1%a3), 
  
  



## 背景介绍

### 环境准备

- [go download](https://go.dev/dl/)



- win

  ```
  
  ```

  









## 数据类型

### 基本数据类型











### channel







## 流程控制

### 分支





### 循环





















## 模块开发 包管理

### gomod







### gowork

- go1.18 workspace  [Go workspaces](https://go.dev/doc/tutorial/workspaces)

  Create a module for your code

  ```bash
  cd /d/code2/hello-world/code-show/go-my 
  mkdir workspace && cd workspace
  
  mkdir hello && cd hello
  go mod init example.com/hello
  go get golang.org/x/example/hello/reverse
  
  touch hello.go
  go run .
  
  ```

  Create the workspace

  ```bash
  cd /d/code2/hello-world/code-show/go-my/workspace
  go work init ./hello
  go run ./hello
  
  
  cd /d/code2/hello-world/code-show/go-my/workspace/
  git clone https://go.googlesource.com/example
  go work use ./example/hello
  # cd workspace/example/hello/reverse
  touch /d/code2/hello-world/code-show/go-my/workspace/example/hello/reverse/int.go
  
  ```
  
  go-my\workspace\go.work
  
  ```
  go 1.20
  
  use (
  	./example/hello
  	./hello
  )
  
  ```
  
- workspace/example/hello/reverse/int.go

  ```go
  package reverse
  
  import "strconv"
  
  // Int returns the decimal reversal of the integer i.
  func Int(i int) int {
      i, _ = strconv.Atoi(String(strconv.Itoa(i)))
      return i
  }
  ```

  workspace/hello/hello.go

  ```go
  package main
  
  import (
      "fmt"
  
      "golang.org/x/example/hello/reverse"
  )
  
  func main() {
      fmt.Println(reverse.String("Hello"), reverse.Int(24601))
  }
  ```

  



- Demo

  ```bash
  mkdir user-center2 && cd user-center2  # workspaces
  mkdir go-uc  # project
  mkdir common  # 不希望公网引用 而是本地引用
  
  cd go-uc/
  go mod init github.com/time1043/user-center2/go-uc  # 公司域名 唯一标识
  cd ../common/
  go mod init github.com/time1043/user-center2/common
  
  cd .. 
  go work init ./go-uc/  # !!!
  go work use ./common/  # !!!
  code .
  
  cd go-uc/ && touch main.go
  cd ../common/ && touch utils.go
  cd ../ && go run github.com/time1043/user-center2/go-uc
  
  ```

- Show

  ```bash
  16654@administrator MINGW64 /d/code2/hello-world/code-show/go-my/user-center2 (main)
  $ tree
  .
  |-- common
  |   |-- go.mod
  |   `-- utils.go
  |-- go-uc
  |   |-- go.mod
  |   `-- main.go
  `-- go.work
  ```

  user-center2\go-uc\main.go

  ```go
  package main
  
  import (
  	"fmt"
  
  	utils "github.com/time1043/user-center2/common"
  )
  
  func main() {
  	fmt.Println("This is go-uc!")
  	utils.Hello()
  }
  
  ```

  user-center2\common\utils.go

  ```go
  package utils
  
  import "fmt"
  
  func Hello() {
  	fmt.Println("This is common utils!")
  }
  
  ```

  







# Go (yangxu)







# Go (ff)







# Gin (ff)







# Gorm (ff)

- ORM

  Object Relational Mapping 对象关系映射 解决了**对象**和**关系型数据库**之间的数据交互问题

  用一个类表示一张表，类中的属性表示表的字段，类的是实例化对象表示一条记录

  使用对象的方法操作数据库，不用手动编写sql

- ORM 优缺

  优点：不用自己写繁琐的sql、避免sql注入 (ORM解决)

  缺点： 学习成本、复杂sql写不了、sql生成不能干预、很重

- ORM 常见

  Go: `GORM`

  Java: `Mybatis`, `Hibernate`

  Python: `DjangoORM`, `SQLAlchemy`

  



## 环境准备

- 环境准备

  ```bash
  mysql -uroot -p123456
  create database ffgorm;
  use ffgorm;
  
  cd /d/code2/hello-world/code-show/go-my/
  mkdir ff-gorm-tutorial/ && cd ff-gorm-tutorial/
  go mod init github.com/time1043/ff-gorm-tutorial
  code .
  
  go get gorm.io/driver/mysql
  go get gorm.io/gorm
  
  ```

  



### 连接

- 简单连接

  ```go
  package main
  
  import (
  	"fmt"
  
  	"gorm.io/driver/mysql"
  	"gorm.io/gorm"
  )
  
  var DB *gorm.DB
  
  func init() {
  	username := "root"   //账号
  	password := "123456" //密码
  	host := "127.0.0.1"  //数据库地址，可以是Ip或者域名
  	port := 3306         //数据库端口
  	Dbname := "ffgorm"   //数据库名
  	timeout := "10s"     //连接超时，10秒
  
  	// root:123456@tcp(127.0.0.1:3306)/ffgorm?charset=utf8mb4&parseTime=True&loc=Local&timeout=10s
  	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local&timeout=%s", username, password, host, port, Dbname, timeout)
  
  	//连接MYSQL, 获得DB类型实例，用于后面的数据库读写操作。
  	DB, err := gorm.Open(mysql.Open(dsn))
  	if err != nil {
  		panic("连接数据库失败, error=" + err.Error())
  	}
  
  	fmt.Println(DB) // &{0xc0000d0360 <nil> 0 0xc0001f4380 1}  // success
  
  }
  
  func main() {
  
  }
  
  ```

  



- 连接中的配置

  `&gorm.Config{}`

  跳过默认事务：`SkipDefaultTransaction: true`

  命令策略：`NamingStrategy: schema.NamingStrategy{}` (默认，表名是蛇形复数，字段名是蛇形单数)

  显示日志：日志等级、自定义日志的显示 (默认，只打印错误和慢SQL)

- 命令策略

  ```go
  db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{
  	SkipDefaultTransaction: true, //禁用默认事务，以便于在多个函数中使用事务
  	NamingStrategy: schema.NamingStrategy{
  		TablePrefix:   "ff_", // 表名前缀
  		SingularTable: false, // 使用单数表名/不 加s
  		NoLowerCase:   true,  // 字段不转小写/是 保留大写
  	},
  })
  ```

- 显示日志

  ```go
  // 方式1：全局加入 &gorm.Config{}
  var mysqlLogger logger.Interface
  mysqlLogger = logger.Default.LogMode(logger.Info)
  
  db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{
  	Logger: mysqlLogger,
  })
  
  
  // 方式2：部分展示日志 DB.Session()
  var model Student
  DB = DB.Session(&gorm.Session{Logger: mysqlLogger})
  session.First(&model)
  
  
  // 方式3：只想某些语句显示日志 .Debug()
  DB.Debug().AutoMigrate(&Student{}) 
  
  ```
  
  自定义日志
  
  ```go
  mysqlLogger = logger.New(
  	log.New(os.Stdout, "\r\n", log.LstdFlags), // （日志输出的目标，前缀和日志包含的内容）
  	logger.Config{
  		SlowThreshold:             time.Second, // 慢 SQL 阈值
  		LogLevel:                  logger.Info, // 日志级别
  		IgnoreRecordNotFoundError: true,        // 忽略ErrRecordNotFound（记录未找到）错误
  		Colorful:                  true,        // 使用彩色打印
  	},
  )
  ```
  
  



- 代码汇总 (逐渐废弃)

  ```go
  package main
  
  import (
  	"fmt"
  	"log"
  	"os"
  	"time"
  
  	"gorm.io/driver/mysql"
  	"gorm.io/gorm"
  	"gorm.io/gorm/logger"
  	"gorm.io/gorm/schema"
  )
  
  var DB *gorm.DB
  var mysqlLogger logger.Interface
  
  func init() {
  	username := "root"
  	password := "123456"
  	host := "127.0.0.1"
  	port := 3306
  	Dbname := "ffgorm"
  	timeout := "10s"
  
  	// mysqlLogger = logger.Default.LogMode(logger.Info)
  	mysqlLogger = logger.New(
  		log.New(os.Stdout, "\r\n", log.LstdFlags), // （日志输出的目标，前缀和日志包含的内容）
  		logger.Config{
  			SlowThreshold:             time.Second, // 慢 SQL 阈值
  			LogLevel:                  logger.Info, // 日志级别
  			IgnoreRecordNotFoundError: true,        // 忽略ErrRecordNotFound（记录未找到）错误
  			Colorful:                  true,        // 使用彩色打印
  		},
  	)
  
  	// root:123456@tcp(127.0.0.1:3306)/ffgorm?charset=utf8mb4&parseTime=True&loc=Local&timeout=10s
  	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local&timeout=%s", username, password, host, port, Dbname, timeout)
  	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{
  		SkipDefaultTransaction: true, //禁用默认事务，以便于在多个函数中使用事务
  		NamingStrategy: schema.NamingStrategy{
  			TablePrefix:   "ff_", // 表名前缀
  			SingularTable: false, // 使用单数表名/不 加s
  			NoLowerCase:   true,  // 字段不转小写/是 保留大写
  		},
  		Logger: mysqlLogger,
  	})
  	if err != nil {
  		panic("connect to database failed, error: " + err.Error())
  	}
  
  	DB = db
  	// fmt.Println(db) // &{0xc0000d0360 <nil> 0 0xc0001f4380 1}  // success
  
  }
  
  type Student struct {
  	ID   uint
  	Name string
  	Age  uint
  }
  
  func main() {
  	// DB = DB.Session(&gorm.Session{Logger: mysqlLogger})
  	DB.AutoMigrate(&Student{}) // create table if not exist
  }
  
  ```

  



### 模型定义

- 模型定义

  迁移表结构 `AutoMigrate` (只新增 不删除 不修改 但大小会修改)

  字段的数据类型 gorm标签

  ```go
  type Student struct {
  	// 小写属性是不会生成字段的
  	ID    uint    // 默认使用ID作为主键
  	Name  string  // 默认值是空字符串
  	Email *string // 使用指针是为了存空值
  }
  
  func main() {
  	DB.AutoMigrate(&Student{}) // AutoMigrate 只新增，不删除，不修改（大小会修改）
  }
  
  ```

  使用gorm的标签进行修改

  `type` 定义字段类型

  `size` 定义字段大小

  `column` 自定义列名

  `primaryKey` 将列定义为主键

  `unique` 将列定义为唯一键

  `default` 定义列的默认值

  `not null` 不可为空

  `embedded` 嵌套字段

  `embeddedPrefix` 嵌套字段前缀

  `comment` 注释

  多个标签之前用 `;` 连接

  ```go
  Name  string  `gorm:"type:varchar(12)"`
  Name  string  `gorm:"size:2"`
  ```

  Demo

  ```go
  type StudentInfo struct {
    Email  *string `gorm:"size:32"` // 使用指针是为了存空值
    Addr   string  `gorm:"column:y_addr;size:16"`
    Gender bool    `gorm:"default:true"`
  }
  type Student struct {
    Name string      `gorm:"type:varchar(12);not null;comment:用户名"`
    UUID string      `gorm:"primaryKey;unique;comment:主键"`
    Info StudentInfo `gorm:"embedded;embeddedPrefix:s_"`
  }
  
  // 建表语句
  CREATE TABLE `students` (
      `name` varchar(12) NOT NULL COMMENT '用户名',
      `uuid` varchar(191) UNIQUE COMMENT '主键',
      `s_email` varchar(32),
      `s_y_addr` varchar(16),
      `s_gender` boolean DEFAULT true,
      PRIMARY KEY (`uuid`)
  )
  
  ```

  



### 单表查询

- 创建数据

  ```go
  package main
  
  import (
  	"fmt"
  
  	"gorm.io/driver/mysql"
  	"gorm.io/gorm"
  	"gorm.io/gorm/logger"
  )
  
  var DB *gorm.DB
  
  func init() {
  	username := "root"
  	password := "123456"
  	host := "127.0.0.1"
  	port := 3306
  	Dbname := "ffgorm"
  	timeout := "10s"
  
  	// root:123456@tcp(127.0.0.1:3306)/ffgorm?charset=utf8mb4&parseTime=True&loc=Local&timeout=10s
  	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local&timeout=%s", username, password, host, port, Dbname, timeout)
  	db, err := gorm.Open(mysql.Open(dsn))
  	if err != nil {
  		panic("connect to database failed, error: " + err.Error())
  	}
  	DB = db
  }
  
  type Student struct {
  	ID     uint   `gorm:"size:3"`
  	Name   string `gorm:"size:8"`
  	Age    int    `gorm:"size:3"`
  	Gender bool
  	Email  *string `gorm:"size:32"`
  }
  
  func main() {
  	DB.AutoMigrate(&Student{})
  
  	// add 1 row
  	email := "xxx@qq.com"
  	student := Student{
  		Name:   "zhou",
  		Age:    21,
  		Gender: true,
  		Email:  &email,
  	}
  	DB.Create(&student)
  	fmt.Printf("%#v\n", student)
  
  	// add many rows
  	var studentList []Student
  	for i := 0; i < 100; i++ {
  		studentList = append(studentList, Student{
  			Name:   fmt.Sprintf("机器人%d号", i+1),
  			Age:    21,
  			Gender: true,
  			Email:  &email,
  		})
  	}
  	DB.Create(&studentList)
  }
  
  ```

- 查询数据

  ```go
  	// select 1 row
  	var student Student
  	// DB = DB.Session(&gorm.Session{
  	// 	Logger: logger.Default.LogMode(logger.Info),
  	// })
  	DB.Take(&student)    // SELECT * FROM `students` LIMIT 1
  	fmt.Println(student) // {1 zhou 21 true 0xc0001ef360}
  
  	student = Student{}  // 重新赋值
  	DB.First(&student)   // SELECT * FROM `students` ORDER BY `students`.`id` LIMIT 1
  	fmt.Println(student) // {1 zhou 21 true 0xc0001ef360}
  
  	student = Student{}  // 重新赋值
  	DB.Last(&student)    // SELECT * FROM `students` ORDER BY `students`.`id` DESC LIMIT 1
  	fmt.Println(student) // {204 zhou 21 true 0xc0001ef4c0}
  
  
  	// select by primary key
  	// Take的第二个参数，默认会根据主键查询，可以是字符串，可以是数字
  	student = Student{} // 重新赋值
  	DB.Take(&student, 2)
  	fmt.Println(student) //{2 zhou 21 true 0xc0001ef590}
  
  	student = Student{} // 重新赋值
  	DB.Take(&student, "4")
  	fmt.Println(student) // {4 机器人2号 21 true 0xc0001ef660}
  
  
  	// select where
  	// 使用？作为占位符，将查询的内容放入?
  	// 这样可以有效的防止sql注入 其原理就是将参数全部转义
  	student = Student{} // 重新赋值
  	DB.Take(&student, "Name = ?", "机器人27号")
  	fmt.Println(student) // {29 机器人27号 21 true 0xc0001ef710}
  
  
  	// 根据struct查询
  	student = Student{} // 重新赋值
  	student.ID = 22     // 只能有一个主要值
  	//student.Name = "机器人52号"
  	DB.Take(&student)
  	fmt.Println(student)
  ```

  





### 创建Hook









## 高级查询

### 





### 





## 多种关系

### 一对多关系









### 一对一关系









### 多对多关系









### 自定义数据类型







### 事务



















# Go Seminar (ByteDance)















