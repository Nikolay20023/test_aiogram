from sqlalchemy import Column, Integer, String, DateTime, PrimaryKeyConstraint
from datetime import datetime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


from bd.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date = Column(DateTime(timezone=True), default=datetime.now())
