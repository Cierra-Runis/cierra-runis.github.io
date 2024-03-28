---
title: React Native 使用报告（二）
tags:
  - React Native
  - 使用报告
abbrlink: 56291
date: 2024-03-28 13:41:56
cover: img/React-Native-使用报告/cover.png
---

被恶心到了，我要狠狠的吐槽。

最近在恶补 React、Next.js、React Native，我先谈谈这个 React Native。

## 一、语言不行？

几个月下来，对 TypeScript 的了解更深了，能基本使用 TypeScript 了，像是它的解构，挺有趣的。自己也用 TypeScript 开发了一个 [VSCode 插件](https://github.com/Cierra-Runis/based_vscode_extension)，可以说是这个项目后才对 TypeScript 有了好感。

有关它的类型，我还是不太能看懂，特别是我想要知道一个类型到底是怎样的时候，也就是翻源码的时候，要在很多联合类型直接跳转，这挺麻烦的。而之前也谈过，Dart 很直观，没有这么绕——但我也确实想要 Dart 加入联合类型就是了。

对了，补充一点，之前说到 Java 没有空安全检查，这不太对，因为后面较新版本的 Java 有空安全，我也看到有的 Java 使用了 `@Nullable` 注释。

我不确定现在公司里都用的什么版本的 Java，不会还是 Java 8 吧？我是建议一直跟最新的，不管是语言还是框架，它们为什么要更新呢？因为它们加入了一些新东西，这些东西肯定是被好好讨论后才加入的，而被 deprecate 的那些东西，终将是会被删掉的，不升级还不行。新版本一般也会修复一些 bug、提升些性能，向后兼容的版本范围也可能变小，总之更新是好事。

但也要求这个过程是渐进的，不然出 bug 会很难受，比如说 Windows 升级，我甚至不想让它自动更新。

## 二、框架不行？

### 组件设计

这个我还是要批评的，基础组件太少，布局写起来很麻烦。

这时候我就去找组件库，找到个 [React Native Paper](https://reactnativepaper.com/) 库，用的是 [Material Design 3](https://m3.material.io/) 的设计，但也没有像 Flutter 里 `Scaffold` 的存在，凑合凑合还算过得去。

### 组件修改

样式确实可以不放在另一个文件夹里，能写内联的，在 React Native 里经常使用 `style` 属性修改，在谈 Next.js 我还会再说个 TailwindCSS。

Lint 提示确实还是不太好，有些属性名和原来的 CSS 属性名还有区别，我可不想被累死。

### 组件在多平台下的表现

这个我就不多谈了，React Native 表现挺差的，但我现在只搞 Android 这边的，随他去吧。

### Navigation 导航

我草死你的妈啊 😅，难用一匹——我现在使用的是 [@react-navigation](https://reactnavigation.org/docs/getting-started/) 这个包。

首先，我还是不喜欢命名路由，对 Flutter 来说一样。第一这意味着路由名称是硬编码的字符串，一旦重构会很麻烦；第二传参变得毫无类型可言，我该怎么判断它有没有我要的参数，我难道要每个需要传参的页面（路由、提示框）里都写 `as`？而且我如果修改了参数类型，在 `navigation.navigate` 这边是不会有任何提示的。

对了，这个 `navigate` 函数本身的类型好像有问题，不知道为什么它要求的是 `never`，而我需要传入字符串和给页面的传参，但是它也只是有个 lint 报错在那，用还是能用。

再就是这个在 Flutter 里称作 `AppBar` 的东西——谁要你自动给我每个路由里的界面都带上了？但这样我人又懵了，对哦，那我自己要写 `AppBar` 对吧，嗯，React Native Paper 里有个叫 `Appbar` 的东西，挺好的……等一下，返回按钮不是自动 implement 的，因为这两个包直接没有关系。也就是说我还要自己写一个 `AppBar` 组件，自己看看这个组件上级有没有路由，有就像 Flutter 那样自动 implement。

唯一一点好处就是，这个页面间跳转动画挺好看，因为跳转动画是 Android 自带的，因为跳转是使用了原生的。

## 三、Debug 工具不方便

对，今天开个第三节继续吐槽 React Native。

我是使用 VSCode 和 React Native Cli 进行开发的，还使用了 Microsoft 开发的一个插件。

首先恶心人的地方是启动，不能 F5 启动（或者说我不知道怎么配置），要 `ctrl + shift + p` 在面板里选择。这还行，但接下来我人晕了，VSCode 没有进入调试模式——就是底下状态条没黄，这说明它没有 VSCode debugger，这？（刚找到篇 [文章](https://blog.logrocket.com/debugging-react-native-vs-code/) 说有插件能，等我用了之后再补充）

我出错了不知道具体错误在哪，鼠标不会自动跳到出问题的代码去，

而且我这玩意不能热重启，我只能重载 VSCode 再启动——而热更新也是，很多时候我都不知道它有没有更新，特别是在出 bug 后，保持黑屏，还得自己重启。

## 四、结尾

总之写起来很累，相比较 Flutter，无论是布局、导航、编程语言、调试工具，React Native 都没有很大的优势——它最大的优势可能就是沾了 React 的光，“熟悉 Web 前端开发的技术人员只需很少的学习就可以进入移动应用开发领域”，但 React 嘛，还是让它好好搞网页开发吧，移动应用真不适合。

PS：本报告可能会有第三期。
