import wx
import sys
from wx.lib.pubsub import pub
from sqlalchemy.orm import sessionmaker
sys.path.insert(0,"/home/je/Documents/PointOfSales/saPos")
from manageUser import manageUser


class LoginDialog(wx.Dialog):
       
		def __init__(self):
			wx.Dialog.__init__(self, None, title="Login",size=(270,190))

			userSizer = wx.BoxSizer(wx.HORIZONTAL)

			userLabel = wx.StaticText(self, label="Username :")
			userSizer.Add(userLabel, 0, wx.ALL|wx.CENTER, 10)
			self.user = wx.TextCtrl(self)
			userSizer.Add(self.user, 0, wx.ALL, 10)

			passwordSizer = wx.BoxSizer(wx.HORIZONTAL)

			passwordLabel = wx.StaticText(self, label="Password  :")
			passwordSizer.Add(passwordLabel, 0, wx.ALL|wx.CENTER, 10)
			
			self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
			passwordSizer.Add(self.password, 0, wx.ALL, 10)

			mainSizer = wx.BoxSizer(wx.VERTICAL)
			mainSizer.Add(userSizer, 0, wx.ALL, 5)
			mainSizer.Add(passwordSizer, 0, wx.ALL, 5)

			okButton = wx.Button(self, label="Login")
			okButton.Bind(wx.EVT_BUTTON, self.onLogin)
			mainSizer.Add(okButton, 0, wx.ALL|wx.CENTER, 10)
			self.SetSizer(mainSizer)
			self.Show()
			self.Bind(wx.EVT_CLOSE, self.onClose)

		def onLogin(self, event):
			
			manager = manageUser()
			manager.readUser()
			userName = self.user.GetValue() 
			userPassword = self.password.GetValue()
			
			if manager.checkUser(userName):
				print 'user correct!!!'
				
				if manager.checkPassword(userName)==userPassword:
					wx.MessageBox('You are now logged in!', 'Welcome', wx.OK | wx.ICON_INFORMATION)
					print "You are now logged in!"
					pub.sendMessage("0987", message='show')
					self.Destroy()
				else:
					wx.MessageBox('password is incorrect!!!', 'Welcome', wx.OK | wx.ICON_INFORMATION)
			
			else: 
				wx.MessageBox('username is incorrect!!!', 'Welcome', wx.OK | wx.ICON_INFORMATION)
		
		def onClose(self, event):
			pub.sendMessage("0987", message='destroy')
			self.Destroy()
				
				


