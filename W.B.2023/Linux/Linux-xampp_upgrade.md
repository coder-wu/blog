---
title: xampp集合环境安装新版本upgrade
date: 2017-09-13
categories: ['Linux']
draft: false
---

xampp是集合环境安装包，安装apache，mysql，php服务器环境。

最近想升级xampp集合安装的httpd，但是因为是集合安装所以不能单模块升级，如果重新单独安装httpd弃掉原来的，又会有vhost配置，ssl等一堆麻烦事。

如果重新安装最新版本的xampp集合环境则会造成原来的xampp中的apache配置和mysql数据库的丢失等问题，但是经过测试是可以恢复原本的apache配置和mysql数据库。

 1. 首先备份原本的安装目录/opt/lampp下的etc和var两个文件夹，如果网站根目录和ssl配置目录也在lampp安装目录下，同样进行备份。

    $ cd /opt/lampp
    $ zip -r etc.zip etc/\*
    $ zip -r var.zip var/\*
    $ mv *.zip ~/

 2. 卸载原本的lampp

    $ ./uninstall
    $ cd ..
    $ rm -rf lampp

 3. 安装新版本的lampp

 4. 还原备份的文件

    $ cd /opt/lampp
    $ mv ~/*.zip ./
    $ unzip etc.zip ./
    $ unzip var.zip ./
    $ cd var/mysql 
    $ chown -R mysql \*

    还原过程中选择替换新安装的文件，如果备份了网站根目录和ssl配置目录，还原到对应的位置。

 5. 重启服务

    $/opt/lampp/lampp restart

升级完成