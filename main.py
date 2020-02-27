# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:21:53 2020

@author: 
"""

import GUI
import wx
import os.path
from os import walk
import os


class delPDFs(GUI.MyFrame1):
    def __init__(self,parent):
            GUI.MyFrame1.__init__(self,parent)  

    #退出按钮
    def onExit( self, event ):
            frame.Destroy()
    #删除PDF按钮
    def del_PDFS( self, event ):
		#event.Skip()
        path = self.select_exported_dir.GetPath()  #得到导出的文件路径
        path_d = self.select_dest_dir.GetPath() #得到存放PDF文件的目录
        #列出所有文件
        for (dirpath, dirnames, filenames) in walk(path):
            for file_name in filenames:
                if file_name.endswith('rdf') == False:
                    del_file = os.path.join(path_d, file_name)
                    #判断文件是否存在
                    if os.path.exists(del_file):
                        os.remove(del_file) #删除文件
                        print('%s已删除' %del_file)
                    else:
                        print("%s不存在！" %del_file)


app = wx.App(False)
frame = delPDFs(None)
frame.Show(True)
#start the applications
app.MainLoop()