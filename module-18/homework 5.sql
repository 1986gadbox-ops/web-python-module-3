import os
from sqlalchemy import (create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime, func)
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError
from datetime import datetime


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:password@localhost:5432/inventory_db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Category(Base):
    __tablename__='categories'
    id=Column(Integer, primary_key=True)
    name= Column(String, nullable=False, unique=True)
    products= relationship('Product', back_populates='category', cascade='all, delete')

class Supplier(Base):
    __tablename__='suppliers'
    id=Column(Integer, primary_key=True)
    name= Column(String, nullable=False, unique=True)
    phone= Column(String)
    email= Column(String, unique=True)
    is_active= Column(Boolean, default=True)
    created_at= Column(DateTime, default=datetime.utcnow)
    products= relationship('Product', back_populates='supplier', cascade='all, delete')

class Product(Base):
    __tablename__='products'
    id=Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    sku= Column(String, nullable=False, unique=True)
    category_id= Column(Integer, ForeignKey('categories.id'))
    supplier_id= Column(Integer, ForeignKey('suppliers.id'))
    purchase_price= Column(Float, nullable=False)
    selling_price= Column(Float, nullable=False)
    min_quantity= Column(Integer, nullable=False)
    is_active= Column(Boolean, default=True)
    created_at= Column(DateTime, default=datetime.utcnow)
    category= relationship('Category', back_populates='products')
    supplier= relationship('Supplier', back_populates='products')
    stock_movements= relationship('StockMovement', back_populates='product', cascade='all, delete')

class StockMovement(Base):
    __tablename__='stock_movements'
    id=Column(Integer, primary_key=True)
    product_id= Column(Integer, ForeignKey('products.id'))
    movement_type= Column(String)  # IN, OUT, ADJUST
    quantity= Column(Integer)
    comment= Column(String)
    created_at= Column(DateTime, default=datetime.utcnow)
    product= relationship('Product', back_populates='stock_movements')

def create_tables():
    Base.metadata.create_all(engine)
    print("Таблицы созданы.")

def drop_tables():
    Base.metadata.drop_all(engine)
    print("Таблицы удалены.")

def create_category(name):
    try:
        c= Category(name=name)
        session.add(c)
        session.commit()
        print(f"Категория '{name}' добавлена.")
    except IntegrityError:
        session.rollback()
        print("Ошибка: такая категория уже есть.")

def get_all_categories():
    cats= session.query(Category).all()
    for c in cats:
        print(f"{c.id}: {c.name}")

def create_supplier(name, phone=None, email=None):
    try:
        s= Supplier(name=name, phone=phone, email=email)
        session.add(s)
        session.commit()
        print(f"Поставщик '{name}' добавлен.")
    except IntegrityError:
        session.rollback()
        print("Ошибка: такой поставщик есть или email занят.")

def get_all_suppliers():
    for s in session.query(Supplier).all():
        print(f"{s.id}: {s.name} (активен:{s.is_active})")

def create_product(name, sku, category_id, supplier_id=None, purchase_price=0, selling_price=0, min_quantity=0):
    try:
        p= Product(
            name=name, sku=sku, category_id=category_id,
            supplier_id=supplier_id, purchase_price=purchase_price,
            selling_price=selling_price, min_quantity=min_quantity
        )
        session.add(p)
        session.commit()
        print(f"Товар '{name}' добавлен.")
    except IntegrityError:
        session.rollback()
        print("Ошибка: sku уже существует или неверные данные.")

def add_stock_movement(product_id, movement_type, quantity, comment=None):
    if quantity <=0:
        print("Количество должно быть больше 0.")
        return
    if movement_type not in ('IN','OUT','ADJUST'):
        print("Некорректный тип операции.")
        return
    try:
        p= session.query(Product).get(product_id)
        if not p:
            print("Товар не найден.")
            return
        sm= StockMovement(
            product_id=product_id,
            movement_type=movement_type,
            quantity=quantity,
            comment=comment
        )
        session.add(sm)
        session.commit()
        print("Операция добавлена.")
    except Exception as e:
        session.rollback()
        print("Ошибка при добавлении операции:", e)

def get_stock_balance(product_id):
    in_sum= session.query(func.sum(StockMovement.quantity)).filter_by(product_id=product_id, movement_type='IN').scalar() or 0
    out_sum= session.query(func.sum(StockMovement.quantity)).filter_by(product_id=product_id, movement_type='OUT').scalar() or 0
    adjust_sum= session.query(func.sum(StockMovement.quantity)).filter_by(product_id=product_id, movement_type='ADJUST').scalar() or 0
    return in_sum + adjust_sum - out_sum

