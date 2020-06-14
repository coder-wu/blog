---
title: 不使用数学运算符求两整数和
date: 2017-07-10
categories: ['算法']
draft: false
---

题目来自  [lintcode A+B问题](http://www.lintcode.com/zh-cn/problem/a-b-problem/?rand=true)

**描述**

给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符。

**样例**
如果 a=1 并且 b=2，返回3

代码：

```java
	public int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        if (b == 0) {
            return a;
        }
        int XOresult = a ^ b;
        int carry = (a & b) << 1;
        return aplusb(XOresult, carry);
    }
```

注意点：

与或（^）运算符,和左移（<<）右移（>>）符号的理解和使用
