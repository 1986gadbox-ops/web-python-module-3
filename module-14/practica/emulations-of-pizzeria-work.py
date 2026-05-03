from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float

@dataclass
class Recipe:
    name: str
    ingredient_keys: list[str]

class RecipeFactory:
    def get_standard_recipes() -> dict[int, Recipe]:
        return {
            0: Recipe("Пицца-1", ["dough", "tomate","mayonnaise", "chiken"]),
            1: Recipe("Пицца-2", ["dough", "tomate","ketchup", "chiken"]),
            2: Recipe("Пицца-3", ["dough", "tomate", "chiken"])
        }

class PizzaBuilder:
    def __init__(self):
        self._ingredient = ["dough", "cheese"]

    def add_ingredient(self, key: str):
        if key not in self._ingredient:
            self._ingredient.append(key)
        return self


    def byild(self):
        return Recipe("Своя пицца", self._ingredient)


@dataclass
class OrderItem:
    recipe: Recipe
    quantity: int

    def total_price(self, ingredients: dict[int, Ingredient]) -> float:
        one_pizza_price = sum(
            ingredients[key].price for key in self.recipe.ingredient_keys
        )

        return one_pizza_price * self.quantity

    def total_cost(self, ingredients: dict[int, Ingredient]) -> float:
        pass

@dataclass
class Order:
    items: list[OrderItem]
    payment_type: str

    def total_price(self, ingredients: dict[str, Ingredient]):
        return sum (item.total_price(ingredients) for item in self.items)

    def total_cost(self, ingredients: dict[str, Ingredient]):
        return sum (item.total_cost(ingredients) for item in self.items)

    def total_profit(self, ingredients: dict[str, Ingredient]):
        return sum (item.total_price(ingredients) for item in self.items)


    def to_text(self, ingredients: dict[str, Ingredient]) -> str:
        lines = ["Информация о заказе:"]

        for item in self.items:
            ingredients_names = [
                ingredients[key].name for key in item.recipe.ingredient_keys
            ]

            lines.append(f"Пицца: {item.recipe.name}")
            lines.append(f"Количество: {item.quantity}")
            lines.append("Состав")

            for name in ingredients_names:
                lines.append(f"- {name}")

            lines.append(f"Цена позиции: {item.total_price(ingredients)} руб")

        lines.append(f"Способ оплаты: {self.payment_type}")

        return "\n".join(lines)

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        return (f"Оплата наличными выполнена на сумму {amount} руб.")

class CardPament(PaymentStrategy):
    def pay(self, amount: float):
        return (f"оплата картой выполнена на сумму {amount} руб")


class FileOrderSaver:
    def __init__(self, filename: str = "order.txt"):
        self.filename = filename

    def save(self, order: Order, ingredients: dict[str, Ingredient]):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(order.to_text(ingredients))
            file.write("\n" + "-" * 50 + "\n")

def create_ingredients():
    return {
        "dough": Ingredient("Тесто", "dough", 70, 30),
        "cheese": Ingredient("сыр", "cheese", 80, 20),
        "tomate": Ingredient("Помидор", "tomate", 20, 5),
        "mayonnaise": Ingredient("Майонез", "mayonnaise", 50, 10),
        "chiken": Ingredient("курица", "chiken", 100, 3),
        "ketchup": Ingredient("Кетчуп", "ketchup", 15, 3),
        }
def create_stock() -> dict[str, int]:
    return{
        "dough": 10,
        "cheese": 10,
        "tomate": 10,
        "mayonnaise": 10,
        "chiken": 10,
        "ketchup": 10
        }
def get_topping() -> list[str]:
    return[
        "tomate",
        "mayonnaise",
        "chiken",
        "ketchup"
        ]

def create_custom_recipe(inventory: Inventory) -> Recipe:
    builder = PizzaBuilder()

    print("Создание своей пиццы")
    for key in get_topping():
        ingredient = inventory.ingredients[key]

        choice = input(f"Хотите добавить {ingredient.name}")
        if choice == "да":
            builder.add_ingredient(ingredient.key)

    return builder.build()

class Inventory:
    def __init__(self, ingredients: dict[str, Ingredient], stock: dict[str, int]):
        self.ingredients = ingredients
        self.stock = stock

    def has_enough(self, ingredient_keys: list[str], quantity: int) -> bool:
        for key in ingredient_keys:
            if self.stock.get(key, 0) < quantity:
                return False
        return True

    def reduce_stock(self, ingredient_keys: list[str], quantity: int):
        for key in ingredient_keys:
            self.stock[key] -=quantity

    def show(self):
        print("Наличие ингридиентов")

        for key, count in self.stock.items():
            ingredient = self.ingredients[key]
            print(f"{ingredient.name}: {count}")

class SelesReport:
    def __init__(self):
        self.profit = 0
        self.revenue = 0
        self.sold_count = 0

    def add_order(self,order: Order, ingredients: dict[str, Ingredient]):

        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print("Отчет")
        print(f"Продано птиц: {self.sold_count}")
        print(f"Выручка: {self.profit}")
        print(f"Доход: {self.revenue}")

def show_menu():
    print("1. Создать заказ")
    print("2. Отчет")
    print("3. Наличие ингридиентов")
    print("4. Выход")


# -- 

def show_standard_recipes(
    recipes: dict[int, Recipe],
    ingredients: dict[str, Ingredient]
    ):
    print("Стандартные пицца")

    for number, recipe in recipes.items():
        print(f"{number}. {recipe.name}")

        price = sum(ingredients[key].price for key in recipe.ingredient_keys)

def choose_recipe(
    recipes: dict[int, Recipe],
    ingredients: dict[str, Ingredient],
    inventory: Inventory
    ):

    while True:
        choice = input("Выберите вариант: ")
        if choice == "0":
            return create_custom_recipe(inventory)
        else:
            return recipes[int(choice)]

def choose_payment():
    print("Выберите способ оплаты:")
    print("1 - наличные")
    print("2 - карта")

    while True:
        choice = input("Выберите: ")

        if choice == "1":
            return CardPament(), "Наличные"
        elif choice == "2":
            return CardPament(), "карта"

        print("Выберите между 1 и 2 вариантом")


def create_order(
    ingredients: dict[str, Ingredient],
    inventory: Inventory,
    report: SalesReport,
    file_saver: FileOrderSaver
    ):
    recipes = RecipeFactory.get_standard_recipes()
    items: list[OrderItem] = []

    while True:
        show_standard_recipes(recipes, ingredients)

        recipe = choose_recipe(recipes, ingredients, inventory)
        quantity = int(input("Введите количество: "))

        if not inventory.has_enough(recipe.ingredient_keys, quantity):
            print("Недостаточно ингридиентов для заказа.")
            return

        items.append(OrderItem(recipe,quantity))

        more = input("Добавить еще один вид пиццы?")

        if more == "нет":
            break

    payment_strategy, payment_type = choose_payment()

    order = Order(items, payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys, item.quantity)
        
        
    # сумма заказа
    amount = order.total_price(ingredients)

    # оплата
    print(payment_strategy.pay(amount))
    # сохранение заказа
    file_saver.save(order, ingredients)

    # добавление заказа в отчет
    report.add_order(order, ingredients)

def main():
    ingredients = create_ingredients()
    stock = create_stock()

    inventory = Inventory(ingredients, stock)
    report = SelesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()
        print(ingredients)
        choice = input("Выберите пункт меню")
        if choice == "1":
            create_order(ingredients, inventory, report, file_saver)
        elif choice =="2":
            report.show()
        elif choice == "3":
            inventory.show()
        elif choice =="4":
            break

main()


   