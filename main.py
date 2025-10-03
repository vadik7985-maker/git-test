from decimal import Decimal, getcontext, ROUND_HALF_UP
from fractions import Fraction
from datetime import datetime, timedelta, date

# 1.Простое преобразование
print('список квадратов чисел от 1 до 10:', [x**2 for x in range(1, 10)])

# 2.Фильтрация
print('список только четных чисел от 1 до 20:', [x for x in range(1, 20) if x % 2 == 0])

# 3.Работа со строками
words = ['python', 'Java', 'c++', 'Rust', 'go']
print([w.upper() for w in words if len(w) > 3])

# 4.Собственный итератор
class Countdown():
    def __init__(self, max_value):
        self.value = max_value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == 0:
            raise StopIteration
        
        carrent = self.value
        self.value -= 1
        return carrent

print('Итератор:')
for i in Countdown(5):
    print(i)

# 5. Собственый генератор
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print('\nГенератор:')
for num in fibonacci(10):
    print(num)

# 6.Точные вычисления
def deposit_calculator(principal, annual_rate, years):
    getcontext().prec = 25  # кол-во значащих цифр
    principal = Decimal(principal)
    annual_rate = Decimal(annual_rate)
    years = int(years)

    # годовая ставка
    monthly_rate = annual_rate / (Decimal('12') * Decimal('100'))

    # количество месяцев
    months = 12 * years

    # формула: S = P * (1 + r/12*100)^(12*t)
    total = principal * ((Decimal('1') + monthly_rate) ** months)

    # округление 2 знаков после запятой
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    profit = total - principal
    return total, profit

print('\nФинансовый калькулятор вкладов:')
#initial_sum = input("Введите начальную сумму вклада (в рублях с копейками): ")
#percent_rate = input("Введите годовую процентную ставку (%): ")
#term_years = input("Введите срок вклада (в годах): ")

#final_sum, earned_profit = deposit_calculator(initial_sum, percent_rate, term_years)
#print(f"Итоговая сумма вклада: {final_sum} руб.")
#print(f"Общая прибыль: {earned_profit} руб.")

# 7.Рациональные дроби
a = Fraction(3, 4)
b = Fraction(5, 6)
print('\nОсновные операции с рациональными дробями:')
print(a, b)
print('сложение:', a + b)
print('вычитание:', a - b)
print('умножение:', a * b)
print('деление:', a / b)

# 8.Текущая дата и время
now = datetime.now()
print("\nТекущая дата и время:", now)
print("Только текущая дата:", now.date())
print("Только текущее время:", now.time())

# 9.Разница дат
birthday = date(2005, 6, 28)
today = date.today()
days_passed = (today - birthday).days

# Дни до следующего дня рождения
next_birthday = date(today.year, birthday.month, birthday.day)
if next_birthday <= today:
    next_birthday += timedelta(days=365)  # Добавляем год в днях

days_to_birthday = (next_birthday - today).days

print('\n')
print(f"Дней с рождения: {days_passed}")
print(f"Дней до следущего дня рождения: {days_to_birthday}")