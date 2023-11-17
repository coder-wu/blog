# 反面单例

<!-- properties
tag: 案例
tag: Java
created: 2023-11-17 22:20:49
-->

## 代码

```java
import java.util.ArrayList;
import java.util.List;

/**
 * @author : coderWu
 * @since : 2023/11/17
 **/
public class StupidSingleton {
    private static final StupidSingleton instance = new StupidSingleton();

    private static List<String> list = null;

    private static Object object = null;

    private StupidSingleton() {
        list = new ArrayList<>();
        object = new Object();
    }

    public synchronized static StupidSingleton getInstance() {
        if (object == null) {
            object = new Object();
        }
        return instance;
    }

    public void doSomething() {
        list.add("Stupid");
    }
}
```

## 问题点解析

### doSomething抛出空指针异常

Java中字段、代码块、构造函数初始化顺序是：
  1. 按照**在代码中的定义顺序**依次加载static变量和static代码块。
  2. 按照**在代码中的定义顺序**依次加载实例变量和实例代码块。
  3. 构造函数。

代入这段代码中顺序为:
  1. 初始化instance = **new StupidSingleton()**
  2. 执行构造函数
  3. 初始化list = null
  4. 初始化object = null

虽然result和object都在构造函数中初始化了，但是随后又被赋值为null。

### 多线程下效率低

估计后来的修改者发现了object为空的问题，所以在getInstance中又做了初始化，这样一来，多线程下就有问题，在getInstance上加个synchronized就好了。

getInstance是static的，这个时候配合synchronized锁的就是StupidSingleton.class，多线程下效率必然低。

## 修改方案

1. 把instance的初始化放在所有static变量定义的最后或者在静态变量定义时直接初始化，不在构造函数中初始化。
2. 删除getInstance的synchronized。
3. 删除getInstance中对object的控制判断和初始化。

