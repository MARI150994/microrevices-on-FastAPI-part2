from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .base import Base


class Provider(Base):
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    products = relationship('Product', back_populates='provider')
