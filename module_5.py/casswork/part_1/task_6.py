logs = [
    ("ivan", "day", 8),
    ("ivan", "night", 4),
    ("olga", "day", 6),
    ("petr", "night", 7),
    ("anna", "day", 4),
    ("anna", "day", 3),
    ]

# employee_shift = {}
# for log in logs:
#     if log [0] not in employee_shift:
#         employee_shift [log[0]] = set()
#     employee_shift [log[0]].add(log[1])
# for employee in employee_shift:
#     value = employee_shift[employee]
#     if len(value) == 2:
#         print(employee)
# print(employee_shift)


# employee_shift = {}

# for log in logs:
#     if log [2] in employee_shift:
#         employee_shift[log[0]] += log[2]
#     else:
#         employee_shift[log[0]] = log[2]

# time = [name for name, total in employee_shift.items() if total < 8]

# print("Смены, где отработано менее 8 часов:", time)



# employee_shift = {}
# shift_hours = {}
# employee_hours = {}

# for name, shift, hours in logs:
#     if name not in employee_shift:
#         employee_shift[name] = set()
#     employee_shift[name].add(shift)

#     if shift not in shift_hours:
#         shift_hours[shift] = 0
#     shift_hours[shift] += hours

#     if name not in employee_hours:
#         employee_hours[name] = 0
#     employee_hours[name] += hours

# multiple_shift = []
# for employee in employee_shift:
#     if len(employee_shift[employee]) == 2:
#         multiple_shift.append(employee)

# shifts_less = []
# for shift in shift_hours:
#     if shift_hours[shift] < 8:
#         shifts_less.append(shift)

# employees = []

#     for employee in employee_hours:
#         if employee_hours[employee] >= 12:
#             employees.append(employee)

# print(employee_shift)
# print(shift_hours)
# print(employee_hours)



# задача 4(найти сущности с не корректным переходом)

history = [
    ("t_1", "new"), ("t_1", "in progress"),
    ("t_1", "done"),
    ("t_2", "new"), ("t_2", "done"),
    ("t_3", "new"), ("t_3", "in progress"),
    ("t_3", "cancelled"),
    ("t_4", "new"), ("t_4", "cancelled"),
    ("t_4", "done"),
]

allowed = {
    ("new", "in_progress"),
    ("in_progress", "done"),
    ("new", "cancelled"),
    ("in_progress", "cancelled")
}

last_status = {}
errors = {}
for entity, status in history:
    if entity not in last_status:
        last_status[entity] = status
        continue

    prev = last_status[entity]
    if (prev, status) not in allowed:
        if entity not in errors:
            errors[entity] = (prev, status)
    else:
        last_status[entity] = status

for entity, transition in errors.items():
    print(entity, ":", transition)