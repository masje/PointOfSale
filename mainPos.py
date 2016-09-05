import wx
import wx.grid
from wx.lib.pubsub import pub
from setCustomer import setCustomer
from payment import payment
from searchProduct import searchProduct
from login import LoginDialog

class mainPos(wx.Frame):

	def __init__(self, parent, title):
		pub.subscribe(self.loginListener, "0987")

		pub.subscribe(self.getMemberDiscount, "mDiscount")
		LoginDialog()
		
		super(mainPos, self).__init__(parent, title= title, size=(1280,800))
		
		self.InitUI()
		self.Centre()

		self.ListProduct=[]
		
		self.discountProduct=False
		
	def loginListener(self, message):
	  if str(message)=='show':
	  	self.Show()
	  else:
	  	self.Destroy()	
		
	def getProduct(self, message, arg2=None):
		
		self.tcBarcode.SetValue(message[0])
		self.tcDescription.SetValue(message[2])
		Price = message[3].split('.')
		Price =	self.formatingNumber(int(Price[0]))
		self.tcPrice.SetValue(Price)
		
	
	def formatingNumber(self, number):
		number = '{:,}'.format(number)
		strPrice = number.replace(',','.')
		return strPrice

	
	def formatingBack(self, number):
		strPrice = number.replace('.','')
		return strPrice

	def getListCurrentBarcode(self):
		ListBarcode=[]
		for i in range(len(self.ListProduct)):
			ListBarcode.append(str(self.posGrid.GetCellValue(i, 0)))
		return ListBarcode
	
		
	def getMemberDiscount(self, message, arg2):
		discount = 0	
		if arg2==True:
			memberDiscount = str(message.split('.'))
			memberDiscount = int(memberDiscount[0])
			discount = int(memberDiscount)
		else:
			discount = 0
		return discount
		self.tcDiscount.SetValue(self.formatingNumber(discount))
	
	def getAmountSubtotalMemberDiscount(self):
		amount=0
		discount=0
		subtotal=0
		memdiskon=0
		finalPrice=0
		for i in range(len(self.ListProduct)):
			amount=amount+int(self.formatingBack(self.posGrid.GetCellValue(i, 5)))
		subtotal=amount-discount	
		finalPrice=subtotal-memdiskon
		self.tcAmount.SetValue(self.formatingNumber(amount))
		self.tcDiscount.SetValue(self.formatingNumber(discount))
		self.tcSubtotal.SetValue(self.formatingNumber(subtotal))
		self.tcMemDiscount.SetValue(self.formatingNumber(memdiskon))
		self.bigtc.SetValue(self.formatingNumber(finalPrice))
		
		
	def calculatePriceQtyDeliver(self):
		Price = int(self.formatingBack(self.tcPrice.GetValue()))
		Qty = int(self.tcQty.GetValue())
		QtyCarried = int(self.tcQtyCarried.GetValue())
		self.totalPrice = Price * Qty
		QtyDeliver = Qty - QtyCarried
		self.tcQtyDeliver.SetValue(str(QtyDeliver)) 
		
	def setListProduct(self):
		#discount = self.getDiscount(None, False)
		self.ListProduct.append([str(self.tcBarcode.GetValue()),str(self.tcDescription.GetValue()),str(self.tcQty.GetValue()),self.formatingBack(self.tcPrice.GetValue()),0,str(self.totalPrice),str(self.tcQtyCarried.GetValue()),str(self.tcQtyDeliver.GetValue())])
		
		#print self.ListProduct
				
	def InitUI(self):
		
		panel = wx.Panel(self)
		panel.SetBackgroundColour('#8d6e63')
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		panelADSM = wx.Panel(panel)
		panelADSM.SetBackgroundColour('#607d8b')
		panelBDQP = wx.Panel(panel)
		#panelBDQP.SetBackgroundColour('#fff59d')
		panelGrid = wx.Panel(panel)
		panelBottom = wx.Panel(panel)
		panelBottom.SetBackgroundColour('#607d8b')
		panelLog = wx.Panel(panel)
		
		gbs = wx.GridBagSizer(10,10)
		fgsTop = wx.FlexGridSizer(1,2,5,5)
		fgsADSM = wx.FlexGridSizer(4,2,10,10)
		bsGrid = wx.BoxSizer(wx.VERTICAL)
		hboxBottom = wx.BoxSizer(wx.HORIZONTAL)
		fgsBottom1 = wx.FlexGridSizer(2,1,10,20)
		fgsBottom2 = wx.FlexGridSizer(4,6,10,10)

		fgsSCC = wx.FlexGridSizer(3,2,5,10)
		gbsLCIC = wx.GridBagSizer(10,10)
		
		gbsCL = wx.BoxSizer(wx.HORIZONTAL)
		
		
		textAmount = wx.StaticText(panelADSM, label='Amount')
		textAmount.SetForegroundColour('white')
		textAmount.SetBackgroundColour('black')
		textDiscount = wx.StaticText(panelADSM, label='Discount')
		textDiscount.SetForegroundColour('white')
		textDiscount.SetBackgroundColour('black')
		textSubtotal = wx.StaticText(panelADSM, label='Subtotal')
		textSubtotal.SetForegroundColour('white')
		textSubtotal.SetBackgroundColour('black')
		textMemDiscount = wx.StaticText(panelADSM, label='Member Discount')
		textMemDiscount.SetForegroundColour('white')
		textMemDiscount.SetBackgroundColour('black')
		tcAmount = wx.TextCtrl(panelADSM, -1,'0',size = (200, -1))
		tcAmount.SetWindowStyle(wx.TE_RIGHT)
		tcAmount.SetBackgroundColour('#efebe9')
		tcAmount.SetForegroundColour('#3e2723')
		tcAmount.SetEditable(False)
		self.tcAmount=tcAmount
		tcDiscount = wx.TextCtrl(panelADSM, -1,'0',size = (200, -1))
		tcDiscount.SetWindowStyle(wx.TE_RIGHT)
		tcDiscount.SetBackgroundColour('#efebe9')
		tcDiscount.SetForegroundColour('#3e2723')
		tcDiscount.SetEditable(False)
		self.tcDiscount=tcDiscount
		tcSubtotal = wx.TextCtrl(panelADSM, -1,'0',size = (200, -1))
		tcSubtotal.SetWindowStyle(wx.TE_RIGHT)
		tcSubtotal.SetBackgroundColour('#efebe9')
		tcSubtotal.SetForegroundColour('#3e2723')
		tcSubtotal.SetEditable(False)
		self.tcSubtotal=tcSubtotal
		tcMemDiscount = wx.TextCtrl(panelADSM, -1,'0',size = (200, -1))
		tcMemDiscount.SetWindowStyle(wx.TE_RIGHT)
		tcMemDiscount.SetBackgroundColour('#efebe9')
		tcMemDiscount.SetForegroundColour('#3e2723')
		tcMemDiscount.SetEditable(False)
		self.tcMemDiscount=tcMemDiscount
		fgsADSM.AddMany([ (textAmount, 0, wx.ALIGN_RIGHT|wx.TOP,5),(tcAmount, 1), (textDiscount, 0, wx.ALIGN_RIGHT|wx.TOP,5), (tcDiscount, 1), (textSubtotal, 0, wx.ALIGN_RIGHT|wx.TOP,5), (tcSubtotal, 1), (textMemDiscount,0 ,wx.ALIGN_RIGHT|wx.TOP,5), (tcMemDiscount, 1) ])
		
		
		
		bigtc = wx.TextCtrl(panelADSM,-1,'0',size=(1200, -1))
		bigtc.SetEditable(False)
		bigtc.SetForegroundColour('#3e2723')
		font = wx.Font(60, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
		bigtc.SetFont(font)
		bigtc.SetWindowStyle(wx.TE_RIGHT)
		self.bigtc=bigtc
		fgsTop.AddMany([ (fgsADSM, 1, wx.ALL, 10), (bigtc, 1, wx.EXPAND|wx.ALL, 10) ])
		
		panelADSM.SetSizer(fgsTop)
		
		textBarcode = wx.StaticText(panelBDQP, label='BARCODE')
		textBarcode.SetForegroundColour('#607d8b')
		textBarcode.SetBackgroundColour('black')
		textDescription = wx.StaticText(panelBDQP, label='DESCRIPTION')
		textDescription.SetForegroundColour('#607d8b')
		textDescription.SetBackgroundColour('black')
		textQty = wx.StaticText(panelBDQP, label='Qty')
		textQty.SetForegroundColour('#607d8b')
		textQty.SetBackgroundColour('black')
		textPrice = wx.StaticText(panelBDQP, label='Price')
		textPrice.SetForegroundColour('#607d8b')
		textPrice.SetBackgroundColour('black')
		textQtyCarried = wx.StaticText(panelBDQP, label='Carried')
		textQtyCarried.SetForegroundColour('#607d8b')
		textQtyCarried.SetBackgroundColour('black')
		textQtyDeliver = wx.StaticText(panelBDQP, label='Deliver')
		textQtyDeliver.SetForegroundColour('#607d8b')
		textQtyDeliver.SetBackgroundColour('black')
		
		tcBarcode = wx.TextCtrl(panelBDQP,-1,'', size=(120,-1))
		tcBarcode.SetEditable(False)
		tcBarcode.SetBackgroundColour('#efebe9')
		self.tcBarcode = tcBarcode
		tcDescription = wx.TextCtrl(panelBDQP,-1,'', size = (300, -1))
		tcDescription.SetEditable(False)
		tcDescription.SetBackgroundColour('#efebe9')
		self.tcDescription = tcDescription
		tcPrice = wx.TextCtrl(panelBDQP,-1,'0', size=(150,-1))
		tcPrice.SetEditable(False)
		tcPrice.SetBackgroundColour('#efebe9')
		self.tcPrice = tcPrice
		tcQty = wx.TextCtrl(panelBDQP, -1,'0',size=(80,-1))
		tcQty.SetFocus()
		tcQty.Bind(wx.EVT_KEY_DOWN, self.onEnterQty)
		self.tcQty = tcQty
		tcQtyCarried = wx.TextCtrl(panelBDQP, -1,'0',size=(80,-1))
		tcQtyCarried.Bind(wx.EVT_KEY_DOWN, self.onEnterQtyCarried)
		self.tcQtyCarried = tcQtyCarried
		tcQtyDeliver = wx.TextCtrl(panelBDQP, -1, '0',size=(80,-1))
		tcQtyDeliver.SetBackgroundColour('#efebe9')
		tcQtyDeliver.SetEditable(False)
		self.tcQtyDeliver = tcQtyDeliver
		
		
		
		gbs.Add(textBarcode, pos= (0,0), flag= wx.TOP|wx.LEFT, border=10)
		gbs.Add(textDescription, pos= (0,1), flag= wx.TOP, border=10)
		gbs.Add(textPrice, pos=(0,2), flag= wx.TOP, border=10)
		gbs.Add(textQty, pos=(0,3), flag= wx.TOP, border=10)
		gbs.Add(textQtyCarried, pos=(0,4), flag=wx.TOP, border=10)
		gbs.Add(textQtyDeliver, pos=(0,5), flag=wx.TOP, border=10)
		
		gbs.Add(tcBarcode, pos=(1,0), flag=wx.LEFT|wx.BOTTOM, border=10)
		gbs.Add(tcDescription,pos=(1,1), flag=wx.EXPAND|wx.BOTTOM, border=10)
		gbs.Add(tcPrice, pos=(1,2), flag=wx.EXPAND|wx.BOTTOM, border=10)
		gbs.Add(tcQty, pos=(1,3))
		gbs.Add(tcQtyCarried, pos=(1,4), flag=wx.EXPAND|wx.BOTTOM, border=10)
		gbs.Add(tcQtyDeliver, pos=(1,5), flag=wx.EXPAND|wx.BOTTOM|wx.RIGHT, border=10)
		gbs.AddGrowableCol(1,1)
		
		panelBDQP.SetSizerAndFit(gbs)
		attr = wx.grid.GridCellAttr()
		attr.SetReadOnly(True)
		posGrid = wx.grid.Grid(panelGrid,size=(600,350))
		posGrid.CreateGrid(100,9)
		posGrid.EnableDragColSize(False)
		posGrid.EnableDragRowSize(False)
		
		for i in range (0, posGrid.GetNumberCols()):
			posGrid.SetColAttr(i, attr)
		
		
		posGrid.SetLabelBackgroundColour('#CFD8DC')
		posGrid.SetColLabelValue(0,'Barcode')
		posGrid.SetColLabelValue(1,'Description')
		posGrid.SetColLabelValue(2,'Qty')
		posGrid.SetColLabelValue(3,'Price')	
		posGrid.SetColLabelValue(4,'Discount')
		posGrid.SetColLabelValue(5,'Amount')
		posGrid.SetColLabelValue(6,'Qty Carried')
		posGrid.SetColLabelValue(7,'Qty Deliver')
		posGrid.SetColLabelValue(8,'')
		posGrid.SetRowLabelSize(0)
		posGrid.SetColSize(0,120)
		posGrid.SetColSize(1,380)
		posGrid.SetColSize(3,140)
		posGrid.SetColSize(4,120)
		posGrid.SetColSize(5,140)
		posGrid.SetColSize(6,90)
		posGrid.SetColSize(7,90)
		posGrid.SetColSize(8,100)
		posGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.onSingleSelect)
		posGrid.Bind(wx.EVT_KEY_DOWN, self.GridOnEnter)
		self.posGrid=posGrid
		self.pastRowExist= False
		self.pastRow=0
		self.currentRow=0
		
		bsGrid.Add(posGrid, 1, wx.EXPAND)
		#bsGrid.AddGrowableRow(0,1)
		panelGrid.SetSizer(bsGrid)
		
		textSession = wx.StaticText(panelBottom, label='Session')
		textSession.SetForegroundColour('white')
		textSession.SetBackgroundColour('black')
		textCashier = wx.StaticText(panelBottom, label='Cashier')
		textCashier.SetForegroundColour('white')
		textCashier.SetBackgroundColour('black')
		textCustomer = wx.StaticText(panelBottom, label='Customer')
		textCustomer.SetForegroundColour('white')
		textCustomer.SetBackgroundColour('black')

		
		tcSession = wx.TextCtrl(panelBottom, size = (300, -1))
		tcSession.SetBackgroundColour('#efebe9')
		tcSession.SetForegroundColour('#5D4037')
		tcSession.SetEditable(False)
		tcCashier = wx.TextCtrl(panelBottom, size = (300, -1))
		tcCashier.SetBackgroundColour('#efebe9')
		tcCashier.SetForegroundColour('#5D4037')
		tcCashier.SetEditable(False)
		tcCustomer = wx.TextCtrl(panelBottom, size = (300, -1))
		tcCustomer.SetBackgroundColour('#efebe9')
		tcCustomer.SetForegroundColour('#5D4037')
		tcCustomer.SetEditable(False)
		self.tcCustomer=tcCustomer
		pub.subscribe(self.OnSetCustomer, 'tcCustListener')
		
		fgsSCC.AddMany([ (textSession, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,10),(tcSession, 1, wx.EXPAND|wx.TOP, 5), (textCashier, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcCashier, 1, wx.EXPAND, 5), (textCustomer, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP,5), (tcCustomer, 1, wx.EXPAND,5) ])
		
		
		textLC = wx.StaticText(panelBottom, label='Line Count')
		textLC.SetForegroundColour('white')
		textLC.SetBackgroundColour('black')
		textIC = wx.StaticText(panelBottom, label='Item Count')
		textIC.SetForegroundColour('white')
		textIC.SetBackgroundColour('black')
		
		
		tcLC = wx.TextCtrl(panelBottom, size=(100,-1))
		tcLC.SetBackgroundColour('#efebe9')
		tcLC.SetForegroundColour('#5D4037')
		tcLC.SetEditable(False)
		tcIC = wx.TextCtrl(panelBottom, size=(80,-1))
		tcIC.SetBackgroundColour('#efebe9')
		tcIC.SetForegroundColour('#5D4037')		
		tcIC.SetEditable(False)
		
		gbsLCIC.Add(textLC, pos=(0,0),flag= wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT|wx.TOP,border=5)
		gbsLCIC.Add(tcLC, pos=(0,1),span=(2,1),flag=wx.EXPAND|wx.RIGHT,border=5)
		gbsLCIC.Add(textIC,pos=(0,2), flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP|wx.RIGHT,border=5)
		gbsLCIC.Add(tcIC,pos=(0,3),span=(2,1),flag=wx.EXPAND|wx.RIGHT, border=5)
		
		fgsBottom1.AddMany([ (fgsSCC, 0, wx.TOP, 10 ),(gbsLCIC, 0, wx.EXPAND) ])
		
		buttonF1 = wx.Button(panelBottom, size=(36,-1), label='F1')
		buttonF1.SetBackgroundColour('#1976D2')
		buttonF1.SetForegroundColour('#FFFFFF')
		
		buttonF2 = wx.Button(panelBottom, size=(36,-1), label='F2')
		buttonF2.SetBackgroundColour('#1976D2')
		buttonF2.SetForegroundColour('#FFFFFF')
		buttonF3 = wx.Button(panelBottom, size=(36,-1), label='F3')
		buttonF3.SetBackgroundColour('#1976D2')
		buttonF3.SetForegroundColour('#FFFFFF')
		buttonF4 = wx.Button(panelBottom, size=(36,-1), label='F4')
		buttonF4.SetBackgroundColour('#1976D2')
		buttonF4.SetForegroundColour('#FFFFFF')
		buttonF5 = wx.Button(panelBottom, size=(36,-1), label='F5')
		buttonF5.SetBackgroundColour('#1976D2')
		buttonF5.SetForegroundColour('#FFFFFF')
		buttonF6 = wx.Button(panelBottom, size=(36,-1), label='F6')
		buttonF6.SetBackgroundColour('#1976D2')
		buttonF6.SetForegroundColour('#FFFFFF')
		buttonF7 = wx.Button(panelBottom, size=(36,-1), label='F7')
		buttonF7.SetBackgroundColour('#1976D2')
		buttonF7.SetForegroundColour('#FFFFFF')
		buttonF8 = wx.Button(panelBottom, size=(36,-1), label='F8')
		buttonF8.SetBackgroundColour('#1976D2')
		buttonF8.SetForegroundColour('#FFFFFF')
		buttonF9 = wx.Button(panelBottom, size=(36,-1), label='F9')
		buttonF9.SetBackgroundColour('#1976D2')
		buttonF9.SetForegroundColour('#FFFFFF')
		buttonF10 = wx.Button(panelBottom, size=(36,-1), label='F10')
		buttonF10.SetBackgroundColour('#1976D2')
		buttonF10.SetForegroundColour('#FFFFFF')
		buttonF11 = wx.Button(panelBottom, size=(36,-1), label='F11')
		buttonF11.SetBackgroundColour('#1976D2')
		buttonF11.SetForegroundColour('#FFFFFF')
		buttonF12 = wx.Button(panelBottom, size=(36,-1), label='F12')
		buttonF12.SetBackgroundColour('#1976D2')
		buttonF12.SetForegroundColour('#FFFFFF')
		
		textF1 = wx.StaticText(panelBottom, label='Set Customer', size=(150,-1))
		textF1.SetForegroundColour('white')
		textF1.SetBackgroundColour('black')
		
		textF2 = wx.StaticText(panelBottom, label='Payment', size=(150,-1))
		textF2.SetForegroundColour('white')
		textF2.SetBackgroundColour('black')
		textF3 = wx.StaticText(panelBottom, label='Select Item', size=(150,-1))
		textF3.SetForegroundColour('white')
		textF3.SetBackgroundColour('black')
		textF4 = wx.StaticText(panelBottom, label='Edit Qty', size=(150,-1))
		textF4.SetForegroundColour('white')
		textF4.SetBackgroundColour('black')
		textF5 = wx.StaticText(panelBottom, label='Delete Item', size=(150,-1))
		textF5.SetForegroundColour('white')
		textF5.SetBackgroundColour('black')
		textF6 = wx.StaticText(panelBottom, label='Search Product', size=(150,-1))
		textF6.SetForegroundColour('white')
		textF6.SetBackgroundColour('black')
		textF7 = wx.StaticText(panelBottom, label='Pending Sale', size=(150,-1))
		textF7.SetForegroundColour('white')
		textF7.SetBackgroundColour('black')
		textF8 = wx.StaticText(panelBottom, label='Select Pending', size=(150,-1))
		textF8.SetForegroundColour('white')
		textF8.SetBackgroundColour('black')
		textF9 = wx.StaticText(panelBottom, label='Delete Pendings', size=(150,-1))
		textF9.SetForegroundColour('white')
		textF9.SetBackgroundColour('black')
		textF10 = wx.StaticText(panelBottom, label='Print Last Receipt', size=(150,-1))
		textF10.SetForegroundColour('white')
		textF10.SetBackgroundColour('black')
		textF11 = wx.StaticText(panelBottom, label='Select Bonus')
		textF11.SetForegroundColour('white')
		textF11.SetBackgroundColour('black')
		textF12 = wx.StaticText(panelBottom, label='Logout', size=(150,-1))
		textF12.SetForegroundColour('white')
		textF12.SetBackgroundColour('black')
		
		fgsBottom2.AddMany([ (buttonF1,1,wx.TOP,10), (textF1,0,wx.TOP,15),
												(buttonF5,1,wx.TOP,10), (textF5,0,wx.TOP,15),
												(buttonF9,1,wx.TOP,10), (textF9,0,wx.TOP,15),
												(buttonF2,1), (textF2,0,wx.TOP,5),
												(buttonF6,1), (textF6,0,wx.TOP,5),
												(buttonF10,1), (textF10,0,wx.TOP,5),
												(buttonF3,1), (textF3,0,wx.TOP,5),
												(buttonF7,1), (textF7,0,wx.TOP,5),
												(buttonF11,1), (textF11,0,wx.TOP,5),
												(buttonF4,1,wx.BOTTOM,10), (textF4,0,wx.TOP,5) ,
												(buttonF8,1,wx.BOTTOM,10), (textF8,0,wx.TOP,5),
												(buttonF12,1,wx.BOTTOM,10), (textF12,0,wx.TOP,5) ])
		
		
		
		hboxBottom.AddMany([ (fgsBottom1, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, 10), (fgsBottom2, 1, wx.RIGHT|wx.ALIGN_RIGHT,5) ])
		
		panelBottom.SetSizer(hboxBottom)
		
		textCL = wx.TextCtrl(panelLog)
		textCL.SetForegroundColour('white')
		textCL.SetBackgroundColour('black')
		textCL.SetEditable(False)
		gbsCL.Add(textCL, 1)
		panelLog.SetSizer(gbsCL)
		vbox.Add(panelADSM, 0, wx.EXPAND |wx.RIGHT|wx.LEFT, 10)
		vbox.Add(panelBDQP, 0, wx.EXPAND |wx.RIGHT|wx.LEFT, 10)
		vbox.Add(panelGrid, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10)
		vbox.Add(panelBottom, 1, wx.EXPAND|wx.RIGHT|wx.LEFT,10)
		vbox.Add(panelLog, 1, wx.EXPAND|wx.RIGHT|wx.LEFT,10)
		panel.SetSizerAndFit(vbox)
		
		id_F1 = wx.NewId()
		id_F2 = wx.NewId()
		id_F3 = wx.NewId()
		id_F4 = wx.NewId()
		id_F5 = wx.NewId()
		id_F6 = wx.NewId()
		id_F7 = wx.NewId()
		id_F8 = wx.NewId()
		id_F9 = wx.NewId()
		id_F10 = wx.NewId()
		id_F11 = wx.NewId()
		id_F12 = wx.NewId()
		
		self.Bind(wx.EVT_MENU, self.presed_F1, id=id_F1)
		self.Bind(wx.EVT_MENU, self.presed_F2, id=id_F2)
		self.Bind(wx.EVT_MENU, self.presed_F3, id=id_F3)
		self.Bind(wx.EVT_MENU, self.presed_F4, id=id_F4)
		self.Bind(wx.EVT_MENU, self.presed_F5, id=id_F5)
		self.Bind(wx.EVT_MENU, self.presed_F6, id=id_F6)
		self.Bind(wx.EVT_MENU, self.presed_F12, id=id_F12)
		
		accel_tbl = wx.AcceleratorTable([	(wx.ACCEL_NORMAL, wx.WXK_F1, id_F1 ), (wx.ACCEL_NORMAL, wx.WXK_F2, id_F2 ), (wx.ACCEL_NORMAL, wx.WXK_F3, id_F3 ), (wx.ACCEL_NORMAL, wx.WXK_F4, id_F4 ), (wx.ACCEL_NORMAL, wx.WXK_F5, id_F5 ), (wx.ACCEL_NORMAL, wx.WXK_F6, id_F6 ), (wx.ACCEL_NORMAL, wx.WXK_F7, id_F7 ), (wx.ACCEL_NORMAL, wx.WXK_F8, id_F8 ), (wx.ACCEL_NORMAL, wx.WXK_F9, id_F9 ), (wx.ACCEL_NORMAL, wx.WXK_F10, id_F10 ), (wx.ACCEL_NORMAL, wx.WXK_F11, id_F11 ), (wx.ACCEL_NORMAL, wx.WXK_F12, id_F12 ) 	])
		self.SetAcceleratorTable(accel_tbl)
		
	def presed_F1(self, event):
		setCustomer(None, title='Set Customer')
		
	def presed_F2(self, event):
		payment(None, title='Payment')

	def presed_F3(self, event):
		self.posGrid.SetFocus()

	def presed_F4(self, event):
		self.tcQty.SetFocus()
		
	def presed_F5(self, event):
		dlg = wx.MessageDialog(None, 'Are you sure to delete this?', 'Warning',wx.YES_NO | wx.ICON_QUESTION)
		result = dlg.ShowModal()
		
		if result==wx.ID_YES:
			if len(self.ListProduct)==0:
				wx.MessageBox('Nothing to be delete !', 'Warning', wx.OK | wx.ICON_WARNING)
			else:
				print self.currentRow
				del self.ListProduct[self.currentRow]				
