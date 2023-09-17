# SimpleDateFormat线程安全性

<!-- properties
tag: 案例
tag: 线程
created: 2023-09-17 09:40:06
-->

## 0

### 结论

**SimpleDateFormat是线程不安全的。**

在JDK中关于SimpleDateFormat有这样一段描述：

> Date formats are not synchronized.
  It is recommended to create separate format instances for each thread.
  If multiple threads access a format concurrently, it must be synchronized
  externally.
  @apiNote Consider using {@link java.time.format.DateTimeFormatter} as an
  immutable and thread-safe alternative.

### 原因

SimpleDateFormat通过父类DateFormat中的calendar对象变量保存要格式化的时间，calendar定义代码：

``` java
protected Calendar calendar;
```

calendar的定义和SimpleDateFormat使用calendar变量都没有考虑线程安全。

## 验证

### 代码

``` java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.CountDownLatch;

public class SimpleDateFormatTest {
    private static final DateFormat STATIC_DATE_FORMAT = new SimpleDateFormat("yyyyMMdd");

    private static final Date NOW = new Date();

    private static final Date TOMORROW = new Date(NOW.getTime() + 24 * 3600 * 1000);

    private static final Set<String> NOW_RESULT = new HashSet<>();

    private static final Set<String> TOMORROW_RESULT = new HashSet<>();

    private static final int THREAD_COUNT = 10;

    private static final CountDownLatch COUNT_DOWN_LATCH = new CountDownLatch(THREAD_COUNT);

    public static void main(String[] args) throws InterruptedException {
        for (int i = 0; i < THREAD_COUNT; i++) {
            new Thread(SimpleDateFormatTest::run).start();
        }

        COUNT_DOWN_LATCH.await();

        System.out.println(NOW_RESULT);
        System.out.println(TOMORROW_RESULT);
    }

    private static void run() {
        for (int i = 0; i < 100; i++) {
            NOW_RESULT.add(STATIC_DATE_FORMAT.format(NOW));
            TOMORROW_RESULT.add(STATIC_DATE_FORMAT.format(TOMORROW));
        }
        COUNT_DOWN_LATCH.countDown();
    }
}

```

### 输出

``` txt 
[20230916, 20230917]
[20230916, 20230917]
```

### 结果说明

```NOW_RESULT```应该只有当天的日期字符串，```TOMORROW_RESULT```应该只有第二天的日期字符串，但结果是这两个Set中既包含当天又包含第二天的字符串。

```STATIC_DATE_FORMAT```作为static变量，在所有的线程中共享，导致不同线程设置的时间错乱，结果不准确。