'''
Создайте класс «Дробь». Необходимо хранить в полях класса: числитель и знаменатель. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. Также создайте методы класса для выполнения арифметических операций: сложение, вычитание, умножение, деление.
Добавьте целую часть в дробь, возможность её сокращения. 
'''
import math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        # Инициализация дроби, проверка знаменателя на ноль
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    # Методы для ввода данных
    def set_numerator(self, numerator):
        self.numerator = numerator
        self.simplify()

    def set_denominator(self, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем")
        self.denominator = denominator
        self.simplify()

    # Методы для получения данных
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    # Метод для вывода данных
    def display(self):
        whole, num, denom = self.to_mixed()
        if whole != 0:
            print(f"{whole} {num}/{denom}")
        else:
            print(f"{num}/{denom}")

    # Метод для упрощения дроби
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:  # Обеспечить положительность знаменателя
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    # Преобразование в смешанную дробь
    def to_mixed(self):
        whole = self.numerator // self.denominator
        numerator = self.numerator % self.denominator
        return whole, abs(numerator), abs(self.denominator)

    # Арифметические операции
    def add(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return  Fraction(numerator, denominator)

    def subtract(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def multiply(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Деление на ноль")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

# Пример использования класса
print("Дробь 1")
fraction1 = Fraction(int(input("Введите числитель: ")), int(input("Введите знаменатель: ")))
print("\nДробь 2")
fraction2 = Fraction(int(input("Введите числитель: ")), int(input("Введите знаменатель: ")))

# Выполнение операций
sum_fraction = fraction1.add(fraction2)
sub_fraction = fraction1.subtract(fraction2)
mul_fraction = fraction1.multiply(fraction2)
div_fraction = fraction1.divide(fraction2)

# Вывод результатов
print (f"Сумма:{sum_fraction.display()}")
print (f"Разность:{sub_fraction.display()}")
print (f"Произведение:{mul_fraction.display()}")
print (f"Частное:{div_fraction.display()}")

