---
title: Next.js 和 React 使用报告
tags:
  - 使用报告
abbrlink: 23517
date: 2024-03-28 13:52:05
cover: img/Next-js-和-React-使用报告/cover.webp
---

使用报告系列开新坑了，今天要谈的是 [Next.js](https://nextjs.org/docs) 14。为什么是 14 呢，因为我从 14 学的，别叫。

先做个介绍吧，最新的 Next.js 官网上其称自己为“The React Framework for the Web”，记得之前有多加一个“专为生产环境”的头衔，总之，人家是框架，开发的方方面面都体贴的为你想到了。

对了，可能还要再介绍 [React](https://react.dev/learn)，它自己介绍自己为“JavaScript library”，在我看来，它就是将原先命令式的 JavaScript 操作，改为了更加简约的声明式组件，提升了组件的复用性。

对，大学课程里教过我们使用 jQuery 来操作 HTML 元素，但这玩意怎么还没死啊？这不累死个人？这不老古董？

以及，React 操作的是 [DOM](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model/Introduction) 节点，通过 `Link` 组件，其能在“跳转页面”时不再真正跳转页面，而是根据新获取的信息更新当前页面，直观来说就是浏览器左上角不再出现转圈圈的刷新图标，使单页应用成为可能。

我是不是还要再解释一下什么是 [单页应用](https://developer.mozilla.org/zh-CN/docs/Glossary/SPA)（？）。

## 一、非常好路由

Next.js 一大好处就是基于文件系统的路由，它抹去了原 React 提供的注册路由的方案，以及其提供的动态路由。

具体的不细讲，但我应该说明一点，就是即便 React Native 也有基于文件系统的动态路由，我也不会喜欢 React Native，因为移动端是移动端，网页是网页，如果真喜欢网页这一套，那还不如真就 `WebView` 跑网页完事。

## 二、组件设计

Next.js 是 React 的框架，所有为 React 开发的 UI 库都能在 Next.js 里使用（不像某个 React Native（指指点点.jpg））。

之前和谢佬参赛时使用的是 [MUI](https://mui.com/) 下的 [Joy UI](https://mui.com/joy-ui/getting-started/)，但 React 的生态太广阔了，不局限于 Joy UI，自己转用了 [NextUI](https://nextui.org/docs/components/avatar) 和 [Ant Design](https://ant.design/components/overview-cn/)，前者和开发 Next.js 的 Vercel 公司没有任何关系，但 UI 看起来很像，后者则是蚂蚁集团开发的。

使用别人的组件基本上就按它们的文档来就行，它们提供的属性一般就足够了。

但我们还是有自己写点样式的，这里就不得不提到 [TailwindCSS](https://tailwindcss.com/docs/installation) 了。

## 三、组件的修改

内联样式如果使用 `style` 属性来配置，会变得极为冗长，TailwindCSS 能大大改善这点，并对响应式的支持更好——比如对界面大小的响应、暗黑模式的响应、打印状态的响应。

更不用说我不喜欢的外置 CSS 文件了。

## 四、服务器组件和客户端组件

这我看过教程，但教程里的方法是 Next.js 14 之前的，我理解还是不太清楚，经常到了报错说要用 `"use client"` 时才反应过来。

这个还得再了解了解。

## 五、状态管理和 Hook

React 本身有带 [状态管理](https://react.dev/learn/passing-data-deeply-with-context) 和一些简单的 [Hooks](https://react.dev/reference/react/hooks)，因为我在学 Flutter 时对 Flutter 本身自带的、也是通过 `context` 向上查找根组件保存的状态的 [状态管理](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html)，以及 [flutter_hooks](https://pub.dev/packages/flutter_hooks) 包里的 Hooks 有一些了解，或者说 Flutter 和 flutter_hooks 本身就从 React 学习了很多，我也就大致对 React 的状态管理和 Hooks 有了一些概念。

具体深造还是得靠写项目的，原理可以不清楚，但总不可以不会用吗——虽然说面试可能也会问到就是了。

和 Flutter 有社区的状态管理方案一样，React 也有其它的状态管理方案 —— [Redux](https://redux.js.org/)（实际上 Flutter 社区就有 [同名包](https://docs.flutter.dev/data-and-backend/state-mgmt/options#redux)），但我不会用。

而且据谢佬说这东西太复杂了，给我推荐了 [zustand](https://github.com/pmndrs/zustand)，到时候都学学看就是了。

而 Hooks 方面，我不太理解 `useEffect` 是用来干什么的，感觉 `useState` 就足够了——我看 `useEffect` 的一个应用的网络请求，但我明显找到了一个更牛逼的 Hooks —— [useSWR](https://swr.vercel.app/zh-CN/docs/getting-started)，其也是由  Next.js 背后的同一团队创建的。

真的非常有用这玩意，我甚至从它身上看到了 mercurius 的未来（指数据同步）。

六、总结

Next.js 和 React 的组合非常适合网页开发，可能之后学习 [Vue](https://vuejs.org/) 的时候会再来一个它们间的对比，所以说本报告肯定会有第二期。
