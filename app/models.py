from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Time, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Сохраняем хэш пароля, а не сам пароль
    role = Column(String)  # Роль: admin, user, observer

class Equipment(Base):
    __tablename__ = "equipments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    availability_start = Column(Time)
    availability_end = Column(Time)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    equipment_id = Column(Integer, ForeignKey("equipments.id"))
    start_time = Column(DateTime, default=func.now())
    end_time = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    user = relationship("User", back_populates="bookings")
    equipment = relationship("Equipment", back_populates="bookings")

User.bookings = relationship("Booking", back_populates="user")
Equipment.bookings = relationship("Booking", back_populates="equipment")

class Checklist(Base):
    __tablename__ = "checklists"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    equipment_id = Column(Integer, ForeignKey("equipments.id"))
    steps = Column(String)  # Это будет строка, где описан весь процесс выполнения эксперимента

    user = relationship("User")
    equipment = relationship("Equipment")
