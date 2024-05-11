# design mode

- Reference - note

  [chen note](https://znunwm.top/archives/gong-chang-mo-shi), 





# design mode (chen)

## 工厂模式

- 核心本质

  实例化对象不使用new，用工厂方法创建对象

  使用工厂统一管理对象的创建，将调用者跟实现类解耦

  



- 三种模式

- `简单工厂模式`：建立一个工厂类，对实现了同一接口的一些类进行实例的创建。

  优点是比较好理解，简单易操作。

  缺点是类的创建依赖工厂类，如果想要拓展程序，必须对工厂类进行修改，这违反了设计模式的开闭原则（OCP），即对扩展开放，对修改关闭。

- `工厂方法模式`：对简单工厂模式的改进，使用一个工厂接口，创建多个工厂类，每个工厂创建对应的对象。

  工厂方法模式，创建一个工厂接口和创建多个工厂实现类，一旦需要增加新的功能，直接增加新的工厂类就可以了，不需要修改之前的代码。有利于代码的维护和扩展。

- `抽象工厂模式`：围绕一个超级工厂创建其他工厂，每个工厂可以生产不同类型的产品

  抽象工厂模式可以将简单工厂模式和工厂方法模式进行整合。

  从设计层面看，抽象工厂模式就是对简单工厂模式的改进(或者称为进一步的抽象)。

  将工厂抽象成两层，抽象工厂 和 具体实现的工厂子类。程序员可以根据创建对象类型使用对应的工厂子类。这样将单个的简单工厂类变成了工厂集合， 更利于代码的维护和扩展。





- show me the code

- 简单工厂模式

  ```java
  /**
  * 手机接口类
  */
  public interface Phone {
      public void call();
  }
  
  
  /**
  * 两个手机实现类
  */
  public class IPhone implements Phone{
      @Override
      public void call() {
          System.out.println("用苹果手机打电话！");
      }
  }
  
  public class MPhone implements Phone{
      @Override
      public void call() {
          System.out.println("用小米手机打电话！");
      }
  }
  
  
  /**
  * 生产手机的工厂类
  */
  public class PhoneFactory {
      public Phone create(String type){
          if (type.equals("IPhone")){
              return new IPhone();
          }else if (type.equals("MPhone")){
              return new MPhone();
          }else
              return null;
      }
  }
  
  
  /**
  * 测试类
  */
  public class Test {
  
      public static final String IPhone = "IPhone";
  
      public static final String MPhone = "MPhone";
  
      public static void main(String[] args) {
          // 生产小米手机
          PhoneFactory factory1 = new PhoneFactory();
          factory1.create(MPhone).call();
  
          // 生产苹果手机
          PhoneFactory factory2 = new PhoneFactory();
          factory2.create(IPhone).call();
      }
  }
  
  
  
  ```

  



















