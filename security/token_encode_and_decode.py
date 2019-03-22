#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 22/03/2019 16:53
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

APP_KEY = 'karl'


def encode(data, expires_time: int = 3600) -> str:
    s1 = Serializer(APP_KEY, expires_in=expires_time)
    return s1.dumps(data)


def decode(data) -> str:
    s1 = Serializer(APP_KEY)
    return s1.loads(data)
