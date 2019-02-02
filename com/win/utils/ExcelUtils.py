# -*- coding: utf-8 -*-

import xlsxwriter
from ProjectURL import _get_project_dir
from com.win.utils.DateUtils import _get_date_formate_unline,_get_date_for_mounth

class ExcelUtils():


    def __init__(self):
        pass

    #  获取路径私有方法
    def __get_path(self):
        path = _get_project_dir() + "\\xlsresource\\"
        pathtm="E:\\Pythonwork\\GUIProject\\xlsresource\\"
        return pathtm

    #  根据事件生成Excel数据
    def __get_Xls_Name(self):
        filename=_get_date_formate_unline()
        return filename

    # 设置表头样式
    def __get_title_style(self,wb):
        merge_formate = wb.add_format({
            'bold': True,
            'border': 6,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': 'red'
            # 'fg_color:':'#D7E4BC'
        })
        merge_formate.set_bg_color('green')
        return merge_formate
    # 设置表头样式
    def __get_header_style(self,wb):
        headerstyle=wb.add_format({'bold': True,
                                   'border':1
                                   })  # 表头样式
        headerstyle.set_size(12)
        headerstyle.set_border_color("black")
        return headerstyle


    # 生成Excel 操作
    def createExcel(self):
        xlsfile=self.__get_path()+_get_date_for_mounth()+".xls"
        # xlsfiledir=open(xlsfile,mode='a',encoding='utf-8')
        workbook=xlsxwriter.Workbook(xlsfile) # 创建Excel
        sheetname=self.__get_Xls_Name()
        # 判断是否已存在shestname
        isincludesheetname=workbook.get_worksheet_by_name(sheetname)

        worksheet=workbook.add_worksheet(sheetname)



        # 画表头
        merge_formate=self.__get_title_style(workbook)
        worksheet.set_row(0, 70)
        worksheet.set_row(1, 50)#设置行 高
        worksheet.set_column('A1:A1',100)
        worksheet.merge_range('A1:I1','设置表头',merge_formate)

        # 列设置
        bold=self.__get_header_style(workbook)

        worksheet.write('A2','测量长度',bold)
        worksheet.write('B2','测量宽度',bold)
        worksheet.write('C2','外框规格',bold)
        worksheet.write('D2', '内杆规格', bold)
        worksheet.write('E2', '内管规格', bold)
        worksheet.write('F2', '款式选择', bold)
        worksheet.write('G2', '外框', bold)
        worksheet.write('H2', '内杆', bold)
        worksheet.write('I2', '内管', bold)

        floatformate=workbook.add_format({'num_format':'$#,##0'})#列格式 float类型
        row = 2
        col = 9
        datas=(
            ['1200','1140','25X25','25X25','方形19X19','横式','外框 25 X 25 方管：1160.0mm X 2 \n  1200.0mm X 2','1090.0mm X 2','1170.0mm X 9']
        )
        i=0
        while i < col:
            worksheet.write(row,i,datas[i])
            i=i+1

        workbook.close()


if __name__ == '__main__':
    xlsUtls=ExcelUtils()
    xlsUtls.createExcel()






