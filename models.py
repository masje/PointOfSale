from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  Table, VARCHAR, BOOLEAN, NUMERIC, Sequence, create_engine, ForeignKey, Date, TIMESTAMP
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
		__tablename__ = 'users'
		
		id = Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
		login = Column(VARCHAR(64), nullable=False, unique=True)
		name = Column(VARCHAR(64))
		pwd = Column(VARCHAR(64))
		is_admin = Column(BOOLEAN, default= False, nullable=False)
		is_cs = Column(BOOLEAN, default= False, nullable=False)
		is_cashier = Column(BOOLEAN, default= False, nullable=False)
		is_spv = Column(BOOLEAN, default= False, nullable=False)
		active = Column(BOOLEAN, default= False, nullable=False)
		def __repr__(self):
				return "<User(login='%s', fullname='%s', password='%s')>" % (self.login, self.name, self.pwd)

class Address(Base):
		__tablename__= 'addresses'
		id = Column(Integer, primary_key=True)
		email_address = Column(String, nullable=False)
		user_id = Column(VARCHAR(64), ForeignKey('users.login'), nullable=False)
		
		user = relationship("User", back_populates="addresses")
		def __repr__(self):
				return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

class Product(Base):
		__tablename__= 'product'
		id = Column(Integer, primary_key=True, nullable=False)
		barcode = Column(VARCHAR(64), nullable=False)
		code = Column(VARCHAR(64), nullable=False)
		name = Column(VARCHAR(128))
		ppn_rate = Column(NUMERIC(16,2), default = 0, nullable=False)
		price = Column(NUMERIC(16,2), default=0, nullable=False)
		sellable = Column(BOOLEAN, default = False, nullable=False)
		active = Column(BOOLEAN, default = False, nullable = False)
		def __repr__(self):
				return "<Product(code='%s',name='%s',price='%s')>" % (self.code, self.name, self.price)

class Customer(Base):
		__tablename__= 'customer'
		id = Column(Integer, primary_key=True, nullable=False)
		member_no = Column(VARCHAR(64), unique=True)
		name = Column(VARCHAR(64))
		disc_rate = Column(NUMERIC(16,2), nullable=False, default=0)
		active = Column(BOOLEAN, default=False, nullable=False)
		is_cust = Column(BOOLEAN, default=False, nullable=False)
		address = Column(VARCHAR(256))
		def __repr__(self):
				return "Customer(member_no='%s', name='%s', address='%s')>" % (self.member_no, self.name, self.address)
		
class PosSession(Base):
		__tablename__= 'pos_session'
		id = Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
		company_id = Column(Integer, primary_key=True, nullable=False, default=1)
		shop_id = Column(Integer, nullable=False)
		ses_date = Column(Date, nullable=False)
		state = Column(VARCHAR(16), nullable=False, default='Draft')
		name = Column(VARCHAR(64), nullable=False)
		ses_pwd = Column(VARCHAR(64))
		info = Column(VARCHAR(64))
		station_id = Column(Integer, nullable=False)
		cashier_id = Column(Integer, nullable=False)
		initial_cash = Column(NUMERIC(16,2), nullable=False, default=0)
		logged_in = Column(BOOLEAN, nullable=False, default=False)
		last_sale_no = Column(Integer, nullable=False, default=0)
		last_pending_no = Column(Integer, nullable=False, default=0)
		last_paid_id = Column(Integer, nullable=False, default=0)
		
class PosSale(Base):
		__tablename__= 'pos_sale'
		id = Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
		session_id = Column(Integer)
		customer_id = Column(Integer)
		state = Column(VARCHAR(32), nullable=False, default='Draft')
		info = Column(VARCHAR(256))
		cust_disc_rate = Column(NUMERIC(16,2), nullable=False, default=0)
		tstamp = Column(TIMESTAMP(0), nullable= False)
		

engine = create_engine('postgresql://siabang:siabang@localhost:5432/rainshop', client_encoding='utf8')

Base.metadata.create_all(engine)
