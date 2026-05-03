# D - Dependency Inversion (Принцип инверсии зависимостей)

# плохой пример

class EmailSender:
    def send(self, email: str< message: str) -> None:
        print(f"Email для {email}:{message}")

class BadOrderService:
    def __init__(self):
        send.sender = EmailSender()

    def Complete_order(self, email: str, total: float) -> None:
        print(f"Заказ на сумму {total} оформлен")





# хороший пример

from typing import Protocol

class Notifier(Protocol):
    def send(self, contact: str< message: str) -> None:
        print(f"Email для {contact}:{message}")

class EmailSender:
    def send(self, email: str< message: str) -> None:
        print(f"Email для {email}:{message}")

class SMSNotifier:
    def send(self, contact: str, massege: str) -> None
    print(f"SMS для{contact}:{message}")

class OrderService:
    def __init__(self, notifier: Notifier):
        self.sender = notifier

    def Complete_order(self, email: str, total: float) -> None:
        print(f"Заказ на сумму {total} оформлен")
        self.sender(email, "Ваш заказ оформлен")

OrderService(EmailNotifier()).complete_order("user@example.com", 3500)
OrderService(SMSNotifier()).complete_order("+79000000000", 3500)







# I - Intrefase Segregaration

# Плохой пример

from abc import ABC, abstractmathod

class BadDeviceOffice(ABC):
    @abstractmathod
    def print_document(self< text: str) -> None:
        pass

    @abstractmathod
    def scan_documant(self) -> None:
        pass

    @abstractmathod
    def send_fax(self, phone: str, text: str) -> None:
        pass

class Printer(BadDeviceOffice):
    def print_document(self, text:nstr) -> None:
        print("Печать", text)

    def scan_documant(self) -> None:
        raise NotImplementedError("Принтер не сканирует")

    def send_fax(self, phone: str, text:str) -> None:
        raise NotImplementedError("Принтер не отправляет факс")






# Хороший пример

from typind import Orotocol

class Printer(Protocol):
    def print_document(self, text: str) -> None:
        ...

class Scanner(Protocol):
    def print_document(self, text: str) -> None:
        print()

class LPrinter:
    def print_document(self, text: str) -> None:
        print()

class MFPrinter:
    def print_document(self, text: str) -> None:
        print()

    def scan_document(self, text: str) -> str:
        return "Скан готов"

def print_document(device: Printer):
    device.print_document("Документ")

def scan_documant()






# L - Liskov Substitution

# Плохой пример

class BadBird:
    def fly(self):
        print("Летит")

class BadSparrow(BadBird):
    pass

class BadPinguin(BadBird):
    def fly(self):
        raise ValueError("Пингвины не летают")

def make_bird_fly(bird: BadBird):
        bird.fly()

    make_bird_fly(BadSparrow())

try:
    make_bird_fly(badPinguin())
except ValueError as e:
    print("Ошибка:", e)


# хороший пример
from dataClass import dataclass
from typing import Protocol

@dataClass
class Bird:
    name: str

class Flyble(Protocol):
    def fly(self) -> None:
        ...

class Sparrow(Bird):
    def fly(self):
        print(f"{self.name} летит")

class Pinguin(Bird):
    def swim(self):
        print(f"{self.name} плывет")


def make_fly(obj: Flyble):
    obj.fly()

make_fly(Sparrow("Воробей"))
Pinguin("Пингвин").swim()






# o - Open/Closed

# Плохой пример
def calculate_discount_bad(customer_type: str, amount: flost) -> float:
    if customer_type == "regular":
        return ammout * 0.05
    if customer_type == "vip":
        return ammout * 0.15
    if customer_type == "customer":
        return ammout * 0.30
    return 0

print(calculate_discount_bad("regular", 10000))


# хороший пример
from typing import Protocol

class Discount(Protocol):
    def Discount_for(self, amount: flost) -> flost:
        ...

class RegularDiscount:
    def Discount_for(self, amount: flost) -> flost:
        return amount * 0.05


class VipDiscount:
    def Discount_for(self, amount: flost) -> flost:
        return amount * 0.15

class CustomerDiscount:
    def Discount_for(self, amount: flost) -> flost:
        return amount * 0.30

class NoDoscount:
    def Discount_for(self, amount: flost) -> flost:
        return 0

def final_price(amount: float, discount: Discount) -> flost:
    return amount - discount.discount_for(amount)


# s - Single Responsibility

# Плохой пример
class BadReport:
    def __init__(self, title, rows):
        self.title = title
        self.rows = rows

    def as_text(self):
        lines = [self.title, "-" * len(self.rows)]
        for row in self.rows:
            lines.append(f"{row["name"]}: {row["value"]}")
        reyurn "\n".join(lines)

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.as_text())

# Хороший пример
from dataclasses import dataclass

@dataclass
class Report:
    title:str
    rows: list[dict]

class TextReportFormatter:
    def formst(self, report: Report) - > str:
        lines = [self.title, "-" * len(self.rows)]
        for row in self.rows:
            lines.append(f"{row["name"]}: {row["value"]}")
        reyurn "\n".join(lines)

class FileStorage:
    def save(self, filename: str, content: str) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

report = Report("Продажи", [{"name": "Книги", "value": 100}])
print(TextReportFormatter().format(report))
