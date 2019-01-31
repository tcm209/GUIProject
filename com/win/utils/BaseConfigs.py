# -*- coding: utf8 -*-
import os
import yaml
from ProjectURL import _get_project_dir

def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = _get_project_dir() + "\\resource\\baseconfig.yaml"
    f = open(path, encoding='UTF-8')
    s = yaml.load(f)
    f.close()
    return s.decode() if isinstance(s, bytes) else s




if __name__ == '__main__':
    print(_get_yaml())