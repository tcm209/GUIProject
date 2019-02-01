# -*- coding: utf-8 -*-
from com.win.client.MainWX import MainWX
from com.win.utils.BaseUtils import _is_stoped,_create_log_file
import os

if __name__ == '__main__':
    isstoped=_is_stoped()
    if isstoped:
        app = MainWX()
        app.MainLoop()
    else:
        os.system('TASKKILL /F /IM MainUI.exe')
        _create_log_file("请检查是否打开多个未关闭的PY模型图")

