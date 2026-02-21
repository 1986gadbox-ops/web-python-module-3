from collections import defaultdict, Counter

purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]


purchase_counts = defaultdict(int)
for purchase in purchases:
    purchase_counts[purchase["user"]] += 1


total_spent = defaultdict(int)
for purchase in purchases:
    total_spent[purchase["user"]] += purchase["price"]


user_unique_items = defaultdict(set)
user_total_items_count = defaultdict(int)
for purchase in purchases:
    user = purchase["user"]
    items = purchase["items"]
    user_unique_items[user].update(items)
    user_total_items_count[user] += len(items)


all_items = []
for purchase in purchases:
    all_items.extend(purchase["items"])
item_counter = Counter(all_items)
most_common_item, count = item_counter.most_common(1)[0]


max_spent_user = max(total_spent.items(), key=lambda x: x[1])[0]
max_items_user = max(user_total_items_count.items(), key=lambda x: x[1])[0]


user_purchases_times = defaultdict(list)
for purchase in purchases:
    user = purchase["user"]
    timestamp = purchase["timestamp"]
    user_purchases_times[user].append(timestamp)


print("1. Общее количество покупок каждого пользователя:")
for user, count in purchase_counts.items():
    print(f"{user}: {count}")

print("\n2. Общая сумма потраченных денег каждым пользователем:")
for user, total in total_spent.items():
    print(f"{user}: {total}")

print("\n3. Уникальные товары каждого пользователя:")
for user, items in user_unique_items.items():
    print(f"{user}: {items}")

print("\nОбщее количество купленных товаров (учитывая повторы):")
for user, count in user_total_items_count.items():
    print(f"{user}: {count}")

print(f"\n4. Самый часто покупаемый товар: {most_common_item} (количество: {count})")

print(f"\n5. Пользователь, потративший больше всего денег: {max_spent_user}")
print(f"Пользователь, купивший больше всего товаров: {max_items_user}")

print("\n6. Максимальный перерыв между покупками каждого пользователя:")
for user, times in user_purchases_times.items():
    sorted_times = sorted(times)
    max_gap = max(
        sorted_times[i+1] - sorted_times[i]
        for i in range(len(sorted_times)-1)
    )
    print(f"{user}: {max_gap}")