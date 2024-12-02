---
title: SSH
abbrlink: 22
tags: 分享
---

## 奔向命令行

大家第一次使用命令行或见到终端是什么时候呢？大多是第一次编写 C 语言程序吧。

我是小学用 `bat` 文件开 Minecraft 服务器时接触的，当时就想这个界面可真丑，黑咕隆咚的——现在不一样了，尽情美化喵。

终端是那个展示 shell 的窗口，而 shell 的话，Windows 有 `cmd`、`PowerShell`、`Windows PowerShell`，macOS、Linux 有 `bash`，Android 可以使用 [Termux](https://github.com/termux/termux-app)，也相当于是 Linux 了——有关 Termux 的配置详见 [Termux 高级终端安装使用配置教程](https://www.sqlsec.com/2018/05/termux.html)。

macOS 和 Linux 的关系更近，总之都能使用 `zsh` 而不是 `bash` 作为 shell，有关 `zsh` 的配置参见 [这篇文章](https://www.mintimate.cn/2021/02/05/configZsh)。

`zsh` 相比 `bash` 能提供命令行历史补全的功能，在 Windows 上，这需要下载 [PowerToys](https://github.com/microsoft/PowerToys) 并启用里面的 `未找到命令` 功能——看起来命令行补全是 `PowerShell` 的功能，但总之这样配置之后就没问题。

在 macOS 上，自带的终端并没有那么“好看”，总之转用了 [iTerm2](https://iterm2.com)，相关的配置略。

## 奔向 SSH

在购入了 Mac mini 后，除了写 SwiftUI 外，也想用 Mac mini 做些别的什么——我是用不来 macOS，操作逻辑相比 Windows 总是有太多别扭的地方，我是应该还会把 Windows 作为主要的开发环境的。

于是看视频，了解到 Mac mini 可以作为软路由、NAS、服务器……诶，服务器。

正好最近在玩 Minecraft，而 Mac mini 完全适合 Minecraft 开服——其实就是我想试试看，总之能分担一下我这台 Windows 笔记本的压力吧，让 Mac mini 专心逻辑处理，Windows 笔记本专心渲染。

这就牵扯到远程操作了——这其实不算“远程”，只在内网操作嘛，但——我曾经发病莫名其妙的购买阿里云的服务器，完全不了解自己为什么要用、该怎么去用服务器，总之我确实对 SSH 连接这一步有印象。

具体开启 SSH 的流程就不在此赘述了，现在再来谈个别的事。

SSH 支持免密登录，总之使用 GPG 的非对称加密——我其实对椭圆曲线的数学性质特别感兴趣，但目前找到的一些资料都是用到了抽象代数的方法的那种，没有传统解析几何的那种解释。

> 加密：公钥加密，私钥解密
> 公钥公开，任何公钥持有者都可以将想要发送给私钥持有者的信息进行加密后发送，这个信息只有私钥持有者能解密。
>
> 签名：私钥加密，公钥解密
> 公钥公开，任何持有公钥的人都能解密私钥加密过的密文，这个过程并不能保证消息的安全性，但是它却能保证消息来源的准确性和不可否认性，也就是说，如果使用公钥能正常解密某一个密文，那么就能证明这段密文一定是由私钥持有者发布的，而不是其他第三方发布的，并且私钥持有者不能否认他曾经发布过该消息。

## 奔向 PowerShell

配置好 Windows 和 macOS 上的 SSH 服务后，成功使用 Windows 远程连接到 macOS，相对应的，macOS 也可以远程连接到 Windows，但是远程连接后默认进入的 shell 居然是 `cmd`，这个实在是有点搞笑了。

[SSH 连接 Windows 默认启用 PowerShell](https://learn.microsoft.com/zh-cn/windows-server/administration/OpenSSH/openssh-server-configuration#configuring-the-default-shell-for-openssh-in-windows)

[WSL 默认目录](https://whlit.github.io/linux/wsl-default-dir.html)

如上配置好后，尽情使用 SSH 带来的便利吧。

## BUG

是的，从 Windows 访问 macOS 使用 `ls/ll` 命令列出含有中文文件的文件夹内容时，会有如下的乱码：

```bash
➜  mods git:(main) ✗ ll
total 80440
-rw-r--r--  1 cierra_runis  staff   2.0M Oct 28 04:33 ???Fabric API???fabric-api-0.92.2+1.20.1.jar
-rw-r--r--  1 cierra_runis  staff   6.3M Oct 28 04:50 ???Kotlin ?????????fabric-language-kotlin-1.9.5+kotlin.1.8.22.jar
-rw-r--r--  1 cierra_runis  staff   533K Oct 28 05:15 ???Masa ????????????malilib-fabric-1.20.1-0.16.3.jar
...
```

答案是去 `.zsh_rc` 里取消如下的注释，使 `LANG` 得以固定为 `en_US.UTF-8`：

```bash
# You may need to manually set your language environment
export LANG=en_US.UTF-8
```
