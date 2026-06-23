import os
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey,
    Boolean, Date, DateTime, inspect, UniqueConstraint
)
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
from pprint import pprint

# Вводите свою строку соединения
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///hospital.db")
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Specialization(Base):
    __tablename__ = 'specializations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    doctors = relationship('Doctor', back_populates='specialization')

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    location = Column(String(255))
    doctors = relationship('Doctor', back_populates='department')
    donations = relationship('Donation', back_populates='department')

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100))
    salary = Column(Float, default=0)
    specialization_id = Column(Integer, ForeignKey('specializations.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))

    specialization = relationship('Specialization', back_populates='doctors')
    department = relationship('Department', back_populates='doctors')
    examinations = relationship('Examination', back_populates='doctor')

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100))
    date_of_birth = Column(Date)
    examinations = relationship('Examination', back_populates='patient')

class Examination(Base):
    __tablename__= 'examinations'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    date = Column(DateTime, default=datetime.utcnow)
    description = Column(String(255))
    department_id = Column(Integer, ForeignKey('departments.id'))

    patient = relationship('Patient', back_populates='examinations')
    doctor = relationship('Doctor', back_populates='examinations')
    department = relationship('Department')

class Donation(Base):
    __tablename__ = 'donations'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, default=datetime.utcnow)
    sponsor = Column(String(100))
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship('Department', back_populates='donations')


def create_tables():
    Base.metadata.create_all(engine)
    print("Таблицы созданы.")

def drop_tables():
    Base.metadata.drop_all(engine)
    print("Таблицы удалены.")

def print_all_records(model):
    records = session.query(model).all()
    if not records:
        print("Нет записей.")
    else:
        for rec in records:
            print(rec.__dict__)

def get_model_by_name(name):
    models = {
        'specializations': Specialization,
        'departments': Department,
        'doctors': Doctor,
        'patients': Patient,
        'examinations': Examination,
        'donations': Donation
    }
    return models.get(name)

def confirm_action(message):
    answer = input(f"{message} (да/нет): ").lower()
    return answer == 'да'

def insert_record():
    table_name = input("Введите название таблицы для вставки: ").lower()
    model = get_model_by_name(table_name)
    if not model:
        print("Неизвестная таблица.")
        return
    data = {}
    for col in model.__table__.columns:
        if col.name == 'id':
            continue
        val = input(f"Введите значение для {col.name} ({col.type}): ")
        # преобразование типов
        if isinstance(col.type, Integer):
            val = int(val)
        elif isinstance(col.type, Float):
            val = float(val)
        elif isinstance(col.type, Date):
            val = datetime.strptime(val, '%Y-%m-%d').date()
        data[col.name] = val
    new_record = model(**data)
    session.add(new_record)
    session.commit()
    print("Запись добавлена.")

def update_records():
    table_name = input("Введите название таблицы для обновления: ").lower()
    model = get_model_by_name(table_name)
    if not model:
        print("Неизвестная таблица.")
        return
    print("Текущие записи:")
    print_all_records(model)
    ids = input("Введите ID записей для обновления через запятую: ")
    id_list = [int(i.strip()) for i in ids.split(',')]
    if not confirm_action("Обновить выбранные записи?"):
        return
    for record_id in id_list:
        rec = session.query(model).get(record_id)
        if not rec:
            print(f"Запись с ID {record_id} не найдена.")
            continue
        print(f"Обновляем запись: {rec.__dict__}")
        for col in model.__table__.columns:
            if col.name == 'id':
                continue
            new_val = input(f"Введите новое значение для {col.name} (оставьте пустым для пропуска): ")
            if new_val:
                if isinstance(col.type, Integer):
                    new_val = int(new_val)
                elif isinstance(col.type, Float):
                    new_val = float(new_val)
                elif isinstance(col.type, Date):
                    new_val = datetime.strptime(new_val, '%Y-%m-%d').date()
                setattr(rec, col.name, new_val)
    session.commit()
    print("Обновление завершено.")

def delete_records():
    table_name = input("Введите название таблицы для удаления: ").lower()
    model = get_model_by_name(table_name)
    if not model:
        print("Неизвестная таблица.")
        return
    print("Текущие записи:")
    print_all_records(model)
    ids = input("Введите ID записей для удаления через запятую: ")
    id_list = [int(i.strip()) for i in ids.split(',')]
    if not confirm_action("Удалить выбранные записи?"):
        return
    for record_id in id_list:
        rec = session.query(model).get(record_id)
        if rec:
            session.delete(rec)
    session.commit()
    print("Удаление завершено.")

def generate_reports():
    print("Выберите отчет:")
    print("1: Врачи и их специализации")
    print("2: Фамилии врачей и зарплаты (без отпуска)")
    print("3: Названия отделений")
    print("4: Отделения по спонсору")
    print("5: Пожертвы по месяцу")
    print("6: Врачи и их обследования")
    choice = input("Введите номер: ")

    if choice == '1':
        # Врачи и специализации
        results = session.query(Doctor.last_name, Specialization.name).join(Specialization).all()
        for last_name, spec in results:
            print(f"{last_name} - {spec}")
    elif choice == '2':
        # Фамилии и зарплаты
        results = session.query(Doctor.last_name, Doctor.salary).filter(Doctor.department_id != None).all()
        for last_name, salary in results:
            print(f"{last_name} - {salary}")
    elif choice == '3':
        # Названия отделений
        departments = session.query(Department.name).distinct().all()
        for (name,) in departments:
            print(name)
    elif choice == '4':
        # Отделения по спонсору
        sponsor_name = input("Введите название спонсора: ")
        results = session.query(Department.name).join(Donation).filter(Donation.sponsor == sponsor_name).distinct().all()
        for (name,) in results:
            print(name)
    elif choice == '5':
        # Пожертвы по месяцу
        month_str = input("Введите месяц и год (ММ-ГГГГ): ")
        month, year = month_str.split('-')
        start_date = datetime(int(year), int(month), 1)
        if month == '12':
            end_date = datetime(int(year)+1, 1, 1)
        else:
            end_date = datetime(int(year), int(month)+1, 1)
        donations = session.query(Department.name, Donation.sponsor, Donation.amount, Donation.date).join(Department).filter(Donation.date >= start_date, Donation.date < end_date).all()
        for dept_name, sponsor, amount, date in donations:
            print(f"{dept_name} | {sponsor} | {amount} | {date.strftime('%Y-%m-%d')}")
    elif choice == '6':
        # Врачи и отделения, где проводят обследования
        results = session.query(Doctor.last_name, Department.name).join(Examination).join(Department).distinct().all()
        for last_name, dept_name in results:
            print(f"{last_name} - {dept_name}")
    else:
        print("Некорректный выбор.")

def show_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Таблицы в базе данных:")
    for t in tables:
        print(t)

def show_table_columns():
    table_name = input("Введите название таблицы: ")
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    print(f"Столбцы таблицы {table_name}:")
    for col in columns:
        print(f"{col['name']} - {col['type']}")

def show_table_schema():
    table_name = input("Введите название таблицы: ")
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    print(f"Структура таблицы {table_name}:")
    for col in columns:
        print(f"{col['name']} : {col['type']}")

def show_foreign_keys():
    table_name = input("Введите название таблицы: ")
    inspector = inspect(engine)
    fks = inspector.get_foreign_keys(table_name)
    if not fks:
        print("Связей не найдено.")
        return
    for fk in fks:
    constrained_cols = fk['constrained_columns']
    referred_table = fk['referred_table']
    referred_cols = fk['referred_columns']
    print(f"Связь: {constrained_cols} -> {referred_table}.{referred_cols}")