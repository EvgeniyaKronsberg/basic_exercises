# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('Задание 1: ')

#Пишем функцию для составления списка имен

def make_list_of_students(students_arg):
    list_of_students_arg=[]
    for student in students_arg:
        list_of_students_arg.append(student.get('first_name',None))
    return list_of_students_arg


#Пишем функцию для подсчета количества повторений имен
def students_amount_count(list_of_students_arg):
    dict_of_students_arg = {}
    for student in list_of_students_arg:
        if student in dict_of_students_arg:
            dict_of_students_arg[student] += 1
        else:
            dict_of_students_arg[student] = 1

    return dict_of_students_arg


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

list_of_students = make_list_of_students(students) # Составляем список имен
dict_of_students = students_amount_count(list_of_students) #Считаем количество повторений имен

for student in dict_of_students:
    print(f'{student}: {dict_of_students[student]}')

# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

print('Задание 2: ')

#Пишем функцию для подсчета самого повторяющегося имени
def most_common_name_count(dict_of_students_arg):
    sorted_dict_of_students={}
    sorted_dict_of_students = dict(sorted(dict_of_students_arg.items(), key = lambda x: x[1], reverse = True))
    most_common_name = list(sorted_dict_of_students.keys())[0]

    return most_common_name

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

list_of_students = make_list_of_students(students) # Составляем список имен
dict_of_students = students_amount_count(list_of_students) # Считаем количество повторений имен
most_common_name_count(dict_of_students) # Считаем самое повторяющееся имя

print(f'Самое частое имя среди учеников: {most_common_name_count(dict_of_students)}')

# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print('Задание 3:')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

class_number = 0

for item in school_students:
    class_number += 1
    list_of_students = make_list_of_students(item)
    dict_of_students = students_amount_count(list_of_students)
    most_common_name_count(dict_of_students)

    print(f'Самое частое имя в классе {class_number}: {most_common_name_count(dict_of_students)}')
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print('Задание 4:')

# Пишем функцию для подсчета мальчиков и девочек
def count_of_males_females(list_of_students):
    number_of_males = 0
    number_of_females = 0

    for name in list_of_students:
        if is_male[name] == False:
            number_of_females +=1
        else:
            number_of_males += 1

    return (number_of_males, number_of_females)


school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2с', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for item in school:
    class_name = item.get('class', None)
    list_of_students = make_list_of_students(item['students'])
    males, females = count_of_males_females(list_of_students) # Считаем количество мальчиков и девочек
    
    print(f'Класс {class_name}: девочки {females}, мальчики {males}')

# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print('Задание 5:')

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

max_number_of_males = 0
max_number_of_females = 0
class_with_max_number_of_males = None
class_with_max_number_of_females = None

for item in school:
    class_name = item.get('class', None)
    list_of_students = make_list_of_students(item['students'])
    males, females = count_of_males_females(list_of_students) # Считаем количество мальчиков и девочек

    if males >= max_number_of_males:
        max_number_of_males = males
        class_with_max_number_of_males = class_name

    
    if females >= max_number_of_females:
        max_number_of_females = females
        class_with_max_number_of_females = class_name

print(f'Больше всего девочек в классе {class_with_max_number_of_females}')
print(f'Больше всего мальчиков в классе {class_with_max_number_of_males}')


# ???

