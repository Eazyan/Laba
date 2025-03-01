from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from datetime import datetime

# Проверка на пересечение бронирования
def check_booking_conflict(db: Session, equipment_id: int, start_time: datetime, end_time: datetime):
    conflicting_bookings = db.query(models.Booking).filter(
        models.Booking.equipment_id == equipment_id,
        models.Booking.start_time < end_time,
        models.Booking.end_time > start_time
    ).all()
    return conflicting_bookings


# Создание нового бронирования
def create_booking(db: Session, booking: schemas.BookingCreate):
    conflict = check_booking_conflict(db, booking.equipment_id, booking.start_time, booking.end_time)
    if conflict:
        raise HTTPException(status_code=400, detail="Booking conflict detected")
    
    db_booking = models.Booking(
        user_id=booking.user_id,
        equipment_id=booking.equipment_id,
        start_time=booking.start_time,
        end_time=booking.end_time
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# Получение списка бронирований
def get_bookings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Booking).offset(skip).limit(limit).all()

# Получение списка оборудования с пагинацией
def get_equipment_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Equipment).offset(skip).limit(limit).all()

def create_equipment(db: Session, equipment: schemas.EquipmentCreate):
    db_equipment = models.Equipment(
        name=equipment.name,
        description=equipment.description,
        availability_start=equipment.availability_start,
        availability_end=equipment.availability_end
    )
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment