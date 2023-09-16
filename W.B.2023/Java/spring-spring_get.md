---
title: Spring GET方法传参省略@RequestParam注解
date: 2018-07-12
categories: ['Spring']
draft: false
---

在形如 http://example.com/method?param=1的请求中

Spring的接收请求方法可以写做：

```java
@GetMapping("/method")
public void get(String param) {
    //param = 1
    ...
}
```

与下面的写法效果相同：

```java
@GetMapping("/method")
public void get(@RequestParam(value = "param", required = false) String value) {
   //value= 1 
   ...
}
```