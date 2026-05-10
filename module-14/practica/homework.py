import json
from abc import ABC, abstractmethod


class Topping:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Recipe:
    def __init__(self, name, base_price, toppings):
        self.name = name
        self.base_price = base_price
        self.toppings = toppings 


class HotDog:
    def __init__(self, recipe, extra_toppings):
        self.recipe = recipe
        self.extra_toppings = extra_toppings

    def price(self):
        return self.recipe.base_price + sum([t.price for t in self.extra_toppings])

    def __str__(self):
        toppings = self.recipe.toppings + [t.name for t in self.extra_toppings]
        return f"{self.recipe.name} с дополнениями: {', '.join(toppings)} — {self.price():.2f}₽"


class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount(self, quantity):
        pass

class SimpleDiscount(DiscountStrategy):
    def get_discount(self, quantity):
        if quantity >= 10:
            return 0.20
        elif quantity >= 5:
            return 0.10
        elif quantity >= 3:
            return 0.05
        return 0.0


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата наличными: {amount:.2f}₽")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата картой: {amount:.2f}₽")


class Inventory:
    def __init__(self, toppings):
        self.toppings = toppings 

    def check_and_reserve(self, required):
        missing = []
        for topping in required:
            if self.toppings[topping].stock <= 0:
                missing.append(topping)
        if missing:
            return False, missing
        for topping in required:
            self.toppings[topping].stock -= 1
        return True, []

    def low_stock(self):
        return {name: t.stock for name, t in self.toppings.items() if t.stock < 3}


class Order:
    def __init__(self, hotdogs):
        self.hotdogs = hotdogs

    def total(self, discount_strategy):
        base = sum([hd.price() for hd in self.hotdogs])
        discount = discount_strategy.get_discount(len(self.hotdogs))
        return base * (1 - discount), discount

    def __str__(self):
        return '\n'.join([str(hd) for hd in self.hotdogs])


class Kiosk:
    def __init__(self):
        onion = Topping('Сладкий лук', 15, 10)
        jalapeno = Topping('Халапеньо', 20, 5)
        chili = Topping('Чили', 20, 3)
        cucumber = Topping('Солёный огурец', 10, 2)
        mayo = Topping('Майонез', 10, 7)
        mustard = Topping('Горчица', 10, 10)
        ketchup = Topping('Кетчуп', 10, 8)
        self.toppings = {
            t.name: t for t in [onion, jalapeno, chili, cucumber, mayo, mustard, ketchup]
        }
        classic = Recipe('Классический', 120, ['Кетчуп', 'Горчица'])
        veggie = Recipe('Вегетарианский', 125, ['Солёный огурец', 'Сладкий лук'])
        spicy = Recipe('Острый', 130, ['Чили', 'Халапеньо', 'Кетчуп'])
        self.recipes = [classic, veggie, spicy]
        self.inventory = Inventory(self.toppings)
        self.discount = SimpleDiscount()
        self.orders = []
        self.profit = 0

    def create_hotdog(self):
        print("Выберите рецепт или создайте свой:")
        for i, r in enumerate(self.recipes):
            print(f"{i+1}: {r.name} ({', '.join(r.toppings)})")
        print(f"{len(self.recipes)+1}: Свой рецепт")

        choice = int(input("> "))
        if 1 <= choice <= len(self.recipes):
            recipe = self.recipes[choice-1]
            base_toppings = [self.toppings[name] for name in recipe.toppings]
        else:
            name = input("Название хот-дога: ")
            recipe = Recipe(name, 100, [])
            base_toppings = []

        print("Выберите топпинги (через ,):")
        for i, t in enumerate(self.toppings.keys()):
            print(f"{i+1}: {t}")
        indexes = input("> ")
        ext_toppings = []
        for idx in indexes.split(","):
            try:
                topping = list(self.toppings.values())[int(idx)-1]
                ext_toppings.append(topping)
            except:
                pass
        all_toppings = set([t.name for t in base_toppings] + [t.name for t in ext_toppings])
        ok, missing = self.inventory.check_and_reserve(all_toppings)
        if not ok:
            print("Нет в наличии:", ', '.join(missing))
            return None
        return HotDog(recipe, ext_toppings)

    def make_order(self):
        hotdogs = []
        print("Сколько хот-догов в заказе?")
        n = int(input("> "))
        for _ in range(n):
            hd = self.create_hotdog()
            if hd: hotdogs.append(hd)
        if not hotdogs:
            print("Заказ не создан.")
            return
        order = Order(hotdogs)
        total, discount = order.total(self.discount)
        print(f"Ваш заказ:\n{order}")
        print(f"Итого: {total:.2f}₽ (скидка {int(discount*100)}%)")
        print("Выберите тип оплаты: 1 - наличные, 2 - карта")
        method = int(input("> "))
        pay_strategy = CashPayment() if method == 1 else CardPayment()
        pay_strategy.pay(total)
        self.orders.append(order)
        self.profit += total
        with open("orders.json", "a") as f:
            data = {"items":[hd.recipe.name for hd in hotdogs], "sum": total}
            f.write(json.dumps(data, ensure_ascii=False)+"\n")
        low = self.inventory.low_stock()
        if low:
            print("Внимание! Заканчиваются компоненты:", low)

    def show_stats(self):
        print(f"Заказано хот-догов: {sum([len(o.hotdogs) for o in self.orders])}")
        print(f"Выручка: {self.profit:.2f}₽")

    def show_inventory(self):
        print("Остатки компонентов:")
        for t in self.toppings.values():
            print(f"{t.name} — {t.stock}")

    def run(self):
        while True:
            print("\n1. Новый заказ\n2. Статистика\n3. Остатки\n4. Выход")
            cmd = input("> ")
            if cmd == "1":
                self.make_order()
            elif cmd == "2":
                self.show_stats()
            elif cmd == "3":
                self.show_inventory()
            elif cmd == "4":
                break

if __name__ == '__main__':
    kiosk = Kiosk()
    kiosk.run()