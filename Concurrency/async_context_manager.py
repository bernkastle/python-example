#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 13:43
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

import aiohttp
import asyncio


class Http:
    """
    此class封装异步上下文管理功能。
    """

    # python3.5 引入异步上下文管理功能，增加新魔法函数__aenter__和__aexit__，分别等同为异步构造函数和异步析构函数
    # 初始化aiohttp session
    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    # 析构aiohttp session
    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    # 真实逻辑函数
    async def fetch(self, url):
        async with self._session.get(url) as resp:
            resp.raise_for_status()
            return await resp.read()


async def main():
    # 函数使用时依然要包装在一个异步函数中
    async with Http() as http:
        print(await asyncio.gather(http.fetch('http://www.qq.com'), http.fetch('http://www.baidu.com')))


if __name__ == '__main__':
    # 事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
