---
title: CentOS升级python2.*到python3.*后yum无法使用
date: 2017-01-28
categories: ['Linux']
draft: false
---

把服务器的python从2.\*升级到3.\*版本之后使用yum命令提示：

**File "/usr/bin/yum", line 30
    except KeyboardInterrupt, e:
SyntaxError: invalid syntax**

解决方案：

检测默认的python版本

$ python -V

如果是python 3.\*

$ whereis python

检测是否有2.\*版本的python,没有安装2.\*版本的python

之后：

\# vim /usr/bin/yum

第一行是：

#!/usr/bin/python  

修改为：

#!/usr/bin/python2.\* 

这里的版本号与whereis python 显示的python2.\*版本号相同

保存退出，可以正常使用yum命令