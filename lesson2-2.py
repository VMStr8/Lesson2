# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

new_list = []
for i in students:
    new_list.append(i['first_name'])
# print(new_dict)
for i2 in set(new_list):
    print(f'{i2}: {new_list.count(i2)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

new_list_2 = []
count = 0
for i in students:
    new_list_2.append(i['first_name'])
res = max(new_list_2, key=new_list_2.count)
print(f'Самое частое имя среди учеников: {res}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
]

names = []
for o in school_students:
    names.append([i2['first_name'] for i2 in o])
for q, w in enumerate(names):
    print(f'Самое частое имя в классе {q + 1}: {max(w, key=names.count)}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

a = []
for o in school:
    a = [i2['first_name'] for i2 in o['students']]
    count_boys = 0
    count_girls = 0
    for q in a:
        if is_male[q] == bool(True):
            count_boys += 1
        else:
            count_girls += 1
    print(f"В классе {o['class']} {count_girls} девочки и {count_boys} мальчика")

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Олег'}]}
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

a = []
max_boys = {}
max_girls = {}
for o in school:
    a = [i2['first_name'] for i2 in o['students']]  # создаем списки имен для последующей проверки пола
    count_boys = 0
    count_girls = 0
    for q in a:  # этот цикл записывает в каунтеры выше кол-во мальчиков и девочек
        if is_male[q] == bool(True):
            count_boys += 1
        else:
            count_girls += 1
    max_boys[o['class']] = count_boys  # создаем словарь, в котором будет ключ = класс, а значение кол-во мальчиков
    max_girls[o['class']] = count_girls  # создаем словарь, в котором будет ключ = класс, а значение кол-во девочек

# Проверяем вышеобъявленные словари по значениям ключей. Где больше мальчиков и девочек, то результат и выдаст
print(f"Больше всего мальчиков в классе {max(max_boys, key=max_boys.get)}")
print(f"Больше всего девочек в классе {max(max_girls, key=max_girls.get)}")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
