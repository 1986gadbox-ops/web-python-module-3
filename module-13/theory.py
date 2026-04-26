# Model

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

class CartModel:
    def __init__(self):
        self.Products = {
            "apple": Product("Яблоко", 80),
            "banana": Product("Банан", 60),
            "coffee": Product("Кофе", 250)
        }
        self.items = []

    def add_items(self, product_code: str):
        if product_code not in self.products:
            raise ValueError("Такого товара нет в каталоге")
        self.items.append(self.products[product_code])

    def total(self):
        return sum(item.price for item in self.items)

    def item_names(self):
        return[item.price for item in self.items]

model = CartModel()
madel.add_item("apple")
model.add_item("coffee")
print(model.item_names())
print(model.total())

# Viev

class ConsoleCartView:
    @staticmethod
    def render_card(items, total):
        print("Корзина:")

        if items:
            for items in items:
                print(f"- {item}")

        else:
            print("-пусто")
        print(f" Итого {total}")

    @staticmethod
    def render_error(msg):
        print(f"Ошибка: {msg}")

ConsoleCartView.render_card(["Яблоко", "кофе"], 330)

# Controller

class CartController:
    def __init__(self, model: CartModel, view: ConsoleCartView):
        self.model = model
        self.view = view

    def add_product(self, product_code):
        try:
            self.model.add_item(product_code)
            self.view.render_card(self.model.item_names(), self.model.total())
        except ValueError as e:
            self.view.render_error(str(e))

Controller = CartController(CartModel(), ConsoleCartView())
Controller.add_product("banana")
Controller.add_product("coffee")
Controller.add_product("water")