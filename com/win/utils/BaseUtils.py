# -*- coding: utf-8 -*-
import re

# 验证手机号是否正确
def _check_phone_number(phonenumber=None):
    phone_pat=re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    if phonenumber is not None:
        res = re.search(phone_pat, phonenumber)
        if res:
            return True
        else:
            return False

def _send_message_to_authoremail(message):
    print("asdas")




