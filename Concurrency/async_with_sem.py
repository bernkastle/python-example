#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/03/2019 11:26
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

import aiohttp
import asyncio


async def main(pool):  # 启动
    sem = asyncio.Semaphore(pool)
    # 信号量用于控制并发数
    async with aiohttp.ClientSession() as session:  # 给所有的请求，创建同一个session
        tasks = []
        # 在异步协程中，task必须被包装为task或者future，gather是high-level api，可以简单的包装future，wait 是low-level api， 这里使用wait
        [tasks.append(control_sem(sem, 'https://api.github.com/events?a={}'.format(i), session)) for i in
         range(10)]  # 十次请求

        # wait包装task
        await asyncio.wait(tasks)


async def control_sem(sem, url, session):  # 限制信号量
    async with sem:
        await fetch(url, session)


async def fetch(url, session):  # 开启异步请求
    async with session.get(url) as resp:
        json = await resp.json()
        print(json)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(pool=2))