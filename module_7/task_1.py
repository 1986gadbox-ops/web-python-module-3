"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""

operations = []

with open("inventory.txt", "w", encoding="utf-8") as f:
   operations = [
      "2024-01-01,яблоко,IN,50",
      "2024-01-02,банан,IN,30",
      "2024-01-03,яблоко,OUT,10",
      "2024-01-03,груша,OUT,5",
      "2024-01-04,груша,IN,20",
      "2024-01-05,банан,OUT,40",
      "2024-01-06,яблоко,OUT,5"
   ]

   f.write("\n".join(operations))

operations = []
product_dates = {}
with open("inventory.txt", "r", encoding="utf-8") as f:
   for line in f:
      date, product, op_type, quantity = line.strip().split(",")
      operations.append({ "date": date, "product": product, "op_type": op_type, "quantity": int(quantity) })

inventory = {}
total_in = {}
total_out = {} 

for op in operations:
    product = op["product"]
    qty = op["quantity"]
    product_dates.setdefault(product, set()).add(op["date"])
    if product not in inventory:
        inventory[product] = 0
        total_in[product] = 0
        total_out[product] = 0
    if op["op_type"] == "IN":
        inventory[product] += qty
        total_in[product] += qty  
    elif op["op_type"] == "OUT":
        inventory[product] -= qty
        total_out[product] += qty



print("Итоговое количество на складе:")
for product, qty in inventory.items():
    print(f"{product}: {qty}")

print(f"Общее количество поступивших единиц: {total_in}")
print(f"Общее количество отгруженных едениц: {total_out}")


negative_inventory = []
for product, amount in inventory.items():
   if amount < 0:
      negative_inventory.append(product)

out_without_in = [p for p in total_out if total_in.get(p, 0) == 0 and total_out[p] > 0]

print("Товары с отрицательным остатком (ошибка учёта):")
if negative_inventory:
    for p in negative_inventory:
        print(f"- {p}: {inventory[p]}")
else:
    print("Нет таких товаров.")

print("Товары, которые ни разу не поступали, но отгружались:")
if out_without_in:
    for p in out_without_in:
        print(f"- {p}: отгружено {total_out[p]} единиц")
else:
    print("Нет таких товаров.")



max_in_product = None
max_in_quantiti = -1
for product, quantity in total_in.items():
   if quantity > max_in_quantiti:
      max_in_product = product
      max_in_quantiti =quantity


max_out_product = None
max_out_quantiti = -1
for product, quantity in total_out.items():
   if quantity > max_out_quantiti:
      max_out_product = product
      max_out_quantiti =quantity

print(f"Товар с максимальным количеством поступлений - {max_in_product}")
print(f"Товар с максимальным количеством отгрузок - {max_out_product}")
product = "яблоко"

if product in product_dates:
    dates = product_dates[product]
    print(f"Даты операций с товаром '{product}':")
    for date in sorted(dates):
        print(date)






with open("report.txt", "w", encoding="utf-8") as f:
   f.write (f"Общее поступление: {total_in} \n "
           f"Общая отгрузка: {total_out}\n "
           f"Товары с отрицательным остатком: {p}: {inventory[p]}\n "
           f"Товары без поступлений, но с отгрузкой: {p}: отгружено {total_out[p]} единиц\n "
           f"Товар с максимальным поступлением: {max_in_product}\n" 
           f"Товар с максимальной отгрузкой:  {max_out_product}\n "
           f"Даты операций с яблоком: {date} ")
          