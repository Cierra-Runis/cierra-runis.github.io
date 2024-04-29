---
title: 有关 Flutter 的若干笔记
tags:
  - Flutter
  - 笔记
  - 编程
abbrlink: 495
date: 2022-11-19 13:13:13
cover: img/有关-Flutter-的若干笔记/cover.png
---

## Flutter 介绍

`Flutter` 是 `Google` 推出并开源的移动应用开发框架，主打跨平台、高保真、高性能。开发者可以通过 `Dart` 语言开发 `App`,一套代码同时运行在 `iOS` 和 `Android` 平台。`Flutter` 提供了丰富的组件、接口，开发者可以很快地为 `Flutter` 添加 `Native` 扩展。

在此记录些常用资料：

|                      文档                       |                                                 文章                                                  |
| :---------------------------------------------: | :---------------------------------------------------------------------------------------------------: |
|        [官方网站](https://flutter.dev/)         | [Flutter 最佳实践和编码准则](https://ducafecat.com/blog/flutter-best-practices-and-coding-guidelines) |
|    [官方英文文档](https://docs.flutter.dev/)    |             [iPad 大屏 & Flutter 多引擎适配之路](https://zhuanlan.zhihu.com/p/589939547)              |
|     [官方中文文档](https://flutter.cn/docs)     |              [详解 android:elevation 的使用](https://www.python100.com/html/91048.html)               |
|       [官方 Package 站](https://pub.dev/)       |       [Flutter elevation 属性名称的含义](https://blog.csdn.net/gaoyp/article/details/123126394)       |
| [Flutter 实战](https://book.flutterchina.club/) |               [Android 中 elevation 的设置方法](https://www.jianshu.com/p/09959db18a4b)               |
|                                                 |                        [模式匹配](https://juejin.cn/post/7304930607133655059)                         |

|                    工具                    |                             包                              |
| :----------------------------------------: | :---------------------------------------------------------: |
| [Json to Dart](https://jsond.bytex.space/) |  [图片缓存](https://pub.dev/packages/cached_network_image)  |
|                                            | [BasedWidget](https://github.com/Cierra-Runis/based_widget) |
|                                            |  [QWeatherIcons](https://pub.dev/packages/qweather_icons)   |

## 使用 index.dart 文件简化导入

规定文件目录结构如下：

```plaintext
lib
│  index.dart
│  main.dart
│
├─pages
│      home_page.dart
│      index.dart
│      setting_page.dart
│
└─widgets
    │  index.dart
    │
    ├─dialog
    │      dialog_confirm_widget.dart
    │      dialog_from_json_widget.dart
    │      index.dart
    │
    └─diary
       │  index.dart
       │
       ├─list
       │      diary_list_item_place_holder_widget.dart
       │      diary_list_item_widget.dart
       │      diary_list_view_widget.dart
       │      index.dart
       │
       └─page
              diary_page_item_share_button_widget.dart
              diary_page_item_widget.dart
              diary_page_view_widget.dart
              index.dart
```

则在 `lib/index.dart` 内 `export` 所有子文件夹下的 `index.dart` 文件：

```dart
export 'main.dart';
export 'pages/index.dart';
export 'widgets/index.dart';
```

在 `pages/index.dart` 内 `export` 所有该文件夹下的 `*.dart` 文件：

```dart
export 'home_page.dart';
export 'setting_page.dart';
```

在所有 `*.dart` 文件（包括 `main.dart` 文件）内尽绝大可能 `import 'package:<项目名>/index.dart';` 即可简化导入。

同时当要引入外部包时，只要在 `lib/index.dart` 文件内导入即可，当然，有时会出现不同包之间的类名冲突，此时在需要使用到该包的地方单独 `import` 即可，或者使用 `hide/show` 语法限制，具体例子如下：

```dart
/// 各路由下的 index.dart
export 'main.dart';
export 'pages/index.dart';
export 'widgets/index.dart';

/// flutter 相关
/// [RefreshCallback] 和 `export 'package:flutter/material.dart'` 冲突，两者近似
export 'package:flutter/cupertino.dart' hide RefreshCallback;
export 'package:flutter/services.dart'
    show DeviceOrientation, SystemChrome; // 设备服务
/// [Badge] 和 `export 'package:badges/badges.dart'; // 小红点提示` 冲突，我想用外部包
export 'package:flutter/material.dart' hide Badge;
export 'package:flutter/gestures.dart';

/// dart 相关
export 'dart:async' show Timer, StreamSubscription;
export 'dart:convert';
export 'dart:io';
export 'dart:ui' show ImageFilter;

/// 外部包相关
export 'package:badges/badges.dart'; // 小红点提示
/// [Interval] 和 `package:flutter/src/animation/curves.dart` 冲突，两者结构完全不同，但外部包里的这个用不到
export 'package:dart_date/dart_date.dart' hide Interval; // 日期工具
/// [Text] 和 `export 'package:flutter/material.dart` 冲突，两者结构完全不同，但外部包里的这个用不到
export 'package:flutter_quill/flutter_quill.dart' hide Text; // 富文本
```

## 版本号构建问题

`Flutter` 使用 `android/app/build.gradle` 来打包 `apk`, 且其引入了 `flutter.gradle` 并指向 `flutter.groovy` 如 `D:\Flutter\packages\flutter_tools\gradle\src\main\groovy\flutter.groovy`

约在 `flutter.groovy` 的 `993` 行

```groovy
if (shouldSplitPerAbi()) {
    variant.outputs.each { output ->
        def abiVersionCode = ABI_VERSION.get(output.getFilter(OutputFile.ABI))
        if (abiVersionCode != null) {
            output.versionCodeOverride =
                abiVersionCode * 1000 + variant.versionCode
        }
    }
}
```

我们知道 `flutter` 将判断是否使用了 `'split-per-abi'` 命令, 是则在 `ABI_VERSION` 选择一个版本 `*1000` 再加上构建号

官方解释见 [此链接](https://developer.android.com/studio/build/configure-apk-splits)

我们只需修改 `ABI_VERSION map` 如下

```groovy
private static final Map ABI_VERSION = [
    (ARCH_ARM32)        : 0,
    (ARCH_ARM64)        : 0,
    (ARCH_X86)          : 0,
    (ARCH_X86_64)       : 0,
]
```

**_注意若进行了 `Flutter` 版本更新，应重新修改该 `flutter.groovy` 文件_**

## `vivo` 系手机无法调试 `Flutter` 程序

`vivo` 系列手机升至 `Origin3` 后发现调试 `Flutter` 应用卡在启动页，并且没有任何报错，详见 [github issue](https://github.com/flutter/flutter/issues/117019)，简化自 [此链接](https://blog.csdn.net/qq910689331/article/details/128790897)

答案是 `vivo` 系统发大病连日志都隐藏，我们需要提供 `IMEI 1` 码至 `vivo` 官方进行授权

1. 拨号盘输入 `*#06#` 复制 `IMEI 1` 值
2. 添加企业 QQ 号 `3002261823`（或通过 [官方网站](https://dev.vivo.com.cn/connectus/customerService?from=header) 联系）
3. 提交相关问题和信息，要求一键授权自己的手机
4. 等待授权成功后拨号盘输入 `*#*#112#*#*`，`“右上角按钮”->“更多”->“一键授权”` 即可

## `AlertDialog` `content` 传入 `ListView` 时在调试模式下报错

这是个怪问题，`release` 版本正常运行，解决方法如下：

```dart
AlertDialog(
  title: (...),
  content: SizedBox(
    width: double.minPositive, // 可选 double.maxFinite 但建议为 double.minPositive,
    child: ListView(
      shrinkWrap: true,
      children: (...),
    ),
  ),
  contentPadding: (...),
  actions: (...),
);
```

## ard 语法

详见 [此页面](https://my.oschina.net/lemos/blog/5559979)

## 代码规范

1. 尽可能使用 `''` 而不是 `""` 来表示字符串
2. 尽量不使用 `StatefulWidget / ConsumerStatefulWidget` 而是 `StatelessWidget / ConsumerWidget`
3. 尽量不要使用 `const MyWidget({Key? key}) : super(key: key);` 而是 `const MyWidget({super.key});`，对于其他变量也是如此
4. 对 `StatelessWidget / ConsumerWidget` 组件，其结构如下

   ```dart
   class MyWidget extends StatelessWidget {
       const MyWidget({super.key});

       void _myFunction() {
           (...)
       }

       @override
       Widget build(BuildContext context) {
           return Container();
       }

       Future<void> _myFuture() {
           (...)
       }
   }
   ```

   ```dart
   class MyWidget extends ConsumerWidget {
       const MyWidget({super.key});

       void _myFunction() {
           (...)
       }

       @override
       Widget build(BuildContext context, WidgetRef ref) {
           return Container();
       }

       Future<void> _myFuture() {
           (...)
       }
   }
   ```

5. 对 `StatefulWidget / ConsumerStatefulWidget` 组件，其结构如下

   ```dart
   class MyWidget extends StatefulWidget {
       const MyWidget({super.key});
       (...)

       @override
       State<MyWidget> createState() => _MyWidgetState();
   }

   class _MyWidgetState extends State<MyWidget> {
       (...)

       @override
       void initState() {
           super.initSate();
           (...)
       }

       @override
       void dispose() {
           (...)
           super.dispose();
       }

       void _myFunction() {
           (...)
       }

       @override
       Widget build(BuildContext context) {
           return Container();
       }

       Future<void> _myFuture() {
           (...)
       }
   }
   ```

   ```dart
   class MyWidget extends ConsumerStatefulWidget {
       const MyWidget({super.key});
       (...)

       @override
       ConsumerState<MyWidget> createState() => _MyWidgetState();
   }

   class _MyWidgetState extends ConsumerState<MyWidget> {
       (...)

       @override
       void initState() {
           super.initSate();
           (...)
       }

       @override
       void dispose() {
           (...)
           super.dispose();
       }

       void _myFunction() {
           (...)
       }

       @override
       Widget build(BuildContext context) {
           return Container();
       }

       Future<void> _myFuture() {
           (...)
       }
   }
   ```

## 感想

- `Flutter` 的使用非常简单，上手也快，非常有意思

- 自己用 `Flutter` 写了很多项目，这里来个 `Mercurius` 日记软件的 [仓库链接](https://github.com/Cierra-Runis/mercurius)