#				self.posGrid.SelectRow(self.currentRow,False)
				self.defaultGrid(self.pastRow)
			#	print "current list product  "+ str(self.ListProduct)
				if len(self.ListProduct)==0:
			#		print 'len data 1'+ str(len(self.ListProduct))
					self.getAmountSubtotalMemberDiscount()
					self.clearGrid(len(self.ListProduct)+1)
				else:
			#		print 'len data2 '+ str(len(self.ListProduct))
			#		print 'data manipulation' +str(self.ListProduct)
					self.getAmountSubtotalMemberDiscount()
					self.clearGrid(len(self.ListProduct)+1)
					self.setGrid()
		else :
			pass
		self.tcQty.SetFocus()
		self.clearPanelBDQP()
	
	def presed_F6(self, event):
		self.clearPanelBDQP()
		self.defaultGrid(self.pastRow)
		searchProduct(None, title='searchProduct')
		pub.sendMessage("currentProductList", message=self.getListCurrentBarcode())
		self.tcQty.SetFocus()
		pub.subscribe(self.getProduct, "sendingGoodsData")
				
	def presed_F12(self, event):
		self.Destroy()
	
	
	def OnSetCustomer(self, message):
		self.tcCustomer.SetValue(message)		

	def onEnterQty(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
			if self.tcQty.IsEmpty():
				wx.MessageBox('Please Enter Quantity !', 'Warning', wx.OK | wx.ICON_WARNING)
			elif str(self.tcQty.GetValue())=='0':
				wx.MessageBox('Quantity Value must be < 0 !', 'Warning', wx.OK | wx.ICON_WARNING)
			elif str(self.tcQty.GetValue()).isalpha():
				wx.MessageBox('Number Only !',  'Warning', wx.OK | wx.ICON_WARNING)
			else:
				event.EventObject.Navigate()
		else:
			event.Skip()


	def onEnterQtyCarried(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
			
			if self.tcBarcode.IsEmpty() or self.tcDescription.IsEmpty():
				wx.MessageBox('Please Search Product !', 'Warning', wx.OK | wx.ICON_WARNING)
			
			elif str(self.tcQtyCarried.GetValue()).isalpha():
				wx.MessageBox('Number Only !',  'Warning', wx.OK | wx.ICON_WARNING)
			
			elif int(self.tcQty.GetValue())<int(self.tcQtyCarried.GetValue()):
				wx.MessageBox('Quantity must be  >  or  =  with QtyCarried !', 'Warning', wx.OK | wx.ICON_WARNING)
				self.tcQty.SetFocus()
			
			elif len(self.ListProduct)==0 :	
				self.calculatePriceQtyDeliver()
				self.setListProduct()
				self.setGrid()

			elif str(self.posGrid.GetCellValue(self.currentRow,0))==str(self.tcBarcode.GetValue()):
				self.calculatePriceQtyDeliver()
				self.ListProduct[self.currentRow][2]=self.tcQty.GetValue()
				self.ListProduct[self.currentRow][5]=self.totalPrice
				self.ListProduct[self.currentRow][6]=self.tcQtyCarried.GetValue()
				self.ListProduct[self.currentRow][7]=self.tcQtyDeliver.GetValue()
				self.setGrid()
			
			else:	
				self.calculatePriceQtyDeliver()
				self.setListProduct()
				self.setGrid()
			
			self.clearPanelBDQP()
			self.tcQty.SetFocus()
		
		else:
			event.Skip()
	#	print "current list product"+ str(self.ListProduct)

	def clearPanelBDQP(self):
		
		self.tcBarcode.SetValue('')
		self.tcDescription.SetValue('')
		self.tcPrice.SetValue('0')
		self.tcQty.SetValue('0')
		self.tcQtyCarried.SetValue('0')
		self.tcQtyDeliver.SetValue('0')		
	
	def clearGrid(self, row):
		for ii in xrange(row):
			for i in range(8):
				self.posGrid.SetCellValue(ii,i,str(''))		
				
	def setGrid(self):
		
		data = self.ListProduct
		for ii in xrange(len(data)):
			for i in range(8):
				self.posGrid.SetCellValue(ii,i,str(data[ii][i]))
		self.getAmountSubtotalMemberDiscount()

	def onSingleSelect(self, event):
		selectedData = []
		self.currentRow = event.GetRow()
	#	print 'select row '+ str(self.currentRow)
		for col in range(9):
			selectedData.append(str(self.posGrid.GetCellValue(self.currentRow,col)))
			self.posGrid.SetCellBackgroundColour(self.currentRow,col,'#fff59d')
		self.posGrid.ForceRefresh()
		if self.pastRowExist==True:
			self.defaultGrid(self.pastRow)
		self.pastRowExist= True
		self.pastRow = self.currentRow	
		self.tcBarcode.SetValue(str(selectedData[0]))
		self.tcDescription.SetValue(str(selectedData[1]))
		self.tcPrice.SetValue(str(selectedData[3]))
		self.tcQty.SetValue(str(selectedData[2]))
		self.tcQtyCarried.SetValue(str(selectedData[6]))
		self.tcQtyDeliver.SetValue(str(selectedData[7]))
		
	
	def defaultGrid(self, pastRow):
		if self.pastRowExist==True:
			for col in range(9):
				self.posGrid.SetCellBackgroundColour(pastRow,col,'white')
			self.posGrid.ForceRefresh()
	
	def GridOnEnter(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
			self.tcQty.SetFocus()
		else:
			event.Skip()

if __name__=='__main__':
	app = wx.App()
	mainPos(None, title='Point of Sales')
	app.MainLoop()
