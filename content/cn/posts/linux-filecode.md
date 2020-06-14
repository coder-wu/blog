---
title: Ubuntu16.04系统中下载的中文文件名乱码解决办法
date: 2016-09-12
categories: ['Linux']
draft: false
---

乱码类似这样的：╫╩┴╧╖┤╤▌▓т╒╛╦┘╢╚│

因为zip文件对文件名的编码默认为当前环境的locale，所以在windows下压缩的zip文件，在linux下解压便会乱码。

在解压时，加上一个参数-O

unzip -O CP936 filename.zip