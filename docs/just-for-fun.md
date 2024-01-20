# 瞎折腾

[EN](#just-for-fun)

> [Homelab](https://github.com/coder-wu/homelab)的正统README

<!-- properties
tag: 案例
created:  2024-01-17 20:47:36
-->

## 起高楼

每个程序员都想有一台自己的服务器。

2020年，我买了一台NUC，装了一块1TB的固态硬盘和一块从老电脑上面拆下来的2015年产的1TB机械硬盘。我有一台MacBook日常使用，所以在NUC上装了Windows以备不时之需（🎮 打游戏），同时在NUC上面跑一些耗时的后台任务，比如下载美剧和电影。

我还在Windows上面装了Linux虚拟机，配置了网络桥接。我在Mac上通过Microsoft Remote Desktop连接Windows，通过SSH连接到Linux虚拟机，这样我就在一块屏幕上同时拥有了MacOS、Windows和Linux，完美！

## 宴宾客

有了一台小机器，总想干点“有趣”的事情。

### Xray

第一件“有趣”的事是把xray跑在linux上作为局域网的统一代理，**这样就不用在每台设备都装xray客户端**，为此写了Homelab中ray的脚本。当时计划通过定时任务检测网络状态；更新路由数据；在异常时主动更新订阅并重启xray，所以xray的脚本中会有更新GEO数据、查询订阅信息和检测网络状态这几个看似鸡肋的功能。

### 备份

备份，不是NAS。

因为一开始的想法就是给Mac上的文件做备份，所以要求安全和方便操作，安全就是备份的文件需要加密，方便操作意味着不用经常手动触发，如果是手动触发要尽可能简单，再有就是备份要是增量备份。

我在NUC上分出来一块硬盘，用BitLocker加密解决了安全的问题。

备份选择了syncthing，在Windows和Mac上装好后，配置从Mac到Windows的路由规则。

至此一切都很平稳，挖了两个坑之后，开始挖下一个坑：容器。

### 容器

我在Windows上分出来两台虚拟机，打算在Mac上再开一个虚拟机配合安装一个小型的高可用K8S集群。

我的Linux是跑在Windows和Mac上的虚拟机，此时从裸金属到容器的路径是：HardWare -> Windows/Mac -> Linux VM -> Container，4层。

如果在裸金属上直接安装Linux作为宿主机，再在宿主机上运行容器，路径是：HardWare -> Host OS -> Container，3层。

在实际的公有云和私有云场景中，I层的资源又被进一步抽象，此时从裸金属到容器的路径可能是：
 - Type1虚拟化：HardWare -> Hypervisor -> Linux VM -> Container，4层。
 - Type2虚拟化：HardWare -> Host OS -> Hypervisor -> Linux VM -> Container，5层。

一层层地抽象虚拟下来显得不那么“利索”。

如果是纯容器场景，Linux VM采用像RedHat、Suse之类的Linux发行版显得有点大材小用，最后选择了CoreOS作为容器的宿主机OS。

> 云厂商提供的裸金属容器，至今没有搞明白是什么样的架构，怎么实现在裸金属上面直接跑容器。

跟着K8S的官方指导，尝试了安装高可用集群。不过MacOS上的虚拟机桥接无线网无法访问外部网络，最后是通过三台运行在Windows上的Linux VM搭建起来的。

利用周末和平常下班之后的时间，整个安装流程耗时大概半个月，集群安装完成之后尝试配置运行了Prometheus，至此，这个集群就**完了**。

## 楼塌了

996之下，如果没有需要长时间占用网络、CPU和GPU计算的后台任务，一直开着NUC并不划算。

**不用在每台设备都装xray客户端是个伪需求**，如果出门在外或者设备换了个网络，还是要运行客户端。

NUC不一直运行，就需要隔段时间启动NUC，解锁BitLocker，启动syncthing备份。那还不如直接把硬盘通过smb挂载使用```rsync```备份。 不如？？

作为学习和实践，在安装高可用K8S集群过程中学到了不少关于Infra、OpenStack、MAAS（Canonical）、K8S、ETCD的知识，作为补充阅读开扩眼界。作为开发环境，我拒绝使用！三个虚拟机搭建的集群运行性能堪忧，维护麻烦。环境是为开发服务的，不是供养的。

## 尘归尘

ray的脚本可以直接拿来用在Mac上，一键启动重启，免去找各种客户端，**省心，不折腾**。

买个硬盘盒，买两块机械硬盘，**TimeMachine好用，不折腾**。

**Minikube好用，不折腾**。

---

# Just For Fun

> Real README for [Homelab](https://github.com/coder-wu/homelab)

## 0

Every programmer wants a personal server.

In 2020, I bought a NUC, installed a 1TB SSD and a 1TB HDD produced in 2015 which was removed from an old laptop. I daily use MacBook, so I install Windows on NUC in case for need(🎮 play games), and run some background tasks like downloading TV series and movies on it.

I also install a Linux VM on Windows with bridge network, so I can connect to Windows by Microsoft Remote Desktop, connect to Linux VM by ssh, and then I have MacOS、Windows、Linux on one screen, bingo!

## 1

No one can set a NUC aside, it has to run something.

### Xray

The first "interesting" thing is to run xray on Linux as a unified proxy for the local area network, **so that I don't need to install the xray client on each device**. For this purpose, I wrote a script for xray in homelab repository. It was planned to provide capabilities like checking the network status, updating routing data, refreshing subscription and restart xray automatically in case of subscription is changed. Therefore, the xray script includes functions such as updating GEO data, querying subscription information, and monitoring network status.

### Back up

Back up, not NAS.

Because I just want to back up files on Mac, so it requires security and easy operation. Security means that the backed up files need to be encrypted. Easy operation means that there is no need to manually trigger it frequently. If it is manually triggered, it should be as simple as possible, the backup must be an incremental backup.

I prepared a disk partition on NUC and used BitLocker encryption to solve the security problem.

I used syncthing for backup, installed it on Windows and Mac, then configured back up rules from Mac to Windows.

So far everything was going well. I started a new way: container.

### Container

I created two VM on Windows and another VM on Mac to install a small high available K8S cluster.

VM is running on Windows and Mac. In this way, the path from bare metal to container is: HardWare -> Windows/Mac -> Linux VM -> Container, 4 layers.

If Linux is directly installed on bare metal as the host, and then run the container on the host, the path is: HardWare -> Host OS -> Container, 3 layers.

In actual public cloud and private cloud scenarios, the resources of infra layer are further abstracted. In this way, the path from bare metal to containers may be:

  - Type 1 hypervisor: HardWare -> Hypervisor -> Linux VM -> Container, 4 layers.
  - Type 2 hypervisor: HardWare -> Host OS -> Hypervisor -> Linux VM -> Container, 5 layers.

The abstraction and virtualization layer by layer does not seem so "clean".

If it is a pure container scenario, it seems a bit overkill to use Linux distributions such as RedHat and Suse for Linux VM. In the end, CoreOS was chosen as the host OS for the container.

> Cloud services provide bare metal containers, but I still don’t understand what kind of architecture it is and how to run containers directly on bare metal.

Following the official guidance of K8S, I tried to install a high available cluster. However, the VM on MacOS with bridge network on wireless cannot access the external network, and it was finally built through three Linux VMs running on Windows.

The entire installation process took about half a month using weekends and time off work. After the cluster installation was completed, I tried to configure and run Prometheus, then this cluster was ```finished```.

## 2

Under 996, if there are no tasks that require network, CPU and GPU for a long time, it is not a good idea to keep the NUC running.

It is't a effective requirement not to install the xray client on every device. If I am away from home or the device changes network, I still need to run the client.

If the NUC does not run all the time, I need to periodically start NUC, unlock BitLocker, and start syncthing. It is better to mount the disk directly through smb and use ```rsync``` backup. Is it better? ?

As a way of learning and practice, I learned a lot about Infra, OpenStack, MAAS (Canonical), K8S, and ETCD during installing high available K8S cluster, which broaden my horizons. As a development environment, I refuse to use it! The cluster built by the three VMs has poor performance and is troublesome to maintain. The environment serves development, not being served.

## Ashes to ashes

The ray script can be used directly on Mac. Xray can be started and restarted with one click, I don't need to find Xray clients. **It is easy to use**.

Buy a hard drive box and two HDDs. **TimeMachine is easy to use**.

**Minikube is easy to use**.
