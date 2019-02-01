# -*- coding: utf-8 -*-
import re
import smtplib
from email.mime.text import MIMEText
from com.win.utils.BaseConfigs import _get_yaml
from email.header import Header
from ProjectURL import _get_project_dir
from com.win.utils.XmlUtils import _update_element_val,_get_element_by_tag
from com.win.utils.PrpcryptUtils import prpcrypt
from com.win.utils.DateUtils import _get_date_formate_unline,_get_date_formate_line
import psutil
import hmac

# 验证手机号是否正确
def _check_phone_number(phonenumber=None):
    phone_pat=re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    if phonenumber is not None:
        res = re.search(phone_pat, phonenumber)
        if res:
            return True
        else:
            return False

def _send_message_to_authoremail(msg_from,message):
    """
        邮件通知
        :param str: email content
        :return:
        """
    email_conf = _get_yaml()
    is_email = email_conf["email_conf"]["is_email"]
    if is_email:
        try:
            port = email_conf["email_conf"]["port"]
            sender = email_conf["email_conf"]["email"]
            receiver = email_conf["email_conf"]["notice_email_list"]
            subject = "申请成功"
            username = email_conf["email_conf"]["username"]
            password = email_conf["email_conf"]["password"]
            host = email_conf["email_conf"]["host"]
            s = "{0}".format(message)

            msg = MIMEText(s, 'plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = sender
            msg['To'] = receiver
            smtp = smtplib.SMTP_SSL(host, port)
            # smtp.connect(host)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver.split(","), msg.as_string())
            smtp.quit()
            print(u"邮件已通知, 请查收")
        except Exception as e:
            print(u"邮件配置有误{}".format(e))
    else:
        pass
# 创建认证文件
def _create_file(send_encryptkey):
    # send_encryptkey = "JA@eDmi&osEx#q2BYzgxOWQ1NjAzMzZmYzVkYzZmNzQ2ZTU4ODhmZGY0MzVlMjE3ZjA5Nzk5Y2Y2ZDRiMGRmM2MzYWVmZWUwMDM4YmY2MTNmYmZjMjVkOTk2NDRkNmY1OWEwMDI3Y2NhM2NiYWFlZjNkYWNlNzJjNTg5YTIyODA5MWJjNDY2NDJkNzA5YWZkYmI4NzhkMDJiZjc3MWFmODFkZDVmYmRhZmY4ZTg2MzE1MmE0YWMwZGIxNjAyM2UxZDIzOGVjZGQzMWRlNjkxMmEwMTUyMzM1ZGJlMmQ5MDg1NDNkNWMwMmY1YWFmNGQzMThiNzU5NWYyY2E0ZDdmZjM0OWRhZjQyNzMyYzUzYjZiYTBmMjMwZWUxMTQ0ZTgzMmRjNGRhZWQxZjM5"
    sendkey = send_encryptkey[0:16]
    ms = send_encryptkey[16:len(send_encryptkey)]
    print(ms)
    # 解密
    prpcrypttool = prpcrypt()
    un_encrypt = prpcrypttool.decrypt(ms, sendkey)
    jsondata = eval(un_encrypt)
    key_e = jsondata['KEY_ENCRY']
    st = str(prpcrypttool.encrypt(un_encrypt, key_e), "utf-8")
    path = _get_project_dir()+"\\resource\\rsa.tcl"
    f=open(path,"w",encoding="utf-8")
    f.write(st)
    f.close()

# 认证是否通过
def _is_using(path):
    file=open(path,"r",encoding="utf-8")

    encrpty_str=file.readline()
    file.close()
    xmlencrykey = _get_element_by_tag("encryptstr")
    if encrpty_str==xmlencrykey:#验证通过
        _update_element_val("isregisted",1)
        return True
    else:
        return False

# 创建日志文件
def _create_log_file(txt):
    logtxt=_get_date_formate_line()+"："+txt+"\n"
    filename = _get_date_formate_unline()
    path=_get_project_dir()+"\\log\\"+filename+".log"
    logfile=open(path,mode='a',encoding='utf-8')
    logfile.writelines(logtxt)
    logfile.close()
# 是否允许一台电脑执行多个
def _is_stoped():
    i = 0
    try:
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)

            pname = p.name()
            if pname == "MainUI.exe":
                i = i + 1
    except:
        i = 404
        _create_log_file("读取异常，关闭重新打开")
    if i > 2:
        return False
    else:
        return True

# mac加密配置文件xml
def hmac_encrypt(txt):
  h = hmac.new('touchme209'.encode('utf-8'))
  h.update(txt.encode('utf-8'))
  hstr=h.hexdigest()
  return hstr


if __name__ == '__main__':
    _create_log_file("asdasdadasssssssssssssssssss")




