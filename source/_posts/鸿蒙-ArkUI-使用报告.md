---
title: 鸿蒙 ArkUI 使用报告
abbrlink: 49343
date: 2024-07-01 19:31:29
tags:
---

大家好啊，今天来点大家想看的东西啊。

## ArkTS 语言

[ArkTS](https://developer.huawei.com/consumer/cn/arkts/) 是鸿蒙生态的应用开发语言。它在保持 [TypeScript](https://www.typescriptlang.org/) 基本语法风格的基础上，进一步通过规范强化静态检查和分析，使得在程序运行之前的开发期能检测更多错误，提升代码健壮性，并实现更好的运行性能。同时，提供了声明式 UI 范式、状态管理支持等相应的能力，让开发者可以以更简洁、更自然的方式开发高性能应用。

官网是这样说的，但我只能呃呃。可能是华为没有那样的能力去创建一门属于自己的语言吧，最后把 TypeScript 变成了与 Swift 或者说是 Kotlin 缝合的缝合怪。一些令我厌烦的写法，如匿名函数 `.bind(this)`、模板字符串要用反引号 `` const str = `Show: ${another} value`  ``，也遗传了下来，特别是组件内引用 `state` 时也要带上 `this`，这肯定是受到语言实现的限制吧。

同样的，我不喜欢 ArkTS：

1. 必须使用 DevEco Studio 才能使用 ArkTS 语言
2. DevEco Studio 自带的代码格式化结果一坨：

   ```ts
   .toolBar({ items: [
     { value: "Plunger", icon: "house", action: () => {
     } },
     { value: "Intelligent", icon: "house", action: () => {
     } },
     { value: "Shop", icon: "house", action: () => {
     } },
     { value: "Me", icon: "house", action: () => {
     } },
   ]
   })
   ```

   真看不下去吧，这都和 Xcode 学一样？

3. 格式化风格不统一，和 Swift 一样，加几个回车和空格格式化结果就不一样了，多人协同我不敢想会是怎么样的
4. 没有热更新，但和 SwiftUI 一样提供了 `Preview` 功能——因为如果连 `Preview` 功能都没有的话，对于连模拟器都不支持的 DevEco Studio 来说，没有鸿蒙设备就别想搞鸿蒙开发了

## DevEco Studio

我去，这不是我们 Android Studio 吗，啊不对，这不是我们 IntelliJ IDEA 吗？下次发布记得标注。

其实就是没能力自研 IDE 啦，所以选择“基于 IntelliJ IDEA Community 开源版本打造”。这个选择是正确的，但结果只能说不尽人意。

首先是代码格式化的问题，这个上面讲过了，那么接下来说点别的。

插件未免太少了，因为自己最常用的代码编辑器是 VSCode 嘛——其实在我心目中这玩意可以说是和 IDE 一样的存在了——所以键位肯定也想按 VSCode 的来，在 IntelliJ IDEA 和 Android Studio 上都有 VSCode KeyMap 的插件可以从 VSCode 导入键位，但
Dev Studio 上就是没有。

难道说华为就完全没有在使用 VSCode 的吗……我去，Xcode 也没有，这下破案了。

代码补全一坨，这是做的极差的。感觉代码补全完全没有根据上下文，也就是光标目前所处的地方该填什么类型的东西、默认能填什么东西，来提示补全内容——原版 TypeScript 在 VSCode 上的代码补全可谓是反向的极端，过度依赖上下文以至于有时我想要的结果反而不在补全结果里。

本地化做的不到位，照理说这还是国内公司的软件本地化应该做的更好，但很多地方都没有翻译到——有人可能会说全英文界面更好，开发者就应该多接触英文，可，~~我不懂英文~~ 我更喜欢待在一个更熟悉的环境里啦。

## ArkUI

你们的文档也是和 Apple 学的？ArkUI、SwiftUI、Jetpack Compose 以及基于 XML 视图的 Android 文档怎么都是一个样子？

这样才有教程书的生存空间是吧。

官方入门教程里的界面也太丑了吧，还是说 Harmony Design 就是这样的？实际上，我都不知道这算不算的上 Harmony Design，因为真的很丑。

我该怎么使用图标呢？我真的得将一堆 SVG 下载下来然后再作为资源文件使用吗？鸿蒙是有自己的图标库的，能否像 Flutter 或者 SwiftUI 那样更加和 ArkTS 结合起来呢？

我看到有 `Symbol` 啦，但是一样，示例代码呢？后面是找到了示例代码，但现在要我再去找一次，那我真不知道在哪里翻出来的示例代码。

```ts
SymbolGlyph($r('sys.symbol.ohos_trash'))
  .fontWeight(FontWeight.Lighter)
  .fontSize(96);
```

```ts
Text() {
  SymbolSpan($r('sys.symbol.ohos_trash'))
    .fontWeight(FontWeight.Normal)
    .fontSize(96)
}
```

我去，我怎么没有 `SymbolGlyph` 和 `SymbolSpan`，有版本要求吗？下次记得标注。

一样没有组件 Gallery 展示 Harmony Design 的默认组件样式，别学 Apple 啊，你能做的更好的啊。

## 总结

累人。
