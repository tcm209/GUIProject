# -*- coding: utf-8 -*-
import wx
import com.win.client.ManagerGUI as frameManager

# 程序入口
class MainWX(wx.App):

    def OnInit(self):
        self.manager=frameManager.ManagerGUI(self.update_ui)
        self.frame=self.manager.get_frame(0)
        self.frame.Show()
        return True


    def update_ui(self,type):
        self.frame.Show(False)
        self.frame=self.manager.get_frame(type)
        self.frame.Show(True)

def main():
    app=MainWX()
    app.MainLoop()

if __name__=="__main__":
    main()