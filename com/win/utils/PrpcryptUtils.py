# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import random
import base64
# 加密工具
class prpcrypt():

    def __init__(self):

        self.mode = AES.MODE_CBC


    # 加密文本
    def encrypt(self,text,key):
        #
        cryptor=AES.new(key,self.mode,key)
        # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count=len(text)
        pad=length-(count%length)
        text=text+('\0'*pad)

        self.ciphertext=cryptor.encrypt(text)
        # Aes加密得到的字符串不一定是ascii字符集 输出到终端或者保存时会出问题
        # 这里统一把加密后的字符串转换位16进制字符串
        encryptstr=b2a_hex(self.ciphertext)
        encryptstr=str(encryptstr,'utf-8')
        # base64加密
        base64str=base64.b64encode(encryptstr.encode('utf-8'))

        return base64str
    # 解密
    def decrypt(self,text,key):
        # base64解密
        base64_decrypt = base64.b64decode(text.encode('utf-8'))
        decrypttext=str(base64_decrypt, 'utf-8')

        cryptor=AES.new(key,self.mode,key)
        target_text=cryptor.decrypt(a2b_hex(decrypttext))
        decryptstr=str(target_text,'utf-8')
        targetstr=decryptstr.rstrip('\0')

        return targetstr

    # 获取16位随机密码
    def get_random_secret(self):
        samplestr="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
        randomstr="".join(random.sample(samplestr,16))
        return randomstr




if __name__ == '__main__':
    print("")
    # send_encryptkey="JA@eDmi&osEx#q2BYzgxOWQ1NjAzMzZmYzVkYzZmNzQ2ZTU4ODhmZGY0MzVlMjE3ZjA5Nzk5Y2Y2ZDRiMGRmM2MzYWVmZWUwMDM4YmY2MTNmYmZjMjVkOTk2NDRkNmY1OWEwMDI3Y2NhM2NiYWFlZjNkYWNlNzJjNTg5YTIyODA5MWJjNDY2NDJkNzA5YWZkYmI4NzhkMDJiZjc3MWFmODFkZDVmYmRhZmY4ZTg2MzE1MmE0YWMwZGIxNjAyM2UxZDIzOGVjZGQzMWRlNjkxMmEwMTUyMzM1ZGJlMmQ5MDg1NDNkNWMwMmY1YWFmNGQzMThiNzU5NWYyY2E0ZDdmZjM0OWRhZjQyNzMyYzUzYjZiYTBmMjMwZWUxMTQ0ZTgzMmRjNGRhZWQxZjM5"
    # sendkey=send_encryptkey[0:16]
    # ms=send_encryptkey[16:len(send_encryptkey)]
    # # 解密
    # prpcrypttool = prpcrypt()
    # un_encrypt = prpcrypttool.decrypt(ms, sendkey)
    # jsondata = eval(un_encrypt)
    # key_e = jsondata['KEY_ENCRY']
    # st=str(prpcrypttool.encrypt(un_encrypt,key_e),"utf-8")
    # _create_file(st)
    # print("自己："+st)
    #
    # xmlencrykey = _get_element_by_tag("encryptstr")
    # print("系统："+xmlencrykey)
    # if st==xmlencrykey:
    #     print("------------------------ok")
    #
    # #
    # # un_ss = prpcrypttool.decrypt(xmlencrykey, key_e)
    # # print(un_ss)



#
# if __name__ == '__main__':
#
#
#
#     mac=_get_machine_message()
#     timenumber=_get_time_stamp13()
#     phonenumber=15659813871
#     registdate=_get_date_formate()
#     daynumber=2
#     key_encry=str(_get_time_stamp16())
#
#
#     # AES加密
#     encrypt_str='{"MAC":'+mac+' ,"PHONE": '+str(phonenumber)+',"TIMENUMBER": '+str(timenumber)+',"REGISTDATE":'+registdate+',"DAYS":'+str(daynumber)+'}'
#     prpcrypttool=prpcrypt(key_encry)
#
#     prpcrypttool.get_random_secret()
#
#
#     AES_txt=prpcrypttool.encrypt(encrypt_str)
#     print("AES加密后："+str(AES_txt,'utf-8'))
#     # AES解密
#     txt=prpcrypttool.decrypt(str(AES_txt,'utf-8'))
#     print("解密后"+txt)
#     _write_yaml('AES_Encrypt_Key','11111')
#
#
#     # base64加密解密
#
#     keystr = base64.b64encode(encrypt_str.encode('utf-8'))
#     str_decrypt = str(keystr, 'utf-8')
#     print("64密钥：" + str_decrypt)
#     # base64解密
#     base64_decrypt=base64.b64decode(str_decrypt.encode('utf-8'))
#     print("BASE64解密串（UTF-8）:\n", str(base64_decrypt, 'utf-8'))


