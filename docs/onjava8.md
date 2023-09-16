# On Java 8

<!-- properties
tag: Java
tag: 读书笔记 
created: 2023/05/10 20:51:09
-->

## OOP

- 在“问题空间”（问题实际存在的地方）的元素与“方案空间”（对实际问题进行建模的地方，如计算机）的元素之间建立理想的“一对一”的映射关系。

- Java不需要sizeof()方法获取数据项被分配的字节大小，因为所有类型的大小在不同平台上是相同的。 —— Java本身就是一种“与平台无关”的语言。

## Operators

- 移位运算符 `>>` 有“正”、“负”值：若值为正，则在高位插入 0；若值为负，则在高位插入 1。

- Java也添加了一种“不分正负”的移位运算符（>>>），它使用了“零扩展”（zero extension）：无论正负，都在高位插入0。

## Control Flow

- case语句能够堆叠在一起，为一段代码形成多重匹配，即只要符合多种条件中的一种，就执行那段特别的代码，如下写法：

```java
Random rand = new Random(47);
for(int i = 0; i < 100; i++) {
  int c = rand.nextInt(26) + 'a';
  System.out.print((char)c + ", " + c + ": ");
  switch(c) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u': System.out.println("vowel");
              break;
    case 'y':
    case 'w': System.out.println("Sometimes vowel");
              break;
    default:  System.out.println("consonant");
  }
}
```

## Class & Abstract Class & Interface

- 如果不需要内部类对象与其外部类对象之间有联系，那么可以将内部类声明为static，这通常称为嵌套类。想要理解static应用于内部类时的含义，就必须记住，普通的内部类对象隐式地保存了一个引用，指向创建它的外部类对象。然而，当内部类是static的时，就不是这样了。嵌套类意味着:
  - 1. 要创建嵌套类的对象，并不需要其外部类的对象。
  - 2. 不能从嵌套类的对象中访问非静态的外部类对象。

- static方法中不会存在this。不能在静态方法中调用非静态方法（反之可以）。

- 可变参数列表会被转变为数组。

- 可变参数列表不依赖于自动装箱，而使用的是基本类型。

- 带参数的构造函数：对基类构造函数的调用必须是派生类构造函数中的第一个操作。如果你写错了，编译器会提醒你。

- 无参构造函数：默认从基类 “向外” 调用无参构造函数，如果没有无参构造函数，编译器也会为你合成一个无参数构造函数，调用基类构造函数。

- 有可能的话，尽量不要调用类中的任何方法。在基类的构造器中能安全调用的只有基类的final方法(这也适用于可被看作是final的private方法)。

- 接口的典型使用是代表一个类的类型或一个形容词，如Runnable或Serializable，而抽象类通常是类层次结构的一部分或一件事物的类型，如String或 ActionHero。

- 为什么接口中的字段是static final的？final确保了不变性，static确保了所有接口公用。

- 内部类只能通过外部类的具体对象创建。


### Override

- private方法默认带有final属性，无法被重写，如果加上@Override会在编译期报错。

- 属性与静态方法不存在多态和Override，只和运行时类型有关。

- Java5中引入了协变返回类型，这表示派生类的被重写方法可以返回基类方法返回类型的派生类型。

### Overload

- 为什么不能根据返回值重载：调用一个方法且忽略返回值，Java 编译器就不知道你想调用哪个方法。

## Access Control

- protected也提供包访问权限

- final
  - 防止子类通过覆写改变方法的行为。
  - 在早期的Java实现中，如果将一个方法指明为final，就是同意编译器把对该方法的调用转化为内嵌调用。

- 类的访问权限可以是package或者public，但是内部类可以是private或者protected的。

## Functional & Lambda

- OO(object oriented，面向对象)是抽象数据，FP(functional programming，函数式编程)是抽象行为。

- “不可变对象和无副作用” 范式，函数式语言作为并行编程的解决方案。