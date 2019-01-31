# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter
from pylab import mpl
from ProjectURL import _get_project_dir
import time
import os

class GraphUtils(object):

    def __init__(self):

        print("初始化参数")
        self.x_min = -1000
        self.y_min = -1000
        self.y_max = 3500
        self.x_max = 3500
        #  X轴基本设置
        self.x_majorLoc = MultipleLocator(1000)  # 将X主刻度标签设置为1000的倍数
        self.x_majorFor = FormatStrFormatter('%100.0f')  # 设置X标签文本的格式
        self.x_minorLoc = MultipleLocator(100)  # 将x轴次刻度标签设置为5的倍数

        #  Y轴基本设置
        self.y_majorLoc = MultipleLocator(1000)  # 将Y轴主刻度标签设置为1000的倍数
        self.y_majorFor = FormatStrFormatter('%100.0f')  # 设置Y轴标签文本的格式
        self.y_minorLoc = MultipleLocator(100)  # 将Y轴此刻度标签设置为0.1的倍数

        #  设置中文汉字  避免中文乱码
        mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

        #  设置主副 宽度
        self.main_pipe_bold = 10.0  # 边框
        self.vertical_pipe_bold = 1.0  # 垂直方向线条宽度
        self.horizontal_pipe_bold = 1.0  # 水平方向线条宽度
        #  颜色
        self.mian_pipe_color = "red"  # 外框颜色
        self.vertical_pipe_color = "blue"  # 垂直方向颜色
        self.horizontal_pipe_color = "red"  # 水平颜色
        self.inner_rod_color = ""
        self.w_min = 18 # 主框宽度引起的微差
        # self.h_min = 15  # 主框宽度引起的微差
        #  虚线颜色
        self.dashed_color = "black"
        self.dashed_color_h = "red"
        self.dashed_color_v = "blue"
        # 读取文件配置
        self.project_dir=_get_project_dir()
        # 设置文字大小
        self.txt_font_size = 12
        self.font_style = {
            'style':'normal',
            'weight':'black',
            'size':'12'
        }
        # 文字方向
        self.h_rotation = 0
        self.v_rotation = 90
    # 输入长: input_width 3
    #  输入宽: input_height 3
    #  水平数量: horizontal_num 26
    #  垂直数量: vertical_num 8
    #  主管宽：main_pipe_w 25
    #  内管宽：inner_pipe_w 19
    #  内杆宽 inner_rod_w
    #  extend_w 垂直方向需要延长
    #  category 款式分类 竖式 横式
    #  out_line_spec 外框规格
    #  inner_rod_spec 内杆规格
    #  inner_pipe_spec 内管规格 最细
    def draw_graph(self,input_width,input_height,horizontal_num,vertical_num,main_pipe_w,inner_rod_w,inner_pipe_w,extend_w,category,out_line_spec,inner_rod_spec,inner_pipe_spec):


        if category == "竖式":
            self.horizontal_pipe_bold = 7.0
            self.vertical_pipe_bold=1.0
            self.vertical_pipe_color = "blue"
            self.horizontal_pipe_color = "red"
            self.dashed_color_h = "red"
            self.dashed_color_v = "blue"
            self.pipe_horizontal=inner_rod_w
            self.pipe_vertical=inner_pipe_w
            self.inner_rod_count=horizontal_num
            self.inner_pipe_count=vertical_num



        elif category == "横式":
            self.horizontal_pipe_bold = 1.0
            self.vertical_pipe_bold = 7.0
            self.vertical_pipe_color = "red"
            self.horizontal_pipe_color = "blue"
            self.dashed_color_h = "blue"
            self.dashed_color_v = "red"
            self.pipe_horizontal = inner_pipe_w
            self.pipe_vertical = inner_rod_w
            self.inner_rod_count = vertical_num
            self.inner_pipe_count = horizontal_num


        plt.figure(figsize=(20,20))#设置显示图大小
        ax=plt.subplot(111)#注意 ax设置不再试用plot中设置
        ##############开始画图#################
        #间距
        h_num_extend_h=input_height+extend_w
        mm_h_num_extend_h=h_num_extend_h*1000
        h_num=horizontal_num-1
        v_num=vertical_num-1

        # 坐标轴 垂直线间距
        vertical_space = input_height / h_num
        # 坐标轴 水平线间距
        horizontal_space = input_width / v_num

        # 真实值 垂直线间距
        vertical_length= self.get_space_length(input_width, main_pipe_w, v_num, self.pipe_vertical)
        # 真是值 水平线间距
        horizontal_length= self.get_space_length(input_height,main_pipe_w,h_num,self.pipe_horizontal)

        # 画垂直线
        for i in range(0,vertical_num):
            point_x=i*horizontal_space
            mm_point_x=point_x*1000
            if i == 0:
                plt.plot([mm_point_x, mm_point_x], [0, mm_h_num_extend_h], color=self.mian_pipe_color, linewidth=self.main_pipe_bold, linestyle="-", label='规格：S= '+out_line_spec+"； Number = 4")
                #垂直虚线
                plt.plot([mm_point_x-self.w_min,mm_point_x-self.w_min], [0-2*self.w_min, -450], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 垂直 第一根延长虚线 黑线
                # plt.plot([mm_point_x, mm_point_x ], [0, -0.3], color="red", linewidth=0.5,linestyle="--")  # 垂直 第一根延长虚线
                # plt.plot([mm_point_x + self.w_min, mm_point_x + self.w_min], [0, -0.15], color="red", linewidth=0.5,linestyle="--")  # 垂直 第一根延长虚线

                # 垂直红线
                plt.plot([-100, -100], [0, vertical_space*1000-self.w_min], color=self.dashed_color_v, linewidth=0.5, linestyle="-")  # y=0.1      画垂直线 水平间距

                plt.plot([-200, -200], [0-self.w_min, input_height*1000], color=self.dashed_color_v, linewidth=0.5,linestyle="-")  # y=0.1      画垂直线 水平间距
                plt.plot([-400, -400], [0-1.5*self.w_min, mm_h_num_extend_h], color=self.mian_pipe_color, linewidth=0.5, linestyle="-")  #y=长度+延长 画垂直线 总长度
                #  标识单个间隔
                plt.text(-150, 0,
                         "L="+str(round(horizontal_length, 2))+"mm",
                         ha='left',
                         va='bottom',
                         fontdict=self.font_style,
                         rotation=self.v_rotation
                         )
                # 标识延长长度
                plt.text(-450, mm_h_num_extend_h / 2,
                         "L=" + str(round(mm_h_num_extend_h,2)) + "mm",
                         ha='left',
                         va='bottom',
                         fontdict=self.font_style,
                         rotation=self.v_rotation
                         )
                #  标识标准长度
                plt.text(-250, mm_h_num_extend_h / 2-100,
                         "L=" + str(round(input_height*1000,2)) + "mm",
                         ha='left',
                         va='bottom',
                         fontdict=self.font_style,
                         rotation=self.v_rotation
                         )  # 标识总长

            elif i == 1:
                if category == "竖式":
                    plt.plot([mm_point_x, mm_point_x], [0, input_height*1000], color=self.vertical_pipe_color, linewidth=self.vertical_pipe_bold, linestyle="-", label='规格：S= '+inner_pipe_spec+"； Number = "+str(self.inner_pipe_count-2))
                elif category == "横式":
                    plt.plot([mm_point_x, mm_point_x], [0, input_height*1000], color=self.vertical_pipe_color,linewidth=self.vertical_pipe_bold, linestyle="-", label='规格：S= '+inner_rod_spec+'； Number = '+str(self.inner_rod_count-2))
                plt.plot([mm_point_x, mm_point_x], [0-self.w_min, -150], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 垂直 第二条线延长
            elif i == v_num:
                #  延长最后一根线
                plt.plot([mm_point_x, mm_point_x], [0, mm_h_num_extend_h], color=self.mian_pipe_color, linewidth=self.main_pipe_bold, linestyle="-")#

                #  y=3虚线
                plt.plot([0, -250], [input_height*1000+self.w_min, input_height*1000+self.w_min], color=self.dashed_color, linewidth=0.5, linestyle="--")
                #  y=3.02虚线
                plt.plot([0, -450], [mm_h_num_extend_h+self.w_min, mm_h_num_extend_h+self.w_min], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 延长水平方向
            else:
                plt.plot([mm_point_x, mm_point_x], [0, input_height*1000], color=self.vertical_pipe_color, linewidth=self.vertical_pipe_bold, linestyle="-")

        #画水平线
        for i in range(0, horizontal_num):
            ponit_y = i * vertical_space
            mm_point_y=ponit_y*1000
            if i == 0:
                plt.plot([0, input_width*1000], [mm_point_y-self.w_min, mm_point_y-self.w_min], color=self.mian_pipe_color, linewidth=self.main_pipe_bold, linestyle="-")
                #水平蓝虚线
                plt.plot([0, horizontal_space*1000-self.w_min], [-100, -100], color=self.dashed_color_h, linewidth=0.5, linestyle="-")  # 画水平线
                plt.text(horizontal_space*1000 / 2, -100,
                         "L=" + str(round(vertical_length,2)) + "mm",
                         ha='center',
                         va='bottom',
                         fontdict=self.font_style,
                         rotation=self.h_rotation
                         )

                plt.plot([0, input_width*1000 - 1.5*self.w_min], [-200, -200], color=self.dashed_color_h, linewidth=0.5,
                         linestyle="-")
                plt.text(input_width*1000 / 2, -400,
                         "L=" + str(round(input_width*1000,2)) + "mm",
                         ha='center',
                         va='bottom',
                         fontdict=self.font_style,
                         rotation=self.h_rotation
                         )

                plt.plot([0, input_width*1000 ], [-400, -400], color=self.mian_pipe_color, linewidth=0.5,
                         linestyle="-")
                plt.text(input_width*1000 / 2-100, -200,
                         "L=" + str(round(input_width*1000-20,2)) + "mm",
                         ha='center',
                         va='bottom',
                         fontdict=self.font_style,
                         rotation=self.h_rotation
                         )

                # 水平方向第一根虚线
                plt.plot([-450, 0-self.w_min], [0-2*self.w_min, 0-2*self.w_min], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 水平第条延长虚线

            elif i == 1:
                if category == "竖式":
                    plt.plot([0, input_width*1000], [mm_point_y, mm_point_y], color=self.horizontal_pipe_color, linewidth=self.horizontal_pipe_bold, linestyle="-",label='规格：S= '+inner_rod_spec+'； Number = '+str(self.inner_rod_count-2))
                elif category == "横式":
                    plt.plot([0, input_width*1000], [mm_point_y, mm_point_y], color=self.horizontal_pipe_color, linewidth=self.horizontal_pipe_bold, linestyle="-", label='规格：S= '+inner_pipe_spec+'； Number = '+str(self.inner_pipe_count-2))
                plt.plot([-150, 0], [mm_point_y, mm_point_y], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 延长垂直方向线
            elif i == h_num:
                # 正常最后一根线
                plt.plot([0, input_width*1000], [mm_point_y, mm_point_y], color=self.mian_pipe_color, linewidth=self.main_pipe_bold, linestyle="-")
                # 垂直延长线

                plt.plot([input_width*1000+self.w_min, input_width*1000+self.w_min], [-450, 0-self.w_min], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 延长垂直方向线
                plt.plot([input_width*1000-self.w_min, input_width*1000-self.w_min], [-300, 0-self.w_min], color=self.dashed_color, linewidth=0.5, linestyle="--")  # 延长垂直方向线

            else:
                plt.plot([0, input_width*1000], [mm_point_y, mm_point_y], color=self.horizontal_pipe_color, linewidth=self.horizontal_pipe_bold, linestyle="-")

        # #############结束画图#################

        #设置主刻度标签的位置 ，标签文本的格式
        ax.xaxis.set_major_locator(self.x_majorLoc)
        ax.xaxis.set_major_formatter(self.x_majorFor)

        ax.yaxis.set_major_locator(self.y_majorLoc)
        ax.yaxis.set_major_formatter(self.y_majorFor)

        # 显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(self.x_minorLoc)
        ax.yaxis.set_minor_locator(self.y_minorLoc)

        #设置x y轴边界值y
        plt.ylim(self.y_min,self.y_max)
        plt.xlim(self.x_min,self.x_max)

        plt.legend(loc=0)
        plt.xlabel('长（mm）')
        plt.ylabel('宽（mm）')
        plt.title('模型图 S：横截面面积；Number：根数；L：间距',fontsize='20',fontweight='bold')
        # plt.show()

        # 保存图片位置
        img_save_file_url = self.project_dir+"\\images\\"
        filename=self.get_filename(input_width,input_height)
        path=img_save_file_url+filename
        print(path)
        plt.savefig(path, format='png', bbox_inches='tight', transparent=True, dpi=100)

        os.system(path)
    # 文件保存路径
    def get_filename(self,mode_w,mode_h):
        now = int(round(time.time() * 1000))
        nowformate=time.strftime('%Y-%m-%d',time.localtime(now/1000))
        filename=str(nowformate)+"_"+str(mode_w)+"x"+str(mode_h)+"_"+str(now)+".png"
        return filename

    # input_length : 输入长度
    # out_line_length ：外宽长度
    # num 根数
    # inner_pipe_length ：内管宽度
    def get_space_length(self,input_length,out_line_length,num,inner_pipe_length):
        divisor = input_length - 2 * out_line_length - (num-1) * inner_pipe_length
        dividend = num
        space_length=1000*(divisor/dividend)
        return space_length




if __name__=="__main__":
    graph=GraphUtils()
    graph.draw_graph(2,1.5,14,6,0.025,0.019,0.02)
