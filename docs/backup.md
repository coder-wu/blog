# 备份之旅 - An Interesting Story About Backup

<!-- properties
tag: 案例
created:  2024-01-17 20:47:36
-->

## 缘起 - 0

每个程序员都想有一台自己的服务器。

> Every programmer wants a personal server.

2020年，我买了一台NUC，装了一块1TB的固态硬盘和一块从老电脑上面拆下来的2015年产的1TB机械硬盘。我有一台MacBook日常使用，所以在NUC上装了Windows以备不时之需，同时在NUC上面跑一些耗时的后台任务，比如下载美剧和电影。

> In 2020, I bought a NUC, installed a 1TB SSD and a 1TB HDD produced in 2015 which was removed from an old laptop. I daily use MacBook, so I install Windows on NUC in case for need, and run some background tasks like downloading TV series and movies on it.

我还在Windows上面装了Linux虚拟机，配置了网络桥接。我在Mac上通过Microsoft Remote Desktop连接Windows，通过SSH连接到Linux虚拟机，这样我就在一块屏幕上同时拥有了MacOS、Window和Linux，完美！

> I also install a Linux VM on Windows with bridge network, so I can connect to Windows by Microsoft Remote Desktop, connect to Linux VM by ssh, and then I have MacOS、Windows、Linux on one screen, bingo!

## 着相 - 1

有了一台小机器，总想干点“有趣”的事情。

> No one can set a NUC aside at beginning.

...