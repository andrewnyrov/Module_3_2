def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')

# Вызовы функции с разным количеством аргументов
print_params()  # a: 1, b: строка, c: True
print_params(10)  # a: 10, b: строка, c: True
print_params(b=25)  # a: 1, b: 25, c: True
print_params(c=[1, 2, 3])  # a: 1, b: строка, c: [1, 2, 3]

# Распаковка параметров
values_list = [54.32, 'Строка', False]
values_dict = {'a': 100, 'b': 'Текст', 'c': None}

print_params(*values_list)  # a: 54.32, b: Строка, c: False
print_params(**values_dict)  # a: 100, b: Текст, c: None

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)  # a: 54.32, b: Строка, c: 42