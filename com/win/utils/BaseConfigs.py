# -*- coding: utf8 -*-
import os
import yaml

def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/baseconfig.yaml')
    f = open(path, encoding='UTF-8')
    s = yaml.load(f)
    f.close()
    return s.decode() if isinstance(s, bytes) else s

if __name__ == '__main__':
    print(_get_yaml())