'''
发布用 py 脚本
main.py
'''

import os
from typing import Any


def input_tool(
    first_message: str,
    rule: str,
    error_message: str,
    rule_function: Any,
) -> str:
    '''
    根据 rule_function 获取合法的值
    '''
    # 提醒
    print(f'> {first_message} {rule}: ', end='')
    # 第一次输入
    input_str = input()
    # 当 rule_function(input_str) 返回 false
    # 即不合法时
    while not rule_function(input_str):
        # 重新提醒并输入
        print(f'> {error_message}')
        print(f'> {first_message} {rule}: ', end='')
        input_str = input()
    # 直至输入合法
    return input_str


def build_module() -> None:
    '''
    构建模块
    '''
    print('> 清除旧构建')
    os.system('hexo clean')

    print('> 获取最新 bangumi 资讯')
    os.system('hexo bangumi -u')

    print('> 构建中')
    os.system('hexo generate')

    print('> 开启服务中')
    os.system('hexo server')


def release_module() -> None:
    '''
    发布模块
    '''
    print('> 清除旧构建')
    os.system('hexo clean')

    print('> 获取最新 bangumi 资讯')
    os.system('hexo bangumi -u')

    print('> 构建中')
    os.system('hexo generate')

    print('> 发布中')
    os.system('hexo deploy')

    print('> 同步本仓库中')
    os.system('git add .')
    os.system('git commit -m "修改"')
    os.system('git push --force')
    print('> 已发布携带信息为 "修改" 的仓库, 请检查发布情况')


if __name__ == '__main__':
    os.system('cls')
    print('-- main.py --')
    input_str = ''
    input_str = input_tool(
        first_message='是否进入发布模式，反之进入构建模式',
        rule='(y/n)',
        error_message='请只输入 y 或 n',
        rule_function=lambda input_str: input_str == 'y' or input_str == 'n',
    )

    if input_str == 'y':
        release_module()
    else:
        build_module()
