import wx
import wx.grid
from paywith import paywith

class payment(wx.Dialog):

	def __init__(self, parent, title):
	  
		super(payment, self).__init__(parent, title=title, size=(750,480))
		self.InitUI()
		self.Centre()
		self.Show()
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		
	def InitUI(self):
	
		panel = wx.Panel(self)
		panel.SetBackgroundColour('#607d8b')
		vbox = wx.BoxSizer(wx.VERTICAL)
		gbs = wx.GridBagSizer(10,19)
		bsgrid = wx.BoxSizer(wx.VERTICAL)
		gbsshortkey = wx.GridBagSizer(10,10)
		fgsfield = wx.FlexGridSizer(6,2,0,18)
		gbsbottom = wx.GridBagSizer(0,10)
		gbsButton = wx.GridBagSizer(10,10)
		
		stTotalSale = wx.StaticText(panel, label='Total Sale')
		stTotalSale.SetForegroundColour('white')
		stTotalSale.SetBackgroundColour('black')
		tcTotalSale = wx.TextCtrl(panel, size=(200,-1))
		tcTotalSale.SetBackgroundColour('#efebe9')
		tcTotalSale.SetForegroundColour('#3e2723')
		tcTotalSale.SetEditable(False)
		
		gbs.AddMany([ (stTotalSale,(1,10),wx.DefaultSpan,wx.TOP,5),(tcTotalSale,(1,11), wx.DefaultSpan, wx.BOTTOM, 5) ])
		

		attr = wx.grid.GridCellAttr()
		attr.SetReadOnly(True)
		posGrid = wx.grid.Grid(panel,size=(740,157))
		posGrid.CreateGrid(100,3)
		
		for i in range (0, posGrid.GetNumberCols()):
			posGrid.SetColAttr(i, attr)
		
		
		posGrid.SetLabelBackgroundColour('#fff59d')
		posGrid.SetColLabelValue(0,'Payment')
		posGrid.SetColLabelValue(1,'Amount')
		posGrid.SetColLabelValue(2,'Charge')

		posGrid.SetRowLabelSize(0)
		posGrid.SetColSize(0,345)
		posGrid.SetColSize(1,200)
		posGrid.SetColSize(2,145)
		posGrid.EnableDragColSize(False)
		posGrid.EnableDragRowSize(False)
		bsgrid.Add(posGrid)
		
		buttonf3 = wx.Button(panel,label='F3', size=(36,25))
		buttonf3.SetForegroundColour('white')
		buttonf3.SetBackgroundColour('#1976D2')
		buttonf4 = wx.Button(panel,label='F4', size=(36,25))
		buttonf4.SetForegroundColour('white')
		buttonf4.SetBackgroundColour('#1976D2')
		buttonf5 = wx.Button(panel,label='F5', size=(36,25))
		buttonf5.SetForegroundColour('white')
		buttonf5.SetBackgroundColour('#1976D2')
		
		stAdd = wx.StaticText(panel, label='Add')
		stAdd.SetForegroundColour('white')
		stAdd.SetBackgroundColour('black')
		stEdit = wx.StaticText(panel, label='Edit')
		stEdit.SetForegroundColour('white')
		stEdit.SetBackgroundColour('black')
		stDelete = wx.StaticText(panel, label='Delete')
		stDelete.SetForegroundColour('white')
		stDelete.SetBackgroundColour('black')
		
		stSalePayment = wx.StaticText(panel, label='Sale Payment')
		stSalePayment.SetForegroundColour('white')
		stSalePayment.SetBackgroundColour('black')
		stCharge = wx.StaticText(panel, label='Charge')
		stCharge.SetForegroundColour('white')
		stCharge.SetBackgroundColour('black')
		stTotalPayment = wx.StaticText(panel, label='Total Payment')
		stTotalPayment.SetForegroundColour('white')
		stTotalPayment.SetBackgroundColour('black')
		stToRefund = wx.StaticText(panel, label='To Refund')
		stToRefund.SetForegroundColour('white')
		stToRefund.SetBackgroundColour('black')
		stRounding = wx.StaticText(panel, label='Rounding')
		stRounding.SetForegroundColour('white')
		stRounding.SetBackgroundColour('black')		
		stRefund = wx.StaticText(panel, label='Refund')
		stRefund.SetForegroundColour('white')
		stRefund.SetBackgroundColour('black')
		
				
		tcSalePayment = wx.TextCtrl(panel, size=(200,-1))
		tcSalePayment.SetBackgroundColour('#efebe9')
		tcSalePayment.SetForegroundColour('#3e2723')
		tcSalePayment.SetEditable(False)
		tcCharge = wx.TextCtrl(panel, size=(200,-1))
		tcCharge.SetBackgroundColour('#efebe9')
		tcCharge.SetForegroundColour('#3e2723')
		tcCharge.SetEditable(False)
		tcTotalPayment = wx.TextCtrl(panel, size=(200,-1))
		tcTotalPayment.SetBackgroundColour('#efebe9')
		tcTotalPayment.SetForegroundColour('#3e2723')
		tcTotalPayment.SetEditable(False)
		tcToRefund = wx.TextCtrl(panel, size=(200,-1))
		tcToRefund.SetBackgroundColour('#efebe9')
		tcToRefund.SetForegroundColour('#3e2723')
		tcToRefund.SetEditable(False)
		tcRounding = wx.TextCtrl(panel, size=(200,-1))
		tcRounding.SetBackgroundColour('#efebe9')
		tcRounding.SetForegroundColour('#3e2723')
		tcRounding.SetEditable(False)
		tcRefund = wx.TextCtrl(panel, size=(200,-1))
		tcRefund.SetBackgroundColour('#efebe9')
		tcRefund.SetForegroundColour('#3e2723')
		tcRefund.SetEditable(False)
		
		gbsshortkey.AddMany([ (buttonf3,(0,0)), (stAdd,(0,1), wx.DefaultSpan, wx.TOP,5), (buttonf4,(1,0)),(stEdit,(1,1), wx.DefaultSpan, wx.TOP,5),(buttonf5,(2,0)),(stDelete,(2,1), wx.DefaultSpan, wx.TOP,5) ])
		
		fgsfield.AddMany([(stSalePayment, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5),(tcSalePayment),(stCharge, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcCharge), (stTotalPayment, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcTotalPayment), (stToRefund, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcToRefund), (stRounding, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcRounding), (stRefund, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcRefund)])		
		
		gbsbottom.AddMany([(gbsshortkey,(0,1),wx.DefaultSpan, wx.LEFT,10),(fgsfield,(0,8),wx.DefaultSpan, wx.BOTTOM,30)])
		
		cancelButton = wx.Button(panel, label='&Cancel')
		cancelButton.Bind( wx.EVT_BUTTON, self.OnClose)
		okButton = wx.Button(panel, label='&OK')
		okButton.SetForegroundColour('white')
		okButton.SetBackgroundColour('#1976D2')

		gbsButton.AddMany([ (cancelButton,(0,26)),(okButton,(0,27), wx.DefaultSpan, wx.BOTTOM,30) ])
		
		vbox.AddMany([ (gbs),(bsgrid,1,wx.LEFT|wx.RIGHT,30), (gbsbottom), (gbsButton) ])
	  
		panel.SetSizerAndFit(vbox)
		
		id_F3 = wx.NewId()
		id_F4 = wx.NewId()
		id_F5 = wx.NewId()
		
		self.Bind(wx.EVT_MENU, self.presed_F3, id=id_F3)
		self.Bind(wx.EVT_MENU, self.presed_F3, id=id_F4)
		self.Bind(wx.EVT_MENU, self.presed_F3, id=id_F5)
		
		accel_tbl = wx.AcceleratorTable([	(wx.ACCEL_NORMAL, wx.WXK_F3, id_F3 ), (wx.ACCEL_NORMAL, wx.WXK_F4, id_F4 ), (wx.ACCEL_NORMAL, wx.WXK_F5, id_F5 )	])
		self.SetAcceleratorTable(accel_tbl)  
		
	def OnClose(self, event):
		self.Destroy()
		
	def presed_F3(self, event):
		paywith(None, title='Choose Payment Method')
	  
def main():

	app = wx.App()
	payment(None, title='Payment')
	app.MainLoop()
	
if __name__=='__main__':
	main()
	
	  
