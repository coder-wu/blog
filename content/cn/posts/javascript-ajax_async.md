---
title: 异步请求保存返回结果，异步同步的区别
date: 2017-03-18
categories: ['JavaScript']
draft: false
---

默认状态下ajax异步请求的async参数为true，也就是异步操作，此时获取到的返回数据只能在回调函数（success，complete）中使用，回调函数结束则返回数据被销毁。

如下代码:

```javascript
    var result = 0;
    $.ajax({
        url : "url",
        type : "POST",
        data : {},
        datatype : "json",
        success : function (data) {
            result = data;
        },
    });
```

虽然在success的回调函数中把data赋值给result，但ajax结束，result还是0，result只是在success函数中暂时等于data。

解决方法：

在ajax请求中吧async设置为false，即改为同步，如下：

```javascript
    $.ajax({
        url : "url",
        type : "POST",
        data : {},
        datatype : "json",
        async : false,
        success : function (data) {
        result = data;
        },
    });
```

有关js异步和的同步一点解释：

在异步操作时，ajax和其他js代码同时执行，而异步操作时，ajax之外的js代码进入一种假死状态，不再运行，等到ajax请求完成其他的js代码复活继续执行。