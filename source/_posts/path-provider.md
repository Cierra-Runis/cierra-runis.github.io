---
title: path_provider
tags:
  - Flutter
  - 笔记
  - 编程
abbrlink: 42016
date: 2024-04-29 22:10:46
---

<h3 align="center">
  <a href="https://pub.dev/packages/path_provider#supported-platforms-and-paths">
    <code>path_provider</code>
  </a>
</h3>

| `${name} => app` | `${org} => com.example` | `${package} => ${org}.${name}` |
| :--------------: | :---------------------: | :----------------------------: |

|          `Directory`           | `Android` `..$0=>/data/user/0; ..$1=>/storage/emulate/0/Android/data` |    `Windows` `...=>C:\Users\${user}`    |
| :----------------------------: | :-------------------------------------------------------------------: | :-------------------------------------: |
|          `Temporary`           |                        🌞 `..$0/${org}/cache`                         |       🌞 `...\AppData\Local\Temp`       |
|     `Application Support`      |                        🌞 `..$0/${org}/files`                         | 🌞 `...\AppData\Roaming\${org}\${name}` |
|     `Application Library`      |                                  🌙                                   |                   🌙                    |
|    `Application Documents`     |                     🌞 `..$0/${org}/app_flutter`                      |           🌞 `...\Documents`            |
|      `Application Cache`       |                        🌞 `..$0/${org}/cache`                         |  🌞 `...\AppData\Local\${org}\${name}`  |
|       `External Storage`       |                        🌞 `..$1/${org}/files`                         |                   🌙                    |
|  `External Cache Directories`  |                     🌞 `..$1/${org}/files/cache`                      |                   🌙                    |
| `External Storage Directories` |                     🌞 `..$1/${org}/files/music`                      |                   🌙                    |
|          `Downloads`           |                                  🌙                                   |           🌞 `...\Downloads`            |

|          `Directory`           | `iOS` `...=>?/data/Containers/Data/Application/${hash}` | `macOS` `...=>/Users/${user}/Library/Containers/${package}/Data` |
| :----------------------------: | :-----------------------------------------------------: | :--------------------------------------------------------------: |
|          `Temporary`           |                 🌞 `.../Library/Caches`                 |                     🌞 `.../Library/Caches`                      |
|     `Application Support`      |          🌞 `.../Library/Application Support`           |         🌞 `.../Library/Application Support/${package}`          |
|     `Application Library`      |                    🌞 `.../Library`                     |                         🌞 `.../Library`                         |
|    `Application Documents`     |                   🌞 `.../Documents`                    |                        🌞 `.../Documents`                        |
|      `Application Cache`       |                 🌞 `.../Library/Caches`                 |                🌞 `.../Library/Caches/${package}`                |
|       `External Storage`       |                           🌙                            |                                🌙                                |
|  `External Cache Directories`  |                           🌙                            |                                🌙                                |
| `External Storage Directories` |                           🌙                            |                                🌙                                |
|          `Downloads`           |                   🌞 `.../Downloads`                    |                        🌞 `.../Downloads`                        |

|          `Directory`           | `Linux` |
| :----------------------------: | :-----: |
|          `Temporary`           |   🌞    |
|     `Application Support`      |   🌞    |
|     `Application Library`      |   🌙    |
|    `Application Documents`     |   🌞    |
|      `Application Cache`       |   🌞    |
|       `External Storage`       |   🌙    |
|  `External Cache Directories`  |   🌙    |
| `External Storage Directories` |   🌙    |
|          `Downloads`           |   🌞    |

<p align="center">
  <a href="https://github.com/Cierra-Runis">
    <code>Sorted by Cierra_Runis</code>
  </a>
</p>
