import wx
import sys
import wx.grid
from wx.lib.pubsub import pub
sys.path.insert(0,"/home/je/Documents/PointOfSales/saPos")
from manageProduct import manageProduct

manage = manageProduct()


class searchProduct(wx.Dialog):

	def __init__(self, parent, title):
	
		super(searchProduct, self).__init__(parent, title=title, size=(900,450))
		self.InitUI()
		self.Centre()
		self.Show()
		self.Bind(wx.EVT_CLOSE, self.onClose)
		pub.subscribe(self.getCurrentProductList, "currentProductList")
		self.checkWithBarcode=[]
		
	def InitUI(self):
		
		self.goods=[]
		
		panel = wx.Panel(self)
		panel.SetBackgroundColour('#607d8b')
		vbox = wx.BoxSizer(wx.VERTICAL)
		gbs = wx.GridBagSizer(10,20)
		bsgrid = wx.BoxSizer(wx.VERTICAL)
		gbsButton = wx.GridBagSizer(10,10)
		
		stCode = wx.StaticText(panel, label='Code')
		stCode.SetForegroundColour('white')
		stCode.SetBackgroundColour('black')
		
		stName = wx.StaticText(panel, label='Name')
		stName.SetForegroundColour('white')
		stName.SetBackgroundColour('black')
		

		tcCode = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(200,-1))
		self.tcCode = tcCode
		self.tcCode.Bind(wx.EVT_KEY_DOWN, self.onSearchProductCodeLike)
		
		tcName = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(200,-1))
		self.tcName = tcName
		self.tcName.Bind(wx.EVT_KEY_DOWN, self.onSearchProductNameLike)
		
		gbs.AddMany([ (stCode,(1,2)), (stName,(1,3)), (tcCode,(2,2)), (tcName,(2,3)) ])
		
		attr = wx.grid.GridCellAttr()
		attr.SetReadOnly(True)
		self.attr= attr
		posGrid = wx.grid.Grid(panel,size=(840,300))
		posGrid.CreateGrid(100,4)
		
		for i in range (0, posGrid.GetNumberCols()):
			posGrid.SetColAttr(i, attr)
		
		posGrid.SetLabelBackgroundColour('#efebe9')
		posGrid.SetColLabelValue(0,'Barcode')
		posGrid.SetColLabelValue(1,'Code')
		posGrid.SetColLabelValue(2,'Name')
		posGrid.SetColLabelValue(3,'Price')
		posGrid.SetRowLabelSize(0)
		posGrid.SetColSize(0,150)
		posGrid.SetColSize(1,150)
		posGrid.SetColSize(2,340)
		posGrid.SetColSize(3,200)
		bsgrid.Add(posGrid)
		
		cancelButton = wx.Button(panel, label='&Cancel')
		cancelButton.Bind( wx.EVT_BUTTON, self.onClose)
		okButton = wx.Button(panel, label='&OK')
		okButton.SetForegroundColour('black')
		okButton.SetBackgroundColour('yellow')
		okButton.Bind( wx.EVT_BUTTON, self.onOkFinalChoose)
		
		gbsButton.AddMany([ (cancelButton,(0,29), wx.DefaultSpan, wx.TOP|wx.BOTTOM,20),(okButton,(0,30), wx.DefaultSpan, wx.TOP|wx.BOTTOM,20) ])
		
		vbox.AddMany([ (gbs),(bsgrid,1,wx.TOP|wx.LEFT|wx.RIGHT,30), (gbsButton) ])
		
		panel.SetSizerAndFit(vbox)
		
		posGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.onSingleSelect)
		posGrid.Bind(wx.EVT_KEY_DOWN, self.GridOnEnter)
		self.posGrid = posGrid
		self.pastRowExist= False
		self.pastRow=0
	
	
	def onSearchProductCodeLike(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
				manage.searchProductCodeLike(self.tcCode.GetValue())				
				self.setDataInGrid()
				self.posGrid.SetFocus()
		else:
			event.Skip()

	def onSearchProductNameLike(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
				manage.searchProductNameLike(self.tcName.GetValue())			
				self.setDataInGrid()
				self.posGrid.SetFocus()
		else:
			event.Skip()
			
	def clearGrid(self):
		for ii in xrange(100):
			for i in range(4):
				self.posGrid.SetCellValue(ii,i,str(''))	

	def setDataInGrid(self):
		self.clearGrid()
		data = manage.getProduct()
		for ii in xrange(len(data)):
			for i in range(4):
				self.posGrid.SetCellValue(ii,i,str(data[ii][i]))	
		manage.setMyProductEmpty()
	
	def onClose(self, event):
		self.Destroy()
		
	
	def onOkFinalChoose(self, event):
		#print self.goods[0]
		if len(self.checkWithBarcode)==0:
			pub.sendMessage("sendingGoodsData", message=self.goods)

		elif self.goods[0] in self.checkWithBarcode:
			wx.MessageBox('sorry, product have been choosen!', 'Warning', wx.OK | wx.ICON_WARNING)
			
			
		else:
			pub.sendMessage("sendingGoodsData", message=self.goods)
		
		self.onClose(event=None)	
	
	
	def getCurrentProductList(self, message):
		if len(message)!=0:
			for i in range(len(message)):
				self.checkWithBarcode.append((message[i]))		
		#print self.checkWithBarcode
		
		
	def onSingleSelect(self, event):
		selectedData = []
		currentRow = event.GetRow()
	#	print 'selected row= '+ str(currentRow)	

		for col in range(4):
			selectedData.append(str(self.posGrid.GetCellValue(currentRow,col)))
			self.posGrid.SetCellBackgroundColour(currentRow,col,'#fff59d')
		self.goods = selectedData
		self.tcCode.SetValue(selectedData[1])
		self.tcName.SetValue(selectedData[2])
		self.posGrid.ForceRefresh()
		if self.pastRowExist==True:
			self.defaultGrid(self.pastRow)
			
		self.pastRowExist= True
		self.pastRow = currentRow	
		
	
	def defaultGrid(self, pastRow):
		if self.pastRowExist==True:
			for col in range(4):
				self.posGrid.SetCellBackgroundColour(pastRow,col,'white')
			self.posGrid.ForceRefresh()

	
	def GridOnEnter(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
			event.EventObject.Navigate()
			event.EventObject.Navigate()
		else:
			event.Skip()


def main():

	app = wx.App()
	searchProduct(None, title='Search Product')
	app.MainLoop()
	
if __name__=='__main__':
	main()
		
