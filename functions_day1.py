# def is_odd(x):
#     return x%2==0

# print(is_odd(7))
# print(is_odd(10))

# def count_odds(x):
#     """ Программа находит из списка нечетные числа
#         и суммирует их количество
#     """
#     count = 0
#     for i in x:
#         if is_odd(i)==False:
#             count += 1
#     return count
#
# print(f'Итого сумма нечетных чисел равна = {count_odds([1,2,3,4,5,6,7])}')
# print(help(count_odds))

# Массивы

# A=[0]*10
# top = 0
# x = int(input('Введите число:'))
# while x!=0 and top<10:
#     A[top]=x
#     top+=1
#     for k in range(9,-1,-1):
#         print(A[k])
#     x = int(input('Введите число:'))


# A = [0]*10
# top = 0
# S = 0
# x = int(input('Введите число:'))
# while x!=0 and top<10:
#     A[top]=x
#     top+=1
#     S=S+x
#     x=int(input('Введите число='))
#
# print('Cумма:', S)
# print("Введенные числа")
# for k in range(top):
#     print(A[k])

# """Сдвиг вправо"""
# A = [1,2,3,4,5]
# # N = int(input('Введите кол-во элементов:'))
# tmp = A[4]
# for k in range(3, -1, -1):
#     A[k+1] = A[k]
# A[0] = tmp
# print(A)
# print('-------')
# print(A[0])
#
#
# """Сдвиг влево"""
# A=[1,2,3,4,5]
# print(A)
# print('Сдвиг влево')
# tmp = A[0]
# for k in range(0,4,1):
#     A[k] = A[k+1]
# A[4] = tmp
# print(A)
#
#
# def cyclic_right_shift(A:list, N:int):
#     """Функция сдвиг вправо"""
#     tmp = A[N-1]
#     for k in range(N-2,-1,-1):
#         A[k+1] = A[k]
#     A[0] = tmp
#     return A
#
# c= cyclic_right_shift([1,2,3,4,5],5)
# print(c)
#
# def cyclic_left_shift(A:list):
#     N = len(A)
#     tmp = A[0]
#     for k in range(0, N-1, 1):
#         A[k] = A[k+1]
#     A[N-1] = tmp
#     return A
#
#
# c = cyclic_left_shift([1, 2, 3, 4, 5])
# print(c)

"""звездный прямоугольник размерами 5×7 (5 строк и 7 столбцов)."""


# for i in range(5):
#     print ('*' * 7)
# print()
#
#
# def draw_box():
#     for _ in range(5):
#         print('*'*7)
#
# draw_box()
# print()
# draw_box()


# def draw_box():
#     for x in range(2):
#         print('*' * 10)
#         if x < 1:
#             for x in range(12):
#                 print('*'+8*' '+'*')
#
#
# draw_box()

# def draw_triangle():
#     for x in range(1, 11):
#         print(x*'*')
#
#
# draw_triangle()

# def draw_triangle():
#     for x in range(1, 11):
#         print('#'*x if x%2==0 else '*'*x)
#
#
# draw_triangle()


# def draw_christmas_tree():
#     print((' '*12)+'*')
#     for i in range(1,12):
#         print(' '*(12-i) + (2*i+1)*'*')
#         if i == 10:
#             for j in range(3):
#                 print(' '*(i+2) + '*')
#
#
#
# draw_christmas_tree()
#
# def draw_box(height: int, width: int):
#     for i in range(height):
#         print(width * '*')
#
# m = 5
# n = 4
#
# draw_box(m, n)
# #
# #
# # def print_hello(txt: str, n: int):
# #     print(txt * n)
# #
# #
# # print_hello('Надеюсь, да ', 1)
#
#
# def test(x):
#     x = 100
#
# a = 3
# test(a)
# print(a)
#
#
#
# def print_sorted_hyphen(s):
#     s = s.split('-')
#     s.sort()
#     s = ('-').join(s)
#     print(s)
#
# s = input('Введите строку: ')
#
#
# print_sorted_hyphen(s)

# def draw_triangle(fill, base):
#     mid = base // 2
#     for i in range(1,mid+2):
#         print(fill * i)
#     for j in range(mid,0,-1):
#         print(fill * j)
#
#
# draw_triangle('*',5)


# def print_perm_time_call(msc_time):
#     msc_time = msc_time.split(':')
#     hours = int(msc_time[0])
#     hours= hours + 2
#     if hours>=24:
#         hours = hours - 24
#     hours = str(hours)
#     if len(hours) == 1:
#         hours = '0' + hours
#     msc_time[0] = str(hours)
#     msc_time = (':').join(msc_time)
#     print(f'Созвон будет в {msc_time}.')
#
# msc_time = input()
#
# print_perm_time_call(msc_time)

# s = '1:30'
# print(s)
# s = s.split(':')
# print(len(s[0]))
# if len(s[0]) == 1:
#     s[0] = '0' + s[0]
#     print(s[0])
#     print('----')
#     print(s)
#     s = (':').join(s)
# print(s)

# def sum_digits(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n = n // 10
#     return f'Cумма цифр равна = {sum}'
#
# n = int(input('Введи любое число и я просуммирую его цифры: '))
#
# print(sum_digits(n))


def display_message():
    """Написать тему главы"""
    print('Определение функции')

# display_message()
# help(display_message)


def favorite_book(title):
    """Выводит название книги"""
    print(f'One of my favorite books is {title}')

# title = input('Введи название книги:')

# favorite_book(title)

def describe_pet(pet_name, animal_type='cat'):
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('Hooxy')
# describe_pet('rex','cat')

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     # else:
#     #     full_name = first_name + ' ' + last_name
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def build_person(fisrt_name, last_name, age=''):
#     """Возвращает имя и фамилию"""
#     person = {'first':fisrt_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# mate = build_person('Bob','Kent', 28)
#
# print(mate)


# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# # Бесконечный цикл!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f'Hello, {formatted_name}! ')
#

# def city_country(city, country):
#     list = city + ', ' + country
#     return list.title()
#
# list1 = city_country('moscow','russia')
#
# print(list1)

# def make_album(musician_name, album_name, track_count=None):
#     album = {'musician_n':musician_name, 'album_n':album_name}
#     if track_count:
#         album['track_count'] = track_count
#     return album
#
# while True:
#     print('Введите название альбома и исполнителя')
#     mus_n = input('Имя исполнителя: ')
#     if mus_n == 'q':
#         break
#
#     alb_n = input('Название альбома: ')
#     track_c = int(input('Кол-во треков: '))
#
#     formatted_name = make_album(mus_n, alb_n, track_c)
#     print(formatted_name)
# print('ты сам вышел')

# result = make_album('Enrique Iglesias','Hero')
# print(result)
# result2= make_album('One republic', 'Stop and Stare', 15)
# print(result2)


# def greet_list(fruits):
#     """Возвращает список фруктов"""
#     for name in fruits:
#         print(f'Вот эти фрукт вкусный {name}')
#
# fruits = ['киви','груша', 'манго']
# result = greet_list(fruits)
# print(result)


def greet_list(fruits):
    """Возвращает список фруктов"""
    for name in fruits:
        msg = 'Этот фрукт вкусный:' + name.title()
        print(msg)

list_fruits = ['киви','груша', 'манго']
greet_list(list_fruits)
