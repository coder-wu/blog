
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

``` txt 
[20230916, 20230917]
[20230916, 20230917]
```