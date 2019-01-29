# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import sys
from com.win.utils.MachineMessage import _get_machine_message
from com.win.utils.DateUtils import _get_time_stamp13,_get_date_formate,_get_time_stamp16
from com.win.utils.BaseConfigs import _get_yaml,_write_yaml
import base64
# 加密工具
class prpcrypt():

    def __init__(self,key):
        print("初始化加密文件")
        self.mode = AES.MODE_CBC
        self.key = key

    # 加密文本
    def encrypt(self,text):
        #
        cryptor=AES.new(self.key,self.mode,self.key)
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
    def decrypt(self,text):
        # base64解密
        base64_decrypt = base64.b64decode(text.encode('utf-8'))
        decrypttext=str(base64_decrypt, 'utf-8')

        cryptor=AES.new(self.key,self.mode,self.key)
        target_text=cryptor.decrypt(a2b_hex(decrypttext))
        decryptstr=str(target_text,'utf-8')
        targetstr=decryptstr.rstrip('\0')

        return targetstr




if __name__ == '__main__':




    mac=_get_machine_message()
    timenumber=_get_time_stamp13()
    phonenumber=15659813871
    registdate=_get_date_formate()
    daynumber=2
    key_encry=str(_get_time_stamp16())


    # AES加密
    encrypt_str='{"MAC":'+mac+' ,"PHONE": '+str(phonenumber)+',"TIMENUMBER": '+str(timenumber)+',"REGISTDATE":'+registdate+',"DAYS":'+str(daynumber)+'}'
    prpcrypttool=prpcrypt(key_encry)
    AES_txt=prpcrypttool.encrypt(encrypt_str)
    print("AES加密后："+str(AES_txt,'utf-8'))
    # AES解密
    txt=prpcrypttool.decrypt(str(AES_txt,'utf-8'))
    print("解密后"+txt)
    _write_yaml('AES_Encrypt_Key','11111')


    # base64加密解密

    keystr = base64.b64encode(encrypt_str.encode('utf-8'))
    str_decrypt = str(keystr, 'utf-8')
    print("64密钥：" + str_decrypt)
    # base64解密
    base64_decrypt=base64.b64decode(str_decrypt.encode('utf-8'))
    print("BASE64解密串（UTF-8）:\n", str(base64_decrypt, 'utf-8'))


