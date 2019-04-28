#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 26/04/2019 15:44
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

import datetime
import calendar
from dateutil import rrule
from dateutil.parser import parse


def get_month_first_day_and_last_day(year=None, month=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)

    return firstDay, lastDay


def parse_month(date: datetime):
    return date.strftime('%Y%m')


def get_month_list(start_month, end_month):
    """
    生成月份列表,使用了dateutil库重的rrule函数
    :param start_month: 起始月份，格式为 201901
    :param end_month: 结束月份，格式为 201912
    :return:返回201901月到201912月之间所有月份，包括201901和201902
    """
    return list(map(parse_month, list(rrule.rrule(rrule.MONTHLY, dtstart=parse(start_month), until=parse(end_month)))))