def get_all_products():
    for p in session.query(Product).all():
        stock= get_stock_balance(p.id)
        print(f"{p.id}: {p.name} (SKU:{p.sku}) - Остаток: {stock}")

def report_products_warehouse_value():
    total=0
    for p in session.query(Product).all():
        stock= get_stock_balance(p.id)
        total+= stock * p.purchase_price
        print(f"{p.name}: Остаток {stock}, Стоимость закупки {stock*p.purchase_price}")
    print(f"Общая стоимость складских остатков: {total}")

def report_products_selling_potential():
    total=0
    for p in session.query(Product).all():
        stock= get_stock_balance(p.id)
        total+= stock * p.selling_price
        print(f"{p.name}: Остаток {stock}, Потенциальная выручка {stock*p.selling_price}")
    print(f"Общая потенциальная выручка: {total}")

def report_products_profit():
    total=0
    for p in session.query(Product).all():
        stock= get_stock_balance(p.id)
        profit= stock * (p.selling_price - p.purchase_price)
        total+= profit
        print(f"{p.name}: Остаток {stock}, Потенциальная прибыль {profit}")
    print(f"Общая потенциальная прибыль: {total}")

def report_low_stock():
    print("Товары, которые заканчиваются или у которых остатков меньше минимального:")
    for p in session.query(Product).all():
        stock= get_stock_balance(p.id)
        if stock <= p.min_quantity:
            print(f"{p.name}: Остаток {stock}, Минимальный {p.min_quantity}")

def report_current_stock():
    for p in session.query(Product).all():
        print(f"{p.name}: Остаток {get_stock_balance(p.id)}")

def seed():
    create_tables()
    for name in ['Electronics','Furniture','Office Supplies','Tools']:
        create_category(name)
    # Поставщики
    for name in ['TechTrade','OfficeMarket','WoodFactory','GlobalTools']:
        create_supplier(name)
    try:
        create_product('Laptop Lenovo ThinkPad', 'SKU0001', 1, 1, 70000, 95000, 2)
        create_product('Wireless Mouse', 'SKU0002', 1, 4, 2000, 3500, 5)
        create_product('Office Chair', 'SKU0003', 2, 2, 10000, 15000,3)
        create_product('A4 Paper Pack', 'SKU0004', 3, 3, 500, 1000,10)
        create_product('Screwdriver Set', 'SKU0005', 4, 4, 1500, 2500,3)
        create_product('Monitor 27 inch', 'SKU0006', 1, 1, 12000,18000,2)
    except:
        pass


def main():
    create_tables()
    while True:
        print("\n=== Inventory Manager CLI ===")
        print("1. Создать категорию")
        print("2. Показать все категории")
        print("3. Создать поставщика")
        print("4. Показать всех поставщиков")
        print("5. Создать товар")
        print("6. Показать все товары")
        print("7. Добавить операцию (поступление/списание/корректировка)")
        print("8. Отчёты по складу")
        print("0. Выход")
        ch= input("Выберите: ")
        if ch=='1':
            name= input("Название категории: ")
            create_category(name)
        elif ch=='2':
            get_all_categories()
        elif ch=='3':
            n= input("Имя поставщика: ")
            p= input("Телефон: ")
            e= input("Email: ")
            create_supplier(n,p,e)
        elif ch=='4':
            get_all_suppliers()
        elif ch=='5':
            name= input("Название: ")
            sku= input("SKU: ")
            cat_id= int(input("ID категории: "))
            supp_id= int(input("ID поставщика: "))
            create_product(name, sku, cat_id, supp_id)
        elif ch=='6':
            get_all_products()
        elif ch=='7':
            print("Добавить операцию:")
            product_id= int(input("ID продукта: "))
            print("Тип операции: IN, OUT, ADJUST")
            t= input("Тип: ").upper()
            q= int(input("Кол-во: "))
            c= input("Комментарий (необязательно): ")
            add_stock_movement(product_id, t, q, c)
        elif ch=='8':
            print("Отчёты:")
            print("1. Общая стоимость остатков")
            print("2. Потенциальная выручка")
            print("3. Потенциальная прибыль")
            print("4. Товары, заканчивающиеся")
            print("5. Текущий остаток по товарам")
            sel= input("Выберите: ")
            if sel=='1':
                report_products_warehouse_value()
            elif sel=='2':
                report_products_selling_potential()
            elif sel=='3':
                report_products_profit()
            elif sel=='4':
                report_low_stock()
            elif sel=='5':
                report_current_stock()
        elif ch=='0':
            break
        else:
            print("Некорректный выбор.")
    session.close()

if __name__=="__main__":  
    main()