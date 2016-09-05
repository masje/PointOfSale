from sqlalchemy.orm import sessionmaker
from models import User, engine


Session = sessionmaker(bind=engine)

session = Session()

new_user = User(id='4',login='ger',name= 'gery',pwd='123')
session.add(new_user)

session.commit()

