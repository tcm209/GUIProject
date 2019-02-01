# -*- coding: utf-8 -*-
import uuid
# 获取电脑基本信息
def _get_machine_message():
    # mac地址
    addr_num = hex(uuid.getnode())[2:]
    mac = "_".join(addr_num[i:i+2] for i in range(0,len(addr_num),2))

    return mac
