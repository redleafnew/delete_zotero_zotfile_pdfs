# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"清除已经删除文献的PDF附件", pos = wx.DefaultPosition, size = wx.Size( 764,243 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.Add( ( 5, 5), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.select_exported_dir = wx.DirPickerCtrl( self, wx.ID_ANY, u"请选择包含导出文件的目录", u"请选择包含导出文件的目录", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer2.Add( self.select_exported_dir, 1, wx.ALL, 5 )

		self.select_dest_dir = wx.DirPickerCtrl( self, wx.ID_ANY, u"请选择包含PDF附件的目录", u"请选择包含PDF附件的目录", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer2.Add( self.select_dest_dir, 1, wx.ALL, 5 )

		self.m_delete = wx.Button( self, wx.ID_ANY, u"删除PDF文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_delete, 0, wx.ALL, 5 )

		self.m_exit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_exit, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 2, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"使用说明：\n此小程序为使用了Zotfile插件后，将PDF统一放到一个文件夹中才适用。原理是删除文献后，会先存到Trash文件夹，在清空Trash前，将此文件夹中的文献导出，读取其中的PDF附件，然后再将PDF附件目录中相应的PDF删除。使用步骤如下：\n1.在Zotero中点击Trash后，点击右侧第一条记录，按住Shift的同时，再点击最后一条记录。\n2.右击，选择Export Items...。\n3. Format选择Zotero RDF，Translator Options中选中Export Files。点击OK，放在自己能记住的位置，一会儿会用到这个位置。\n4. 点击第一个Browse，选择3中的位置。点击第二个Browse，选中存放PDF的文件夹（在Zotfile中指定的）。\n5. 点击删除PDF文件按钮，会删除在Zotfile中指定的统一存放PDF的文件夹中的PDF附件。\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 5), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 3, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_delete.Bind( wx.EVT_BUTTON, self.del_PDFS )
		self.m_exit.Bind( wx.EVT_BUTTON, self.onExit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def del_PDFS( self, event ):
		event.Skip()

	def onExit( self, event ):
		event.Skip()


