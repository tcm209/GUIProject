# -*- coding: utf-8 -*-
import com.win.client.CalculatorGui as calcuteFrame
import com.win.client.RegistUI as registUI

class ManagerGUI(object):

    def __init__(self,UpdateUI):
        self.UpdateUI=UpdateUI
        self.frameDict={}# 存放已创建FRAME

    # 获取frame对象 已存在  获取 不存在 创建
    def get_frame(self,type):
        frame=self.frameDict.get(type)

        if frame is None:
            frame = self.create_frame(type)
            self.frameDict[type]=frame

        return frame
    # 创建 frame ui
    def create_frame(self,type):
        if type == 0:
            return calcuteFrame.CalculatorGui(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 1:
            return registUI.RegistUI(parent=None, id=type, UpdateUI=self.UpdateUI)


