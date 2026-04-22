logs = [
    ("ivan", 8), ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]

total_hours = {}

for employee, hours in logs:
    total_hours[employee] = total_hours.get(employee, 0) + hours

overtime = [emp for emp, hrs in total_hours.items() if hrs > 40]
undertime = [emp for emp, hrs in total_hours.items() if hrs < 20]

print("Общее количество часов по каждому сотруднику:")
for emp, hrs in total_hours.items():
    print(f"{emp}: {hrs}")

print("Сотрудники с переработкой (> 40 часов):")
if overtime:
    for emp in overtime:
        print(emp)
else:
    print("Нет сотрудников с переработкой.")

print("Сотрудники с недоработкой (< 20 часов):")
if undertime:
    for emp in undertime:
        print(emp)
else:
    print("Нет сотрудников с недоработкой.")