import wx
#import wx.lib.pubsub import pub
import sys



class paywith(wx.Dialog):
	
	def __init__(self, parent, title):
		
		super(paywith, self).__init__(parent, title = title, size=(470,450))
			
		self.InitUI()
		self.Centre()
		self.Show()
		self.Bind(wx.EVT_CLOSE, self.OnClose)
			
			
	def InitUI(self):
		
		panel = wx.Panel(self)
		panel.SetBackgroundColour('#607d8b')
		self.panel = panel
		vbox = wx.BoxSizer(wx.VERTICAL)
		fgsTop = wx.FlexGridSizer(2,2,5,60)
		gbsMid = wx.FlexGridSizer(15,2,5,50)
		panelMid = wx.Panel(panel)
		panelMid.SetBackgroundColour('#fff59d')
		gbs = wx.GridBagSizer(15,5)
		
		stPaywith = wx.StaticText(panel, label='paywith')
		stPaywith.SetForegroundColour('white')
		stPaywith.SetBackgroundColour('black')
		stBalance = wx.StaticText(panel, label='balance')
		stBalance.SetForegroundColour('white')
		stBalance.SetBackgroundColour('black')
		tcBalance = wx.TextCtrl(panel, size=(200,-1))
		tcBalance.SetEditable(False)
		tcBalance.SetBackgroundColour('#efebe9')
		tcBalance.SetForegroundColour('#5D4037')


		paymentMethod = ['Cash', 'EDC BCA', 'EDC BNI', 'EDC Mandiri', 'EDC CIMB Niaga','Voucher','POS Return','POS Debt Note'] 
		comboPaywith = wx.ComboBox(panel,value = 'Cash', choices = paymentMethod)
		comboPaywith.Bind(wx.EVT_COMBOBOX, self.OnComboPaywith)
		
		paymentCard = ['BCA Card', 'BNI Card', 'Mandiri Card', 'CIMB Niaga Card'] 
		
		fgsTop.AddMany([ (stPaywith), (stBalance), (comboPaywith), (tcBalance) ])
		
		
		bs = wx.BoxSizer( wx.HORIZONTAL)
		#cash
		self.stAmount= wx.StaticText(panelMid, label='Amount')
		self.tcAmount = wx.TextCtrl(panelMid, size=(200,-1))		
		
		#bank card
		
		self.stPaymentCard = wx.StaticText(panelMid, label='Payment Card')
		self.stPaymentCard.Hide()
		self.comboPaymentCard = wx.ComboBox(panelMid,choices = paymentCard)
		self.comboPaymentCard.Hide()
		self.stPayAmount = wx.StaticText(panelMid, label='Pay Amount')
		self.stPayAmount.Hide()
		self.stCharge = wx.StaticText(panelMid, label='Charge')
		self.stCharge.Hide()
		self.stTotalCard = wx.StaticText(panelMid, label='Total Card')
		self.stTotalCard.Hide()
		self.stCardNo = wx.StaticText(panelMid, label='Card No.')
		self.stCardNo.Hide()
		self.stApprCode = wx.StaticText(panelMid, label='Appr. Code')
		self.stApprCode.Hide()
		self.tcPayAmount = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcPayAmount.Hide()
		self.tcCharge = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcCharge.SetEditable(False)
		self.tcCharge.SetBackgroundColour('#efebe9')
		self.tcCharge.Hide()
		self.tcTotalCard = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcTotalCard.SetEditable(False)
		self.tcTotalCard.SetBackgroundColour('#efebe9')
		self.tcTotalCard.Hide()
		self.tcCardNo = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcCardNo.Hide()
		self.tcApprCode = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcApprCode.Hide()
		
		#voucher
		self.stVoucherNo = wx.StaticText(panelMid, label='Voucher No.')
		self.stVoucherNo.Hide()
		self.stVoucherCount = wx.StaticText(panelMid, label='Voucher Count')
		self.stVoucherCount.Hide()
		self.stNominal = wx.StaticText(panelMid, label='Nominal @')
		self.stNominal.Hide()
		self.stTotalAmount = wx.StaticText(panelMid, label='Total Amount')
		self.stTotalAmount.Hide()		
		self.tcVoucherNo = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcVoucherNo.Hide()
		self.tcVoucherCount = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcVoucherCount.Hide()
		self.tcNominal = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcNominal.SetEditable(False)
		self.tcNominal.SetBackgroundColour('#efebe9')
		self.tcNominal.Hide()
		self.tcTotalAmount = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcTotalAmount.SetEditable(False)
		self.tcTotalAmount.SetBackgroundColour('#efebe9')
		self.tcTotalAmount.Hide()
		
		
		#pos return
		
		self.stPosReturnNo = wx.StaticText(panelMid, label='Return No.')
		self.stPosReturnNo.Hide()
		self.stPosReturnAmount = wx.StaticText(panelMid, label='Return Amount')
		self.stPosReturnAmount.Hide()
		
		self.tcPosReturnNo = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcPosReturnNo.Hide()
		self.tcPosReturnAmount = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcPosReturnAmount.Hide()		
		
		#pos debt note
		
		self.stDebtNoteNo = wx.StaticText(panelMid, label='Debt Note No.')
		self.stDebtNoteNo.Hide()
		self.stDebtAmount = wx.StaticText(panelMid, label='Debt Amount')
		self.stDebtAmount.Hide()
		
		self.tcDebtNoteNo = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcDebtNoteNo.Hide()
		self.tcDebtAmount = wx.TextCtrl(panelMid, size=(200,-1))
		self.tcDebtAmount.Hide()
		
		
		
		gbsMid.AddMany([ (self.stAmount, 0, wx.LEFT|wx.TOP, 5),(self.tcAmount) ])
		
		gbsMid.AddMany([ (self.stPaymentCard,0,wx.LEFT|wx.TOP, 5), (self.comboPaymentCard), (self.stPayAmount,0,wx.LEFT| wx.TOP, 5), (self.tcPayAmount), (self.stCharge,0,wx.LEFT|wx.TOP, 5), (self.tcCharge), (self.stTotalCard,0,wx.LEFT|wx.TOP, 5), (self.tcTotalCard), (self.stCardNo,0, wx.LEFT|wx.TOP, 5), (self.tcCardNo), (self.stApprCode,0, wx.LEFT|wx.TOP, 5), (self.tcApprCode) ])
		
		gbsMid.AddMany([ (self.stVoucherNo,0,wx.LEFT|wx.TOP, 5), (self.tcVoucherNo), (self.stVoucherCount,0,wx.LEFT|wx.TOP, 5),(self.tcVoucherCount), (self.stNominal,0,wx.LEFT|wx.TOP, 5),(self.tcNominal), (self.stTotalAmount,0,wx.LEFT|wx.TOP, 5), (self.tcTotalAmount) ])
		
		gbsMid.AddMany([ (self.stDebtNoteNo, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5), (self.tcDebtNoteNo),	(self.stDebtAmount, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5), (self.tcDebtAmount) ])
		
		gbsMid.AddMany([ (self.stPosReturnNo, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5), (self.tcPosReturnNo),	(self.stPosReturnAmount, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5), (self.tcPosReturnAmount) ])
		
		bs.Add(gbsMid, 1, wx.ALL|wx.EXPAND, 20)
		panelMid.SetSizer(bs)
		cancelButton = wx.Button(panel, label='&Cancel')
		cancelButton.Bind( wx.EVT_BUTTON, self.OnClose)
		
		okButton = wx.Button(panel, label='&OK')
		okButton.SetForegroundColour('white')
		okButton.SetBackgroundColour('#1976D2')
