from sqlalchemy.orm import sessionmaker
from models import Sale, SaleLine, engine

class manageSales():

	def __init__(self):
		Session = sessionmaker(bind=engine)
		self.session = Session()
	
	def addSale(self, name, sale):
		productOnSale= []
		productOnSale.append(address)
		newProductOnSale = Sale(name,self.myAddress)
		self.session.add(newProductOnSale)
		self.session.commit()
