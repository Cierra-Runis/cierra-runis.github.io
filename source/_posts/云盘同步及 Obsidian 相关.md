---
title: 云盘同步及 Obsidian 相关
tags:
  - markdown
  - Obsidian
  - iCloud
  - GoogleDrive
  - OneDrive
  - MaterialFiles
  - FolderSync
  - 笔记
abbrlink: 2308
date: 2023-01-02 23:58:49
cover: img/云盘同步及-Obsidian-相关/cover.png
---

之前在某个直播间看到有人在用一个看起来又是很新的玩意写 `markdown` 于是非常好奇的下载了 `Obsidian` ，在看到官方的同步价格贵的一批之后在直播间里进行吐槽获得了能自搭同步的情报，于是进行一个 `iCloud` 的利用～

## iCloud 与 Obsidian

具体来说，苹果官方在 `Windows` 端推出了个 [云盘同步工具](https://www.microsoft.com/store/productId/9PKTQ5699M62) ，安装登陆后就能在电脑上看到已和 `iPad` 文件管理器中同步了的 `iCloud 云盘` 一项，在 `iPad` 端的 `Obsidian` 软件里选择在 `iCloud` 创建仓库后，便能在 `iCloud 云盘` 里看到 `Obsidian` 文件夹，进行软件配置、文件创建、修改、删除都会很快同步，当然 `iCloud` 有时抽风给你在那把文件“高高挂起”也不是不可能 😡

个人觉得每月给 `iCloud` 交的 `6` 块钱特别的值，便宜好用就是值——于是这同步空间可不能浪费，把自己原先囤积在电脑上的图片、音乐、文件都传了上来，算是减轻了因装了很多开发工具而臃肿不堪的电脑的压力。

哦，原先想着自己的一些“私密文件”也传上来方便些，但因为 **举头三尺有神明** ，铁拳还是有可能砸到云上贵州的，所以转向了其他云盘。

## Google Drive

`Google Drive` 因为一些懂得都懂的原因，是不能直接访问的，那么这里就可以很好保存“私密文件”。毕竟自己鉴赏这些东西时，也会同时使用技术手段进行一个维基百科的查、用 `iPad` 里特别好的 `GoodNotes` 进行一个笔记的做，也就给 `GoodNotes` 的备份网盘设定成了 `Google Drive` ～

## OneDrive 与 MaterialFiles 和 FolderSync

前面主要还是关注 `iPad` 和 `Windows` 之间的文件同步，但很明显 `Android` 阵营也有话说。

自己有在玩 `osu!` ，它有官方 `stable` 版、 `lazer` 版， [MATRIX-夜翎](https://space.bilibili.com/305637715) 从 `lazer` 版 `fork` 出来所维护的 `mfosu` 版，[摆烂好久都不更新](https://github.com/osudroid/osu-droid) 再这样下去什么时候我自己 `fork` 一个来更新的 `osu!droid` 版，其中我玩的是 `Windows` 上的 `stable` 版和 `Android` 上的 `osu!droid` 版。它们很好的一点就是文件层次是互通的，简单同步俩者的 `Songs` 文件夹即可。

可就是这么简单的方案实现起来也很累人。

首先需要选择同步云盘，因为 `iCloud` 没有支持安卓，且 `Google Drive` 需要那样的技术手段，便考虑别的方法。

在这里其实有另一套方案，这里我没有继续下去的原因就是有点晕人，再就是速度有点慢，但姑且也作一个记录。在 `bilibili` 里也能看见有介绍 `Syncthing` 这款软件的视频，特点是 `P2P` 安全迅速（存疑），设定双设备相互加对方好友并都设置目标文件夹后，只要连接成功就会开始同步，只可惜我这边连接不稳定——仔细想想这也并不是很符合我的使用场景，这要求俩者都在线且成功连接，所以也就放弃了。

兜兜转转还得是微软的 `OneDrive` ，在 `cmd` 使用 `mklink /d "D:\OneDrive\Songs" "D:\osu\Songs"` 创建链接使 `D:\OneDrive` 这个我个人设定的 `OneDrive` 文件夹（默认在哪来着不记得了）里出现一个 `Songs` 文件夹，进去一看好家伙是 `D:\osu\Songs` 里的东西，这样 `Windows` 方面成功。

问题出在 `Android` 方面，这边比 `iCloud` 不能自选任意文件夹同步更屑，连在文件管理器里都不显示——

> 这里需点明的是不同安卓手机的文件管理器不一样，但自 `Android 13` 开始都是用底层的文件管理器才能打开 `data` 文件夹，在这个底层文件管理器里能看到 `OneDrive` 网盘，但也没什么用，没法管任意文件夹。

经过一系列的搜索，这里推荐 `MaterialFiles` 作文件管理器， `FolderSync` 作文件同步管理器。

[前者](https://github.com/zhanghai/MaterialFiles) 是特别简洁的一款使用 `Material Design` 风格的文件管理器，其几大特点分别是：

- 能直接访问 `data` 文件夹
- 能使用 `FTP` 远程访问
- 安装包体积小至 `8 MB` ，占用不超 `20 MB`

简而言之非常好用～

[后者](https://play.google.com/store/apps/details?id=dk.tacit.android.foldersync.lite) 则是能自选任意文件夹和超多同步云盘服务的文件同步管理器，具体的不介绍了，创建“文件夹对”进行文件同步即可——虽然我文件快两万个同步起来确实有些吃力就是了。

## 总结

苹果的东西在它自家用起来是很方便的，安卓的好处是自定义程度很高～什么 `Windows` ？再好不过啦！
