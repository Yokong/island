from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app.modles.base import Base


class User(Base):
	id = Column(Integer, primary_key=True)
	nickname = Column(String(24))
	phone_number = Column(String(18), unique=True)
	email = Column(String(50), unique=True, nullable=False)
	confirmed = Column(Boolean, default=False)
	beans = Column(Integer, default=0)
	_password = Column('password', String(128), nullable=False)
	
	@property
	def password(self):
		return self._password
		
	@password.setter
	def password(self, raw):
		self._password = generate_password_hash(raw)
		
	def check_password(self, raw):
		return check_password_hash(self._password, raw)
