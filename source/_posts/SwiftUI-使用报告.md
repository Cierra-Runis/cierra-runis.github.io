---
title: SwiftUI 使用报告
abbrlink: 4691
date: 2024-05-25 22:56:46
tags:
---

## Swift 语言

[Swift](https://developer.apple.com/swift/) 是 [Apple ](https://www.apple.com/) 开发的一门编程语言——不像 [某为](https://www.huawei.com/) 什么 [ArkTS 语言](https://developer.huawei.com/consumer/cn/arkts/) 就是给 [TypeScript](https://www.typescriptlang.org/) 套皮——用的范围也很小，就它自家的产品开发用。

Swift 和 [Kotlin](https://kotlinlang.org/) 非常相似，创新了一些比较奇妙的语法比如：

```dart
callFunction(parma1, (value) {
  final value2 = value * 2;
  print(value2);
});
```

这种最后一个参数是函数时，可以写作：

```swift
callFunction(parma1) { value in
  let value2 = value * 2
  print(value2)
}
```

你说代码好看了嘛是好看了，但代码格式化时不会自动格式化到这种好看的格式，要写这种格式代码补全又不给我补全成这样，到后面反而是浪费了时间。

我不是很喜欢 Swift，究其原因如下：

1. 必须使用 Xcode 才能使用 Swift 语言
2. Xcode 不自带代码格式化，需要自己找插件
3. 格式化风格不统一
4. 没有热更新（Dart 都可以不依赖 Flutter 进行热更新）

在寻找 Swift 相关项目时看到了能使 Swift 热更新的 [InjectIII](https://github.com/johnno1962/InjectionIII) 项目，为什么 Apple 不加？

> 2024-07-05 12:50:35
> 修正：Swift 可以在 macOS、Linux、Windows 上使用，详见 [官方文档](https://www.swift.org/getting-started/)
> 这下更喜欢 Swift 了 🥰

## Xcode

我真的很想吐槽：这是人用的 IDE？

真的很难想象 Xcode 没有 Internationalization，以及它的那些面板排布为什么这么反人类，文件管理视图为什么这么让人憋屈。

我知道 Xcode 和 Android Studio 一样都有个项目视图，但 Android Studio 还能让人切到文件视图，但 Xcode，我的选项呢？

`Preview` 功能是需要表扬的，因为 SwiftUI 不支持热更新所以连 `Preview` 都没有的话就更写不下去了。

但它这 `Preview` 是会丢失状态的，所以还是有点不行。

## SwiftUI

我要骂死你们的 Document 啊，你们是不舍得给例子吗？光有文字描述我怎么知道我怎么使用这个组件、函数、类啊？

`List` 也是神鬼莫测，文档不说明它会自动给子组件加背景和分割线，我在思考。

有个 `LabeledContent` 这么好的组件你怎么忍心让它吃灰呢？我一开始一直都是用 `HStack { Label() Space() Text() }` 这样实现类似 Flutter 里的 `ListTile` 组件的。

它要是像 Flutter 那样有一个 [组件 Gallery](https://flutter.github.io/samples/web/material_3_demo/#/) 给你展示出来多好啊，可就是没有。

要称赞的一点就是它的 `Text` 组件，能直接写 Markdown 转 URL 链接：

```swift
Text("[byrdsaron@gmail.com](mailto://byrdsaron@gmail.com)")
```

## 总结

资料好少，我好伤心。

自己在用 SwiftUI 写一个手写字体创建软件，我要了解 [Unicode](https://home.unicode.org/)、字体、字形的相关知识，特别是怎么在 SwiftUI 里实现这件事，因为这需要涉及到一些比较低级的函数和接口。

但资料少的一批，官方文档简略的一批，鼠鼠我伤心的一批 😢。
