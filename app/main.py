from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Разрешаем доступ с localhost:3000 (или другого домена)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем доступ с этого домена
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Создание таблиц при старте приложения
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)

# Функция для получения сессии базы данных
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для получения списка оборудования
@app.get("/equipments/", response_model=list[schemas.Equipment])
def read_equipment(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    equipments = crud.get_equipment_list(db, skip=skip, limit=limit)
    return equipments

# Маршрут для создания нового оборудования
@app.post("/equipments/", response_model=schemas.Equipment)
def create_equipment(equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    return crud.create_equipment(db=db, equipment=equipment)

# Маршрут для создания пользователя
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Маршрут для создания нового бронирования
@app.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)

# Маршрут для получения списка бронирований
@app.get("/bookings/", response_model=list[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

# Маршрут для создания чек-листа
@app.post("/checklists/", response_model=schemas.Checklist)
def create_checklist(checklist: schemas.ChecklistCreate, db: Session = Depends(get_db)):
    return crud.create_checklist(db=db, checklist=checklist)
