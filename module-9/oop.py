# from abc import ABC, abstractmethod

# class EmployeeBase(ABC):
#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id
#         self.name = name

#     @abstractmethod
#     def compensation(self):
#         pass

# class Employee(EmployeeBase):
#     company = "123123123"

#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary
#         self._salary = 0

#     def __str__(self):
#         return f"{self.name}: {self.salary}"

#     def __eq__(self):
#         if not isinstance(other, Employee):
#             return NotImplemented
#         return self.emp_id == other.emp_id

#     def __lt__(self,other):
#         if not isinstance(other, Employee):
#             return NotImplemented
#         return self.salary < other.salary

#     def info(self):
#         return f"{self.name} -> {self.salary}"

#     @classmethod
#     def from_string(cls, raw):
#         emp_id, name, salary = raw.split(",")
#         return cls(int(emp_id), name, int(salary))

#     @staticmethod
#     def valid_name(name):
#         return len(name.strip()) >= 2

#     def get_salary(self):
#         return self.salary

#     def set_salary(self, value):
#         if value < 0:
#             self.salary = 0
#         else:
#             self.salary = value


#     def compensation(self):
#         return self.set_salary

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, value):
#         self._salary = value

#     @salary.deleter
#     def salary(self):
#         self._salary = 0

#     def yearly_income(self):
#         return self.salary * 12

# class LoggableMixin:
#     def log(self, messages):
#         print(f"[LOG] {self.name}: {messages}")

# class Manager(Employee, LoggableMixin):
#     def __init__(self, emp_id, name, salary, bonus):
#         super().__init__(emp_id, name, salary)
#         self.bonus = bonus

#     def yearly_income(self):
#         return super().yearly_income() + self.bonus

# m = Manager(3, "Алексей", 2000, 5000)
# m1 = Manager(4, "Алиса", 1000, 2000)

# print(m < m1)
# print(m > m1)
# print(m.log("123123"))
# # print(m.yearly_income())

# print(Manager.__mro__)


# e = Employee.from_string("2,Андрей,3000")

# # e.set_salary(4000)

# e.salary = 4000

# # print(e.get_salary(), e.salary)
# print(e.salary)

# del e.salary
# print(e.salary)


# e = Employee(1, "Алиса", 2000)
# print(e.info())


