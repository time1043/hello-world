# Java-Scala-Kotlin

- Reference 

  



# Java Standard Edition

- overview

  Java's core apis, such as 

  collection, multithreading, network programming, input/output (I/O), database connectivity





## 基础语法











## 进阶语法

### 反射











### 工厂







# Java Enterprise Edition

- overview

  Technology Stack: `Servlet`, `JSP (JavaServer Pages)`, EJB (Enterprise JavaBeans), JMS (Java Message Service）, JTA (Java Transaction API), JPA (Java Persistence API)









### JDBC (连接数据库)





### MyBatis (持久层框架)



### Tomcat (web服务器)



### Maven (包管理工具)

- [mvn repository](https://mvnrepository.com/artifact/mysql)



### http通信





# Java Spring







# Scala (atguigu)













# Kotlin (Syntactic sugar)

- kotlin 语法糖

  kotlin：建立在jvm上的编程语言、可以与java代码无缝集成

  syntax sugar：对底层语法的一种包装、提高代码可读性和可维护性

  



- kotlin 语法精简 (Talk is cheap, show me the code)

- class的声明

  ```java
  // java
  public class Person {
      private String name;
      private int age;
      
      // Constructor
      // getters
      // setters
      // equals
      // toString
      // ...
  }
  ```

  kotlin的数据类data classes 可以自动生成常见的函数

  ```kotlin
  // kotlin
  data class Person(val name: String, val age: Int)
  ```

- 检查空指针

  ```java
  // java
  String result = null;
  if (obj != null && obj.getProperty() != null) {
      result = pbj.getProperty().toString();
  }
  ```

  ```go
  // go
  if err != nil {
      ...
  }
  ```
  
  kotlin 的 Elvis Operator (`?.`)
  
  ```kotlin
  // kotlin
  val result = obj?.property?.toString()
  ```
  
- 找出符合条件的元素

  ```java
  // java
  List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
  List<Integer> evenNumbers = new ArrayList<>();
  for (Integer number: numbers) {
      if (number % 2 == 0) {
          evenNumbers.add(number);
      }
  }
  
  // java 另一种表达
  List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
  List<Integer> evenNumbers = numbers.stream()
      							.filter(num -> num % 2 == 0)
      							.collect(Collectors.toList());
  ```

  kotlin 的 filter函数 可直接用于各种集合类型

  ```kotlin
  // kotlin
  val numbers = listOf(1, 2, 3, 4, 5)
  val evenNumbers = numbers.filter { it % 2 == 0 }
  ```

- 不同的语法实现相同的功能 (灵活)、

  ```kotlin
  val number = 10
  
  // using let 
  val result1 = number.let { it * 2 + 5 }
  
  // using run 
  val result2 = run { number * 2 + 5 }
  
  // using apply
  val result3 = number.apply { this * 2 + 5 }
  ```

- kotlin 支持spring framework

  



## 基础语法







## spring (kotlin)









