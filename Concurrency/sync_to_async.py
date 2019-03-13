#!/usr/bin/env python
# encoding:utf-8

import asyncio
import requests
import time


async def download(url):
    """
    同步函数，加上async关键字，宣称为awaitable
    :param url:
    :return:
    """
    response = requests.get(url)
    print(response.text)


async def wait_download(url):
    """
    包装同步函数为一个原生的协程对象，等待同步函数完成
    :param url:
    :return:
    """
    await download(url) # 这里download(url)就是一个原生的协程对象
    print("get {} data complete.".format(url))


async def main():
    start = time.time()
    # 添加协程执行函数
    await asyncio.wait([
        wait_download("http://www.163.com"),
        wait_download("http://www.mi.com"),
        wait_download("http://www.baidu.com")])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


# 添加时间循环，异步函数必须要有事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
