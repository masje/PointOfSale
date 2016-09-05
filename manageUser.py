from sqlalchemy.orm import sessionmaker
from models import User, engine

class manageUser():
	
	def __init__(self):
		Session = sessionmaker(bind=engine)
		self.session = Session()
		self.myUser = []
	
	def createUser(self, id, login, name, pwd):
		new_user = User(id,login,name,pwd)
		session.add(new_user)
		session.commit()
	
	def readUser(self):
		for i in self.session.query(User).order_by(User.id):
			for x in range(1):
				self.myUser.append(str(i.login))
		

			
	def updateUser(self, userlog,pass_new):
		our_user = self.session.query(User).filter_by(name=userlog).first()
		our_user.password = pass_new
		self.session.commit()
	
	def deleteUser(self, delUser):
		self.session.query(User).filter(User.login==delUser).delete()

	def checkUser(self, user):
		check = False
		for i in range(self.session.query(User).count()):
			if self.myUser[i]==user:
				check=True
		return check		
	
	def checkPassword(self, user ):
		password=''
		for i in self.session.query(User.pwd).filter(User.login==user):
			password = i.pwd
		
		return password
		

