from sqlalchemy import Column, Integer, String

from app.modles.base import Base


class User(Base):
	id = Column(Integer, primary_key=True)
	openid = Column(String(64), unique=True)
	nickname = Column(String(24))
