from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        Boolean,
                        DECIMAL)
from sqlalchemy.orm import relationship

from .base import Base


class Product(Base):
    name = Column(String, unique=True, index=True, nullable=False)
    article = Column(String, nullable=False)
    price = Column(DECIMAL(5, 2), default=False)
    available = Column(Integer, nullable=False, default=0)  # available_quantity
    provider_id = Column(Integer, ForeignKey('provider.id'))
    provider = relationship('Provider', back_populates='products')

    # ordered = Column(Integer, nullable=False, default=0)
    # orderes = relationship()

