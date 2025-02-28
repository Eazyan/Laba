from pydantic import BaseModel
from datetime import time, datetime
from typing import List, Optional

# Базовая схема для оборудования
class EquipmentBase(BaseModel):
    name: str
    description: str
    availability_start: time
    availability_end: time

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    id: int

    class Config:
        orm_mode = True

# Схема для пользователя
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str  # Здесь храним пароль для создания

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

# Схема для бронирования
class BookingBase(BaseModel):
    user_id: int
    equipment_id: int
    start_time: datetime
    end_time: datetime

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True

# Схема для чек-листа
class ChecklistBase(BaseModel):
    user_id: int
    equipment_id: int
    steps: str

class ChecklistCreate(ChecklistBase):
    pass

class Checklist(ChecklistBase):
    id: int

    class Config:
        orm_mode = True
