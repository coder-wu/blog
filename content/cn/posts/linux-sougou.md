---
title: Ubuntu16.04解决fcitx搜狗中文输入法在一些软件中无法使用
date: 2016-09-08
categories: ['Linux']
draft: false
---

有些时候Ubuntu的搜狗输入法在一些软件中无法调出使用

解决方法：

测试可用

1.杀死fcitx重新启动

$ sudo killall fcitx

$ fcitx

2.启动搜狗输入法

$ sogou-qimpanel

执行命令时若遇到错误提醒，长时间停顿可ctrl+c退出执行下一条命令，最后也能解决问题。

