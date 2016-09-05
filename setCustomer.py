import wx
import sys
from wx.lib.pubsub import pub
sys.path.insert(0,"/home/je/Documents/PointOfSales/saPos")
from manageCustomer import manageCustomer
manage = manageCustomer()

class setCustomer(wx.Dialog):

	def __init__(self, parent, title):

		super(setCustomer, self).__init__(parent, title=title, size=(600,280))
		self.InitUI()
		self.Centre()
		self.Show()
		
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.noMember=False
		
	def InitUI(self):
	
		panel = wx.Panel(self)
		self.panel=panel
		panel.SetBackgroundColour('#607d8b')
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		fgs = wx.FlexGridSizer(3,2,5,15)
		gbs = wx.GridBagSizer(15,5)
		
		cbMember = wx.CheckBox(panel, label='Registered Member')
		cbMember.SetForegroundColour('white')
		cbMember.SetBackgroundColour('#546e7a')
		cbMember.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
		stNoMember = wx.StaticText(panel, label=('No Member'))
		stNoMember.SetForegroundColour('white')
		stNoMember.SetBackgroundColour('black')
		stNoMember.Hide()
		tcNoMember = wx.TextCtrl(panel,size=(500,-1))
		self.tcNoMember = tcNoMember
		self.tcNoMember.Bind(wx.EVT_KEY_DOWN, self.onEnterNoMember)
		tcNoMember.Hide()
		
		self.stNoMember=stNoMember
		self.tcNoMember=tcNoMember
				
		stCustomer = wx.StaticText(panel, label=('Customer'))
		stCustomer.SetForegroundColour('white')
		stCustomer.SetBackgroundColour('black')
		tcCustomer = wx.TextCtrl(panel,size=(500,-1))
		self.tcCustomer=tcCustomer
		
		stDAddress = wx.StaticText(panel, label='Delivery Address')
		stDAddress.SetForegroundColour('white')
		stDAddress.SetBackgroundColour('black')
		tcDAddress = wx.TextCtrl(panel,size=(500,70),style=wx.TE_MULTILINE)
		self.tcDAddress=tcDAddress
		
		fgs.AddMany([ (stNoMember), (tcNoMember, 1, wx.EXPAND),(stCustomer), (tcCustomer, 1, wx.EXPAND), (stDAddress), (tcDAddress, 1, wx.EXPAND) ])
		fgs.AddGrowableCol(1,1)
		
		
		cancelButton = wx.Button(panel, label='&Cancel')
		cancelButton.Bind( wx.EVT_BUTTON, self.OnClose)
		
		okButton = wx.Button(panel, label='&OK')
		okButton.SetForegroundColour('white')
		okButton.SetBackgroundColour('#1976D2')
		okButton.Bind(wx.EVT_BUTTON, self.actionCustomer)
		
		gbs.AddMany([ (cancelButton,(0,25)),(okButton,(0,26)) ])

		vbox.AddMany([ (cbMember,1, wx.TOP|wx.RIGHT|wx.LEFT, 20),(fgs,1, wx.TOP|wx.RIGHT|wx.LEFT, 20), (gbs, 1, wx.ALL, 20) ])

		panel.SetSizerAndFit(vbox)
		
	def actionCustomer(self):
		if self.noMember==True:
			self.onEnterNoMember()
		else:
			self.sendAndClose()
		
	def onEnterNoMember(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
			data = manage.SearchCustomer(str(self.tcNoMember.GetValue()))
			self.tcCustomer.SetValue(str(data[0]))
			self.tcDAddress.SetValue(str(data[1]))
			pub.sendMessage('mDiscount', data[2],arg2=True)		
		else : 
			event.Skip()
		
		
	def OnCheckBox(self, event):
		state = event.IsChecked()
		if state:
			self.tcCustomer.SetEditable(False)
			self.tcCustomer.SetBackgroundColour('#efebe9')
			self.tcCustomer.SetForegroundColour('#3e2723')
			self.tcDAddress.SetEditable(False)
			self.tcDAddress.SetBackgroundColour('#efebe9')
			self.tcDAddress.SetForegroundColour('#3e2723')
			
			self.stNoMember.Show()
			self.tcNoMember.Show()
			self.noMember = True
			self.panel.GetSizer().Layout()
			
		else:
			self.tcCustomer.SetEditable(True)
			self.tcCustomer.SetBackgroundColour('white')
			self.tcCustomer.SetForegroundColour('black')
			self.tcDAddress.SetEditable(True)
			self.tcDAddress.SetBackgroundColour('white')
			self.tcDAddress.SetForegroundColour('black')
			self.stNoMember.Hide()
			self.tcNoMember.Hide()
			self.tcNoMember.SetValue('')
			self.noMember = False
			self.panel.GetSizer().Layout()
		
	def OnClose(self, event):
		self.Destroy()
		
	def sendAndClose(self, event):
	  inputText = self.tcCustomer.GetValue()
	  pub.sendMessage('InputCustomer', message=inputText)

	  self.Destroy()

def main():

	app = wx.App()
	setCustomer(None, title='Set Customer')
	app.MainLoop()
	
if __name__=='__main__':
	main()
	

