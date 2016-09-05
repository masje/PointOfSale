from sqlalchemy.orm import sessionmaker
from models import Product, engine

class manageProduct():
	
	def __init__(self):
		Session = sessionmaker(bind=engine)
		self.session = Session()
		myProduct=[]
		self.myProduct = myProduct

		
	def readAllProduct(self):
		for i in self.session.query(Product):
			for x in range(1):
				self.myProduct.append([str(i.barcode),str(i.code),str(i.name),str(i.price)])

	def searchProductWithBarcode(self, barcode):
		for i in self.session.query(Product).filter(Product.barcode==barcode):
			self.myProduct.append([str(i.barcode),str(i.code),str(i.name),str(i.price)])
	
	
	def searchProductCodeLike(self, codeLike):
		for i in self.session.query(Product).filter(Product.code.like('%'+codeLike+'%')):
			self.myProduct.append([str(i.barcode),str(i.code),str(i.name),str(i.price)])


	def searchProductNameLike(self, nameLike):
		for i in self.session.query(Product).filter(Product.name.like('%'+nameLike+'%')):
			self.myProduct.append([str(i.barcode),str(i.code),str(i.name),str(i.price)])
	
	
	def setMyProductEmpty(self):
		self.myProduct = []
		
		
	def getProduct(self):
		return self.myProduct
		print self.myProduct
		
