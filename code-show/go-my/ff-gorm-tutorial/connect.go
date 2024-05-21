package main

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
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

}
