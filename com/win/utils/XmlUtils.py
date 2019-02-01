# -*- coding: utf8 -*-
import xml.dom.minidom
from ProjectURL import _get_project_dir
#   获取element节点数据
def _get_element_by_tag(tagname):
    path = _get_project_dir() + "\\resource\\comfig.xml"
    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    elementval=root.getElementsByTagName(tagname)[0].firstChild.data

    return elementval

def _update_element_val(tagname,updateval):
    path = _get_project_dir() + "\\resource\\comfig.xml"
    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    elementnode = root.getElementsByTagName(tagname)[0]
    elementnode.firstChild.data=updateval
    fh=open(path,'w')
    dom.writexml(fh,encoding='utf-8')
    fh.close()





if __name__ == '__main__':
    _get_element_by_tag("mac")

    _update_element_val("phonenumber", 22)
    _update_element_val("encryptstr", 22)

    _update_element_val("mac", 33)
    _update_element_val("registdate",44)
    _update_element_val("timenumber", 55)
    _update_element_val("key_encry", 66)
    _update_element_val("isregisted", 0)



