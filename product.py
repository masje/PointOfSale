import wx
import wx.grid


class product(wx.Frame):

	def __init__(self, parent, title):
	  
		super(product, self).__init__(parent, title=title, size=(1000,700))
		self.InitUI()
		self.Centre()
		self.Show()

		
	def InitUI(self):
	
		panel = wx.Panel(self)
		panel.SetBackgroundColour('#607d8b')
		vbox = wx.BoxSizer(wx.VERTICAL)
		bsgrid = wx.BoxSizer(wx.VERTICAL)
		fgsfield = wx.FlexGridSizer(6,2,0,18)
		gbsbottom = wx.GridBagSizer(0,10)
		gbsButton = wx.GridBagSizer(10,10)

		attr = wx.grid.GridCellAttr()
		attr.SetReadOnly(True)
		posGrid = wx.grid.Grid(panel,size=(950,400))
		posGrid.CreateGrid(100,8)
		
		for i in range (0, posGrid.GetNumberCols()):
			posGrid.SetColAttr(i, attr)
		
		
		posGrid.SetLabelBackgroundColour('#fff59d')
		posGrid.SetColLabelValue(0,'id')
		posGrid.SetColLabelValue(1,'bcode')
		posGrid.SetColLabelValue(2,'code')
		posGrid.SetColLabelValue(3,'name')
		posGrid.SetColLabelValue(4,'ppn')
		posGrid.SetColLabelValue(5,'price')
		posGrid.SetColLabelValue(6,'sellable')
		posGrid.SetColLabelValue(7,'active')
		
		posGrid.SetRowLabelSize(0)
		posGrid.SetColSize(0,50)
		posGrid.SetColSize(1,150)
		posGrid.SetColSize(2,150)
		posGrid.SetColSize(3,200)
		posGrid.SetColSize(5,150)
		
		posGrid.EnableDragColSize(False)
		posGrid.EnableDragRowSize(False)
		bsgrid.Add(posGrid)
		

		
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
		tcCharge = wx.TextCtrl(panel, size=(200,-1))
		tcCharge.SetBackgroundColour('#efebe9')
		tcCharge.SetForegroundColour('#3e2723')
		tcTotalPayment = wx.TextCtrl(panel, size=(200,-1))
		tcTotalPayment.SetBackgroundColour('#efebe9')
		tcTotalPayment.SetForegroundColour('#3e2723')
		tcToRefund = wx.TextCtrl(panel, size=(200,-1))
		tcToRefund.SetBackgroundColour('#efebe9')
		tcToRefund.SetForegroundColour('#3e2723')
		tcRounding = wx.TextCtrl(panel, size=(200,-1))
		tcRounding.SetBackgroundColour('#efebe9')
		tcRounding.SetForegroundColour('#3e2723')
		tcRefund = wx.TextCtrl(panel, size=(200,-1))
		tcRefund.SetBackgroundColour('#efebe9')
		tcRefund.SetForegroundColour('#3e2723')
		
		fgsfield.AddMany([(stSalePayment, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5),(tcSalePayment),(stCharge, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcCharge), (stTotalPayment, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcTotalPayment), (stToRefund, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcToRefund), (stRounding, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcRounding), (stRefund, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcRefund)])		
		
		gbsbottom.AddMany([(fgsfield,(0,8),wx.DefaultSpan, wx.BOTTOM,30)])

		vbox.AddMany([(bsgrid,1,wx.LEFT|wx.RIGHT,30), (gbsbottom)])
	  
		panel.SetSizerAndFit(vbox)
		

def main():

	app = wx.App()
	product(None, title='CRUD Product')
	app.MainLoop()
	
if __name__=='__main__':
	main()