#		okButton.Bind(wx.EVT_BUTTON, self.SendAndClose)
		gbs.AddMany([ (cancelButton,(0,15)),(okButton,(0,16)) ])
		vbox.AddMany([(fgsTop,1,wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND,30), (panelMid ,3, wx.LEFT|wx.RIGHT|wx.EXPAND, 30), (gbs,1, wx.ALL|wx.EXPAND,20) ])
		panel.SetSizerAndFit(vbox)
		
	def OnClose(self, event):
		self.Destroy()
		
	def SendAndClose(self, event):
	  inputText = self.tcCustomer.GetValue()
	  pub.sendMessage('tcCustListener', message=inputText)
	
	def OnComboPaywith(self, event):
		bankCard =['EDC BCA','EDC BNI','EDC Mandiri','EDC CIMB Niaga']
		if event.GetEventObject().GetValue() == 'Cash' :
			
			self.stVoucherNo.Hide()
			self.stVoucherCount.Hide()
			self.stNominal.Hide()
			self.stTotalAmount.Hide()
			self.tcVoucherNo.Hide()
			self.tcVoucherCount.Hide()
			self.tcNominal.Hide()
			self.tcTotalAmount.Hide()
	
			
			self.stPaymentCard.Hide()
			self.comboPaymentCard.Hide()
			self.stPayAmount.Hide()
			self.stCharge.Hide()
			self.stTotalCard.Hide()
			self.stCardNo.Hide()
			self.stApprCode.Hide()
			self.tcPayAmount.Hide()
			self.tcCharge.Hide()
			self.tcTotalCard.Hide()
			self.tcCardNo.Hide()
			self.tcApprCode.Hide()

			self.stPosReturnNo.Hide()
			self.stPosReturnAmount.Hide()
			self.tcPosReturnNo.Hide()
			self.tcPosReturnAmount.Hide()
			
			self.stDebtNoteNo.Hide()
			self.stDebtAmount.Hide()
			self.tcDebtNoteNo.Hide()
			self.tcDebtAmount.Hide()
			
			self.stAmount.Show()
			self.tcAmount.Show()
			self.panel.GetSizer().Layout()
		
		elif event.GetEventObject().GetValue() in bankCard :
			
			self.stAmount.Hide()
			self.tcAmount.Hide()			
			
			self.stVoucherNo.Hide()
			self.stVoucherCount.Hide()
			self.stNominal.Hide()
			self.stTotalAmount.Hide()
			self.tcVoucherNo.Hide()
			self.tcVoucherCount.Hide()
			self.tcNominal.Hide()
			self.tcTotalAmount.Hide()
			
			self.stDebtNoteNo.Hide()
			self.stDebtAmount.Hide()
			self.tcDebtNoteNo.Hide()
			self.tcDebtAmount.Hide()

			self.stPosReturnNo.Hide()
			self.stPosReturnAmount.Hide()
			self.tcPosReturnNo.Hide()
			self.tcPosReturnAmount.Hide()
			
			self.stPaymentCard.Show()
			self.comboPaymentCard.Show()
			self.stPayAmount.Show()
			self.stCharge.Show()
			self.stTotalCard.Show()
			self.stCardNo.Show()
			self.stApprCode.Show()
			self.tcPayAmount.Show()
			self.tcCharge.Show()
			self.tcTotalCard.Show()
			self.tcCardNo.Show()
			self.tcApprCode.Show()
			self.panel.GetSizer().Layout()
			
		elif event.GetEventObject().GetValue() == 'Voucher' :

			self.stAmount.Hide()
			self.tcAmount.Hide()

			self.stPaymentCard.Hide()
			self.comboPaymentCard.Hide()
			self.stPayAmount.Hide()
			self.stCharge.Hide()
			self.stTotalCard.Hide()
			self.stCardNo.Hide()
			self.stApprCode.Hide()
			self.tcPayAmount.Hide()
			self.tcCharge.Hide()
			self.tcTotalCard.Hide()
			self.tcCardNo.Hide()
			self.tcApprCode.Hide()
			
			self.stDebtNoteNo.Hide()
			self.stDebtAmount.Hide()
			self.tcDebtNoteNo.Hide()
			self.tcDebtAmount.Hide()			

			self.stPosReturnNo.Hide()
			self.stPosReturnAmount.Hide()
			self.tcPosReturnNo.Hide()
			self.tcPosReturnAmount.Hide()
			
			self.stVoucherNo.Show()
			self.stVoucherCount.Show()
			self.stNominal.Show()
			self.stTotalAmount.Show()
			self.tcVoucherNo.Show()
			self.tcVoucherCount.Show()
			self.tcNominal.Show()
			self.tcTotalAmount.Show()
			self.panel.GetSizer().Layout()	
			
		elif event.GetEventObject().GetValue() == 'POS Return' :
			
			self.stAmount.Hide()
			self.tcAmount.Hide()

			
			self.stVoucherNo.Hide()
			self.stVoucherCount.Hide()
			self.stNominal.Hide()
			self.stTotalAmount.Hide()
			self.tcVoucherNo.Hide()
			self.tcVoucherCount.Hide()
			self.tcNominal.Hide()
			self.tcTotalAmount.Hide()
	
			
			self.stPaymentCard.Hide()
			self.comboPaymentCard.Hide()
			self.stPayAmount.Hide()
			self.stCharge.Hide()
			self.stTotalCard.Hide()
			self.stCardNo.Hide()
			self.stApprCode.Hide()
			self.tcPayAmount.Hide()
			self.tcCharge.Hide()
			self.tcTotalCard.Hide()
			self.tcCardNo.Hide()
			self.tcApprCode.Hide()
			
			self.stDebtNoteNo.Hide()
			self.stDebtAmount.Hide()
			self.tcDebtNoteNo.Hide()
			self.tcDebtAmount.Hide()
			
			self.stPosReturnNo.Show()
			self.stPosReturnAmount.Show()
			self.tcPosReturnNo.Show()
			self.tcPosReturnAmount.Show()
			
			self.panel.GetSizer().Layout()
			
		elif event.GetEventObject().GetValue() ==		'POS Debt Note':

			self.stAmount.Hide()
			self.tcAmount.Hide()

			
			self.stVoucherNo.Hide()
			self.stVoucherCount.Hide()
			self.stNominal.Hide()
			self.stTotalAmount.Hide()
			self.tcVoucherNo.Hide()
			self.tcVoucherCount.Hide()
			self.tcNominal.Hide()
			self.tcTotalAmount.Hide()
	
			
			self.stPaymentCard.Hide()
			self.comboPaymentCard.Hide()
			self.stPayAmount.Hide()
			self.stCharge.Hide()
			self.stTotalCard.Hide()
			self.stCardNo.Hide()
			self.stApprCode.Hide()
			self.tcPayAmount.Hide()
			self.tcCharge.Hide()
			self.tcTotalCard.Hide()
			self.tcCardNo.Hide()
			self.tcApprCode.Hide()
			
			self.stPosReturnNo.Hide()
			self.stPosReturnAmount.Hide()
			self.tcPosReturnNo.Hide()
			self.tcPosReturnAmount.Hide()
			
			self.stDebtNoteNo.Show()
			self.stDebtAmount.Show()
			self.tcDebtNoteNo.Show()
			self.tcDebtAmount.Show()
			self.panel.GetSizer().Layout()	
		else:
			event.Skip()

def main():

	app = wx.App()
	paywith(None, title='Choose Payment Method')
	app.MainLoop()
		
	
if __name__=='__main__':
	main()		

