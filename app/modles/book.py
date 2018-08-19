from sqlalchemy import Column, String, Integer, Boolean

from app.modles.base import Base


class Like(Base):
	"""喜欢书籍模型"""

	id = Column(Integer, primary_key=True)
	openid = Column(String(64))
	isbn = Column(Integer)
	islike = Column(Boolean)
	