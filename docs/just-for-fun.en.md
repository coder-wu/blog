# Just For Fun

<!-- properties
language: en
tag: 案例
created:  2024-01-17 20:47:36
-->

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
