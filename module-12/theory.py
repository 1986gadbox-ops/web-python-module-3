# поведенческие паттерны
# Template Method

class ReportTemplate:
    def build(self):
        data = self.fetch_data()
        return self.format_data(data)

    def fetch_data(self):
        raise NotImplementedError

    def format_data(self, data):
        raise NotImplementedError

class SelesReport(ReportTemplate):
    def fetch_data(self):
        return[100,200,300]

    def formst_data(self, data):
        return f"Сумма продаж: {sum(data)}"

print(SelesReport().build())

# Visitor

class Book:
    def __init(self, title, price):
        self.title = title
        self.price = price

    def accept(self, Visitor):
        return Visitor.visit_book(self)

class Course:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, book):
        return Visitor.visit_course(self)

class DiscountVisitor:
    def visit_book(self, book):
        return f"{book.title}: {book.prise * 0.9}"

    def visit_course(self, course):
        return f"{cours.title}: {course.price * 0.9}"

visitor = DiscountVisitor()
items = [Book("book", 1000) Course("course", 5000)]
for item in items:
    print(item.accept(visitor))