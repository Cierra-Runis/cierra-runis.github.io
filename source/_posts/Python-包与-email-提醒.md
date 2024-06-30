---
title: Python 包与 email 提醒
tags:
  - python
  - email
  - 编程
abbrlink: 11399
date: 2023-01-08 13:50:21
---

## 缘起

在使用 `python` 写监听器的时候经常使用邮件提醒监听器变化，一开始就是简单一句话提醒就行，后面想着这玩意应该能和自己以前收到的邮件一样好看，所以开始试着发送 `html` 格式而不是纯文本的邮件，经过一番折腾，最后搞出来了个 `python` 包 [listener_email](https://github.com/Cierra-Runis/listener_email) 。

## 问题

参考了苹果购物详情邮件：

![Alt text](/img/Python-包与-email-提醒/image.png)

可是在修改过程中发现各个平台显示出的结果都不一样，其中：

- `QQ` 邮箱网页版支持最好，能不使用 `<table>` `<tbody>` `<tr>` `<td>` 等标签，而是普通的 `<div>` 和 `css` 里的 `display: flex` 属性进行布局，其他的邮箱都不可以；能使用 `github.com` 域名下的图片，而不是非要使用 `raw.githubusercontent.com` 域名下的图片，其他的邮箱都不可以；唯一的缺点是没有暗色模式
- `iPad` 版 `Gmail` 只能使用 `<table>` `<tr>` `<td>` 等标签进行布局，使用 `<tbody>` 标签 `Gmail` 会把里面的东西掏出来，从而破坏布局，且不支持自定义字体
- 网页版 `Gmail` 同上，但背景强制显示为白色，即便开启了暗色模式
- `iPad` 自带 `邮件` 同上，同时在 `系统设置 > 邮件 > 隐私保护` 里的 `保护“邮件”活动` 若未关闭，且下方 `阻止所有远程内容` 未关闭，则默认不能查看图片
- `QQ` 手机版 `QQ 邮箱提醒` 里的邮件不支持自定义字体，且若在 `QQ 侧拉栏设置 > 通用 > 模式选择` 里选择 `体验模式` ，则背景强制显示为白色，反之选择 `普通模式` 则背景在夜间模式下能显示为黑色
- `微信` 手机版 `QQ 邮箱提醒` 里的邮件最差劲，不会自动识别邮箱为链接，不支持自定义字体，链接颜色会被一致改为蓝色，整个页面根本没做暗色模式，连上面 `发件人` 的样式都丑的一批，鉴定为 `“小而美”`

排查了好久才总结出以上信息，最后才写出来一个较为满意的 `html` ，想着这东西可以写成个包方便使用，也就开始了写包历程。

## Python 包

答案是国内资源太少，姑且把包 [listener_email](https://github.com/Cierra-Runis/listener_email) 上传使用了。

但我想着一般包都是 `import listener_email` 然后 `listener_email.sent_email()` 来使用函数，而不是 `from listener_email import sent_email, ListenerEmail` 然后 `sent_email()` 来使用函数……

不懂，暂且懒了——
