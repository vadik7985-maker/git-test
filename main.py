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
    
for i in Countdown(5):
    print(i)
    