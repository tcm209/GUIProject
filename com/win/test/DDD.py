# # import psutil
# # pids = psutil.pids()
# # i=0
# # for pid in pids:
# #   try:
# #     p = psutil.Process(pid)
# #     print("pid-%d,pname-%s" % (pid, p.name()))
# #     pname=p.name()
# #     if pname=="MainUI.exe":
# #       i=i+1
# #   except :
# #     print("读取异常，关闭重新打开")
# # if i>2:
# #   print("不允许执行")
# # -*- coding: utf-8 -*-
#
# import hmac
# def hmac_encrypt(txt):
#   h = hmac.new('touchme209'.encode('utf-8'))
#   h.update(txt.encode('utf-8'))
#   hstr=h.hexdigest()
#   return hstr
#
# if __name__ == '__main__':
#     s=hmac_encrypt("hello")
#     ss=hmac_encrypt("hello")
#     print(s)
#     print(ss)