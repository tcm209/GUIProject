# -*- coding: utf-8 -*-
import wx
from com.win.utils.BaseConfigs import _get_yaml
from com.win.utils.MachineMessage import _get_machine_message
from com.win.utils.DateUtils import _get_date_formate,_get_time_stamp13
from com.win.utils.BaseUtils import _is_using,_create_file,_create_log_file,hmac_encrypt
import com.win.client.RegistUI as registDialog
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from com.win.utils.GraphUtils import GraphUtils
from com.win.utils.XmlUtils import _get_element_by_tag,_update_element_val
from ProjectURL import _get_project_dir

class CalculatorGui(wx.Frame):

    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='PY模型图', size=(600, 400), pos=(500, 200),style=(wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX))


        self.base_configs = _get_yaml()
        self.l_f_y = 30  # 第一行 y
        self.l_s_y = 70  # 第二行 y
        self.l_t_y = 110  # 第三行 y
        self.l_fo_y = 150  # 第四行

        self.l_f_x = 30  # 第一列 label x
        self.t_f_x = 100  # 第一列 txt x

        self.l_s_x = 270  # 第二列 label x
        self.t_s_x = 350  # 第二列 txt x

        self.l_t_x = 520  # 第三列 label x
        self.t_t_x = 600  # 第三列 txt x

        self.btn_x = 200

        # txt字体大小
        self.t_f_width = 150
        self.t_s_width = 150
        self.t_box_width = 150
        self.f_f_size = 24

        self.five_y = 200  # 第5行
        self.graphTool=GraphUtils()

        # 发送电脑物理地址
        self.machine_info = _get_machine_message()
        # 获取日期
        self.regist_date = _get_date_formate()
        # 获取注册信息状态是否可用


        self.UpdateUI=UpdateUI
        self.show_window()

        # 获取认证成功标准

        self.init_isused()







    #显示窗体
    def show_window(self):
        # 设置图标
        iconpath = _get_project_dir() + "\\images\\logo.ico"
        self.icon = wx.Icon(iconpath, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = wx.Panel(self,-1)
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)#字体样式
        # 初始化menubar
        menubar=wx.MenuBar(style=0)
        filemenu=wx.Menu()
        self.newitem = wx.MenuItem(filemenu, wx.ID_NEW, text="注册使用", kind=wx.ITEM_NORMAL)
        self.uploadfileitem=wx.MenuItem(filemenu,wx.ID_NETWORK,text="导入注册文件",kind=wx.ITEM_NORMAL)
        # self.registfile=wx.MenuItem(filemenu,wx.FD_SAVE,text="生成注册文件",kind=wx.ITEM_NORMAL)
        quitMENU = wx.MenuItem(filemenu, wx.ID_EXIT, '退出')


        filemenu.Append(self.newitem)
        filemenu.Append(self.uploadfileitem)
        # filemenu.Append(self.registfile)
        filemenu.AppendSeparator()
        filemenu.Append(quitMENU)
        menubar.Append(filemenu,'&设置')
        self.SetMenuBar(menubar)

        # 添加menubaritem点击事件
        self.Bind(wx.EVT_MENU, self.regist_gui, self.newitem)
        self.Bind(wx.EVT_MENU, self.uploadFile_FUN, self.uploadfileitem)
        # self.Bind(wx.EVT_MENU, self.registFileDialog, self.registfile)
        self.Bind(wx.EVT_MENU_CLOSE,self.onclose,quitMENU)
        self.Bind(wx.EVT_CLOSE,self.ui_closed)




        # 静态标签#
        #第一行   测量长度
        label_w = wx.StaticText(panel, -1, "测量长度", pos=(self.l_f_x, self.l_f_y))
        label_w.SetFont(font)
        self.w_input = wx.TextCtrl(panel, -1, size=(self.t_f_width, self.f_f_size), pos=(self.t_f_x, self.l_f_y))


        #第一行 测量宽度
        label_h = wx.StaticText(panel, -1, "测量宽度", pos=(self.l_s_x, self.l_f_y))
        label_h.SetFont(font)
        self.h_input = wx.TextCtrl(panel, -1, size=(self.t_f_width, self.f_f_size), pos=(self.t_s_x, self.l_f_y))



        #第二行 下拉选择
        label_out_line_spec=wx.StaticText(panel,-1,"外框规格",pos=(self.l_f_x,self.l_s_y))
        label_out_line_spec.SetFont(font)
        choices_out_line_spec = self.base_configs['set']['side_category_combox']
        self.out_line_spec_Box = wx.ComboBox(panel, -1,
                                        choices=choices_out_line_spec,
                                        pos=(self.t_f_x, self.l_s_y),
                                        size=(self.t_box_width, self.f_f_size),
                                        style=wx.CB_READONLY)
        #绑定事件
        self.out_line_spec_Box.Bind(wx.EVT_COMBOBOX, self.on_out_line_spec_Box_selected)

        label_inner_rod_spec = wx.StaticText(panel, -1, "内杆规格", pos=(self.l_s_x, self.l_s_y))
        label_inner_rod_spec.SetFont(font)
        choices_inner_rod_spec = self.base_configs['set']['side_category_combox']
        self.inner_rod_spec_Box = wx.ComboBox(panel, -1,
                                            choices=choices_inner_rod_spec,
                                            pos=(self.t_s_x, self.l_s_y),
                                            size=(self.t_box_width, self.f_f_size),
                                            style=wx.CB_READONLY)
        self.inner_rod_spec_Box.Bind(wx.EVT_COMBOBOX, self.on_inner_rod_spec_Box_selected)


        #第三行
        label_inner_pipe_spec = wx.StaticText(panel, -1, "内管规格", pos=(self.l_f_x, self.l_t_y))
        label_inner_pipe_spec.SetFont(font)
        choices_inner_pipe_spec = self.base_configs['set']['inner_pipe_category']
        self.inner_pipe_spec_Box = wx.ComboBox(panel, -1,
                                              choices=choices_inner_pipe_spec,
                                              pos=(self.t_f_x, self.l_t_y),
                                              size=(self.t_box_width, self.f_f_size),
                                              style=wx.CB_READONLY)
        self.inner_pipe_spec_Box.Bind(wx.EVT_COMBOBOX, self.on_inner_pipe_spec_Box_selected)


        label_window_category = wx.StaticText(panel, -1, "款式选择", pos=(self.l_s_x, self.l_t_y))
        label_window_category.SetFont(font)
        choices_window_category = self.base_configs['set']['window_style']
        self.window_category_Box = wx.ComboBox(panel, -1,
                                               choices=choices_window_category,
                                               pos=(self.t_s_x, self.l_t_y),
                                               size=(self.t_box_width, self.f_f_size),
                                               style=wx.CB_READONLY)
        self.window_category_Box.Bind(wx.EVT_COMBOBOX, self.on_window_category_Box_selected)

        # 计算按钮
        self.calcu_btn = wx.Button(panel, -1, "结果", size=(200, 30), pos=(self.btn_x, self.l_fo_y))
        # 富文本看
        self.show_rich_txt = wx.TextCtrl(panel,-1,
                                         size=(470,100),
                                         style= (wx.TE_MULTILINE | wx.TE_READONLY),
                                         pos=(self.l_f_x,self.five_y)
                                         )
        self.show_rich_txt.SetInsertionPoint(0)
        self.show_rich_txt.SetStyle(0, self.show_rich_txt.GetLastPosition(), wx.TextAttr("red", "green", font))

        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.on_clacu_click, self.calcu_btn)



        # self.frame.Center()
        # self.frame.Show(True)



    #点击事件
    def show_message(self,word="",inp=None,is_ok=False):
        if is_ok:
            dlg = wx.MessageDialog(None, word, u'错误', wx.YES_NO | wx.ICON_QUESTION)
        else:
            dlg = wx.MessageDialog(None, word, u'错误')

        if dlg.ShowModal() == wx.ID_YES:
            pass
            if inp is not None:
                inp.SetValue("")

        dlg.Destroy()
    #计算结果
    def on_clacu_click(self,event):
        is_show_model=True
        w_val=self.w_input.GetValue()#测量长
        h_val=self.h_input.GetValue()#测量宽
        h_is_number=self.is_number(h_val)
        w_is_number=self.is_number(w_val)
        out_line_spec_val=self.out_line_spec_Box.GetValue()#外框规格25 x 25
        inner_rod_spec_val=self.inner_rod_spec_Box.GetValue()#内杆规格25 x 25
        inner_pipe_spec_val=self.inner_pipe_spec_Box.GetValue()#内管规格 19 x 19
        inner_pipe_spec_num=self.base_configs['set']['inner_width']#19
        window_category=self.window_category_Box.GetValue()#款式 横 竖


        if h_is_number is None:
            self.show_message("非法字符，请输入正确的高度，是否清除？",self.h_input,True)
            return
        if w_is_number is None:
            self.show_message("非法字符，请输入正确的宽度，是否清除？", self.w_input,True)
            return

        if window_category == "":
            self.show_message("请选择管款式", None, False)
            return

        measure_w_float = float(w_val)#测量长
        measure_h_float = float(h_val)#测量宽

        if out_line_spec_val == "":
            self.show_message("请选择外框规格", None, False)
            return
        if measure_w_float > 3200 or measure_h_float > 3200 or measure_w_float<500 or measure_h_float<500:
            is_show_model=False
            self.show_message("在试用版测量长、宽大于3500不显示效果图", None, False)
        # 外边框规格
        start_index_out_line_spec=out_line_spec_val.index("X")
        end_index_out_line_spec=len(out_line_spec_val)
        out_line_spec_num_show =float(out_line_spec_val[0:start_index_out_line_spec])#可视宽度 计算
        out_line_spec_num_hidden = float(out_line_spec_val[start_index_out_line_spec+2:end_index_out_line_spec])#不可视宽度
        # 内杆规格
        start_index_inner_rod_spec = inner_rod_spec_val.index("X")
        end_index_inner_rod_spec=len(inner_rod_spec_val)
        inner_rod_spec_num_show=float(inner_rod_spec_val[0:start_index_inner_rod_spec])#可视宽度 计算
        inner_rod_spec_num_hidden=float(inner_rod_spec_val[start_index_inner_rod_spec+2:end_index_inner_rod_spec])#不可视宽度 计算

        if inner_rod_spec_num_hidden > out_line_spec_num_hidden:
            self.show_message("所选内杆参数大于边框参数", None, False)
            return
        if inner_pipe_spec_num > inner_rod_spec_num_hidden:
            self.show_message("所选内管参数大于内杆参数", None, False)
            return

        if window_category == "横式":
            #总长 1500 内管19x19 间距 100
            space_width =self.base_configs['set']['width_range'][0]['max']#间距100
            inner_pipe_count = self.on_calcute_result(measure_h_float,out_line_spec_num_show,space_width,inner_pipe_spec_num)
            _create_log_file("内管"+str(inner_pipe_count))
            #总长2000 内杆25x25 间距 400
            space_width = self.base_configs['set']['length_range'][0]['max']  # 间距400
            inner_rod_count = self.on_calcute_result(measure_w_float,out_line_spec_num_show,space_width,inner_rod_spec_num_show)
            _create_log_file("内杆" + str(inner_rod_count) )
            #竖着多处一点20
            measure_h_float_result_extend = measure_h_float+self.base_configs['set']['vertical_extend_max'] # 垂直方向多处20mm
            measure_h_rod_float_result = measure_h_float-2*out_line_spec_num_show # 内杆
            measure_w_pipe_float_result = measure_w_float-2*out_line_spec_num_show + self.base_configs['set']['inner_error_max'] # 内管
            self.fill_rich_txt(out_line_spec_val,measure_h_float_result_extend,measure_w_float,
                      inner_rod_spec_val,measure_h_rod_float_result,inner_rod_count,inner_pipe_spec_val,
                      measure_w_pipe_float_result,inner_pipe_count)
            #画图
            if is_show_model:
                input_width=measure_w_float/1000
                input_height=measure_h_float/1000
                horizontal_num=math.ceil(inner_pipe_count)+2  # 19x19
                vertical_num=math.ceil(inner_rod_count)+2  # 25x25
                main_pipe_w=out_line_spec_num_show/1000  # 主管宽 换算成m
                inner_rod_w=inner_rod_spec_num_show/1000  #内杆 25
                inner_pipe_w=inner_pipe_spec_num/1000  # 内管宽19 换算成m

                extend_w=self.base_configs['set']['vertical_extend_max']/1000
                self.graphTool.draw_graph(input_width,input_height,
                                          horizontal_num,vertical_num,
                                          main_pipe_w,inner_rod_w,inner_pipe_w,
                                          extend_w,"横式",
                                          out_line_spec_val,inner_rod_spec_val,inner_pipe_spec_val
                                          )




        elif window_category == "竖式":
            #总长 1500 内杆 25x25 间距 400
            space_width=self.base_configs['set']['length_range'][0]['max']  # 间距400
            inner_rod_count=self.on_calcute_result(measure_h_float,out_line_spec_num_show,space_width,inner_rod_spec_num_show)
            _create_log_file("内杆" + str(inner_rod_count))
            #总长 2000 内管19 x 19 间距100
            space_width=self.base_configs['set']['width_range'][0]['max']#间距100
            inner_pipe_count=self.on_calcute_result(measure_w_float,out_line_spec_num_show,space_width,inner_pipe_spec_num)
            _create_log_file("内管" + str(inner_pipe_count))
            measure_h_float_result_extend = measure_h_float + self.base_configs['set'][
                'vertical_extend_max']  # 垂直方向多处20mm
            measure_w_rod_float_result = measure_w_float - 2 * out_line_spec_num_show #内杆
            measure_h_pipe_float_result = measure_h_float - 2 *out_line_spec_num_show + self.base_configs['set']['inner_error_max'] # 内管

            self.fill_rich_txt(out_line_spec_val, measure_h_float_result_extend, measure_w_float,
                               inner_rod_spec_val, measure_w_rod_float_result, inner_rod_count, inner_pipe_spec_val,
                               measure_h_pipe_float_result, inner_pipe_count)

            if is_show_model:
                input_width = measure_w_float / 1000
                input_height = measure_h_float / 1000
                horizontal_num = math.ceil(inner_rod_count) + 2  # 19x19
                vertical_num = math.ceil(inner_pipe_count) + 2  # 25x25
                main_pipe_w = out_line_spec_num_show / 1000  # 主管宽 换算成m
                inner_rod_w = inner_rod_spec_num_show / 1000  # 内管宽25 换算成m
                inner_pipe_w = inner_pipe_spec_num/1000  # 内管 19

                extend_w = self.base_configs['set']['vertical_extend_max'] / 1000
                self.graphTool.draw_graph(input_width, input_height,
                                          horizontal_num, vertical_num,
                                          main_pipe_w,inner_rod_w,inner_pipe_w,
                                          extend_w,"竖式",
                                          out_line_spec_val,inner_rod_spec_val,inner_pipe_spec_val
                                          )

    #total_len 总长
    #out_line_width 外边框宽度
    #space_len 间距 100 或400
    #pipe_width 管宽度
    def on_calcute_result(self,total_len,out_line_width,space_len,pipe_width):
        #除数
        divisor = total_len-2*out_line_width-space_len
        dividend = space_len+pipe_width
        result=divisor/dividend
        return result

    # 填充
    def fill_rich_txt(self,out_line_spec_val,measure_h_float_result_extend,measure_w_float,
                      inner_rod_spec_val,measure_h_rod_float_result,inner_rod_count,inner_pipe_spec_val,
                      measure_w_pipe_float_result,inner_pipe_count):
        show_f_txt = "外框 " + out_line_spec_val + " 方管：" + str(measure_h_float_result_extend) + "mm X 2 \n" \
                                                                                               "\t\t" + str(
            measure_w_float) + "mm X 2\n" \
                               "内杆 " + inner_rod_spec_val + " 方管：" + str(measure_h_rod_float_result) + "mm X " + str(
            math.ceil(inner_rod_count)) + "\n" \
                                          "内管 " + inner_pipe_spec_val + "：" + str(
            measure_w_pipe_float_result) + "mm X " + str(math.ceil(inner_pipe_count))
        self.show_rich_txt.SetValue(show_f_txt)


        #外框选择
    def on_out_line_spec_Box_selected(self,event):
        _create_log_file("外框选择")


    #内杆规格
    def on_inner_rod_spec_Box_selected(self,event):
        _create_log_file("内杆规格")


    #内管规格
    def on_inner_pipe_spec_Box_selected(self,event):
        _create_log_file("内管选择")
    #类型选择
    def on_window_category_Box_selected(self,event):
        _create_log_file("类型选择")




    #画模型图
    def draw_model(self):
        np.random.seed(1000)
        y = np.random.standard_normal(10)
        print( "y = %s" % y)

        x = range(len(y))
        print("x=%s" % x)

        plt.plot(y)
        plt.grid(True)##增加格点
        plt.axis('tight')
        plt.show()


        #输入长宽只能为正整数或者小数
    def is_number(self,val):
        compilestr=re.compile(r'^([1-9]\d*|0)(\.\d{1,2})?$')
        result=compilestr.match(val)
        if result:
            _create_log_file("数字")
        else:
            _create_log_file("非法字符")
        return result
    # 生成注册文件
    def registFileDialog(self,event):
        dlg = wx.TextEntryDialog(self, '输入加密文', 'Text Entry Dialog')
        if dlg.ShowModal() == wx.ID_OK:
            send_encryptkey=dlg.GetValue()
            _create_file(send_encryptkey)

        dlg.Destroy()
    # 上传注册文件
    def uploadFile_FUN(self, event):
        fileFilter="Dicom (*.dcm)|*.dcm|" "All files (*.*)|*.*"
        fileDialog=wx.FileDialog(self,message="选择证书文件", wildcard=fileFilter, style = wx.FD_OPEN)
        dialogResult=fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        path=fileDialog.GetPath()
        fileDialog.Destroy()
        _create_log_file("文件地址：" + path)
        isusing=_is_using(path)
        if isusing:
            self.show_message("认证成功,请重新打开", None, False)
        else:
            self.show_message("请确认认证文件是否正确", None, False)


    def on_but_register(self, event):
        # 类似上上面的查询，只需获取相关内容插入到数据库就可以做出相关的操作
        # 内容与上面内容相似，不再经行书写
        pass


    def init_isused(self):
        mac = _get_element_by_tag("mac")
        nowmac=hmac_encrypt(self.machine_info)
        if  nowmac!= mac:
            _update_element_val("isregisted", 0)
            self.show_message("如果切换电脑请重新申请", None, False)

        self.isregisted = _get_element_by_tag("isregisted")
        if self.isregisted == "1":

            self.newitem.Enable(False)
            self.uploadfileitem.Enable(False)
            # self.registfile.Enable(False)
            self.calcu_btn.Enable(True)
        elif self.isregisted == "0":
            self.newitem.Enable(True)
            self.uploadfileitem.Enable(True)
            # self.registfile.Enable(True)
            self.calcu_btn.Enable(False)



    # 输入手机号
    def regist_gui(self,event):
        macnumber=_get_machine_message()
        regisnumber=_get_time_stamp13()

        dlg=RegistDialog(self.registFunc,macnumber,regisnumber)
        dlg.Show()
    # 关闭事件
    def ui_closed(self,event):
        ret = wx.MessageBox('是否关闭', '是', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            # do something here...
            event.Skip()

    def onclose(self,event):
        self.Close()


    # 回调函数  获取注册使用的信息
    def registFunc(self,phonenumber,secretkey):
        _create_log_file(phonenumber)
        _create_log_file(secretkey)




class RegistDialog(registDialog.RegistUI):
    def __init__(self, func_callBack, macnumber,registtime):
        registDialog.RegistUI.__init__(self, '注册使用页面', func_callBack, macnumber,registtime)












if __name__=="__main__":
    app=CalculatorGui()
    app.show_window()
    app.MainLoop()




