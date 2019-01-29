# -*- coding: utf-8 -*-

import wx
from com.win.utils.BaseUtils import _check_phone_number
from com.win.utils.MachineMessage import _get_machine_message
from com.win.utils.DateUtils import _get_time_stamp13,_get_date_formate,_get_time_stamp16
from com.win.utils.BaseConfigs import _get_yaml


class RegistUI(wx.Dialog):

    def __init__(self, title, func_callBack,macnumber,registtime):
        wx.Dialog.__init__(self, None, -1, title, size=(300, 200))
        self.func_callBack = func_callBack
        self.mac = macnumber
        self.registnumber=registtime
        #  x轴
        self.f_x=10
        self.s_x_input=70
        self.t_x=80
        #  y轴
        self.f_y=20
        self.s_y=70
        self.t_y=110

        self.size_w=180
        self.size_h=30
        # 读取yaml文件
        self.yamltool=_get_yaml()







        self.showUI()  #布局注册页面





    def showUI(self):
        panel = wx.Panel(self)
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)  # 字体样式
        # 添加静态标签
        self.phone_Label=wx.StaticText(panel, -1, "手 机", pos=(self.f_x, self.f_y))
        self.phone_Label.SetFont(font)
        self.phoneNumber=wx.TextCtrl(panel,-1,pos=(self.s_x_input,self.f_y),size=(self.size_w,self.size_h-5))

        self.secret_Label=wx.StaticText(panel,-1,"密 钥",pos=(self.f_x,self.s_y))
        self.secret_Label.SetFont(font)
        self.secret_key=wx.TextCtrl(panel,-1,pos=(self.s_x_input,self.s_y),size=(self.size_w,self.size_h))

        self.regist=wx.Button(panel,-1,"注册",pos=(self.t_x,self.t_y),size=(120,40))


    # 注册
    def regist_event(self,event):
        # 获取手机号
        phonenumber=self.phoneNumber.GetValue()
        secret_key=self.secret_key.GetValue()
        registdate = _get_date_formate()
        timenumber = _get_time_stamp13()
        key_encry = str(_get_time_stamp16())
        if phonenumber != '':
            isTrue=_check_phone_number(phonenumber)
            if isTrue:

                encrypt_str = '{"MAC":' + self.mac + ' ,"PHONE": ' + str(phonenumber) + ',"TIMENUMBER": ' + str(timenumber) + ',"REGISTDATE":' + registdate + ',"KEY_ENCRY":' + key_encry + '}'
                wx.MessageBox("请联系作者申请使用权限", "Message")

            else:
                wx.MessageBox("请检查手机输入是否正确", "Message")






