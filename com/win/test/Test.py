# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pyplotz.pyplotz import PyplotZ

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator = MultipleLocator(0.5)  # 将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
xminorLocator = MultipleLocator(0.1)  # 将x轴次刻度标签设置为5的倍数

ymajorLocator = MultipleLocator(0.5)  # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数
plt.figure(figsize=(10, 10))#设置显示大小
import matplotlib
from pylab import mpl
# pltz=PyplotZ()
# pltz.enable_chinese()
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
ax =plt.subplot(111)  # 注意:一般都在ax中设置,不再plot中设置

#横着24 间隔:0.125    垂直6  间隔0.5

horizontal_space=3/7
vertical_space=3/25
for i in range(0,8):
    point_x=i*horizontal_space
    if i==0:
        plt.plot([point_x, point_x], [0, 3], color="red", linewidth=3.0, linestyle="-", label='横截面规格：25 X 13')
        plt.plot([point_x, point_x], [0, -0.3], color="red", linewidth=0.5, linestyle="--")#延长水平方向
        plt.plot([-0.2, -0.2], [0, vertical_space], color="red", linewidth=0.5, linestyle="-")#画垂直线
        plt.text(-0.2, vertical_space/2-0.03, "误差：90-100mm", ha='center', va='bottom', fontsize=8, rotation=0)
    elif i==1:
        plt.plot([point_x, point_x], [0, 3], color="red", linewidth=3.0, linestyle="-")
        plt.plot([point_x, point_x], [0, -0.3], color="red", linewidth=0.5, linestyle="--")#延长水平方向

    else:
        plt.plot([point_x, point_x], [0, 3], color="red", linewidth=3.0, linestyle="-")


#水平方向
for i in range(0,26):
    ponit_y=i*vertical_space
    if i==0:
        plt.plot([0, 3], [ponit_y, ponit_y], color="blue", linewidth=1.0, linestyle="-", label='横截面规格：19 X 19')
        plt.plot([0, horizontal_space], [-0.2, -0.2], color="blue", linewidth=0.5, linestyle="--")#画水平线
        plt.plot([-0.3, 0], [0, 0], color="blue", linewidth=0.5, linestyle="--")#延长垂直方向线
        plt.text(horizontal_space / 2, -0.2, "误差：300-400mm", ha='center', va='bottom', fontsize=8, rotation=0)
    elif i==1:
        plt.plot([0, 3], [ponit_y, ponit_y], color="blue", linewidth=1.0, linestyle="-")
        plt.plot([-0.3, 0], [ponit_y, ponit_y], color="blue", linewidth=0.5, linestyle="--")#延长垂直方向线
    else:
        plt.plot([0, 3], [ponit_y, ponit_y], color="blue", linewidth=1.0, linestyle="-")




# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

# 显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
#设置
plt.ylim(-0.5,3.5)
plt.xlim(-0.5,3.1)

# ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度

# ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
plt.legend(loc=0)
# plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')
plt.show()