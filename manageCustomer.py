from sqlalchemy.orm import sessionmaker
from models import Customer, engine

class manageCustomer():

	def __init__(self):
		Session = sessionmaker(bind=engine)
		self.session = Session()
		self.myCust= []
		
		
	def searchCustomer(self, memberNumber):
		for i in self.session.query(Customer).filter(Customer.member_no==memberNumber):
			self.myCust.append([ str(i.name), str(i.address), str(i.disc_rate)])
		return self.myCust
		
	def addCustomer(self, name, address):
		myAddress= []
		myAddress.append(address)
		newCustomer = Customer(name,self.myAddress)
		self.session.add(newCustomer)
		self.session.commit()
