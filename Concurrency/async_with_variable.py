#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 18/03/2019 16:23
# # @Author : karl wang
# # @Email: karl.wang.1991@gmail.com
import asyncio
import random


async def test():
    await asyncio.sleep(random.randrange(1, 10))
    return random.randrange(1, 10)

# 生成函数列表
tasks = [test() for x in range(5)]

# 获取时间循环
loop = asyncio.get_event_loop()

# gather返回list
all_data = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
print(all_data)