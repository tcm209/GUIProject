# -*- coding: utf-8 -*-
import time
import datetime

# 获取日期 格式化
def _get_date_formate():
    now = int(round(time.time() * 1000))
    nowformate = time.strftime('%Y-%m-%d', time.localtime(now / 1000))
    return nowformate

#   获取13位时间戳
def _get_time_stamp13():
    # 生成13时间戳   eg:1540281250399895
    datetime_now = datetime.datetime.now()
    # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 3位，微秒
    data_microsecond = str("%06d" % datetime_now.microsecond)[0:3]

    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)

# 获取16位时间戳
def _get_time_stamp16():
    datetime_now = datetime.datetime.now()
    print(datetime_now)

    # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 6位，微秒
    data_microsecond = str("%06d" % datetime_now.microsecond)

    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)




if __name__=="__main__":
    _get_date_formate()