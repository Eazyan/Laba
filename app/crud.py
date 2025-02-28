from sqlalchemy.orm import Session
from . import models, schemas

# Создание нового оборудования
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

# Создание нового пользователя
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Создание нового бронирования
def create_booking(db: Session, booking: schemas.BookingCreate):
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

# Получение всех бронирований
def get_bookings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Booking).offset(skip).limit(limit).all()

from sqlalchemy.orm import Session
from . import models, schemas

def get_equipment_list(db: Session, skip: int = 0, limit: int = 10):
    """
    Функция для получения списка оборудования из базы данных с поддержкой пагинации
    """
    return db.query(models.Equipment).offset(skip).limit(limit).all()
