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

def _write_yaml(key,val):
    path = os.path.join(os.path.dirname(__file__) + '/testconfig.yaml')
    # 写入yaml 文件
    # a 追加写入，w,覆盖写入
    fw = open(path, 'a', encoding='utf-8')

    # 构建数据
    data = {
        "REGIST": {'domain': '.yiyao.cc', 'expiry': 1521558688.480118, 'httpOnly': False, 'name': '_ui_', 'path': '/',
                    'secure': False, 'value': 'HSX9fJjjCIImOJoPUkv/QA=='}}
    # 装载数据
    yaml.dump(data, fw)


if __name__ == '__main__':
    print(_get_yaml())