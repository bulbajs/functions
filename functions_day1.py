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


# def greet_list(fruits):
#     """Возвращает список фруктов"""
#     for name in fruits:
#         msg = 'Этот фрукт вкусный:' + name.title()
#         print(msg)
#
# list_fruits = ['киви','груша', 'манго']
# greet_list(list_fruits)
#
#
# def printing_models(unprinted_designs):
#     completed_designs = []
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         completed_designs.append(current_design)
#     return completed_designs
#
#
# unprinted_designs = ['Y', 'E', 'N', 'O', 'H']
#
# def enter_models(completed_designs):
#     for n in completed_designs:
#         print(n)
#
#
# completed_designs = printing_models(unprinted_designs)
# enter_models(completed_designs)

# Как сде
# def show_names(names):
#     for n in names:
#         print(n+"\n"+"-----")
# names = ['Petya', 'Daniil', 'Alesha', 'Petrosyan']
# show_names(names)

# def greet_users(users):
#     for n in users:
#         print (f'Hello epta, {n}! ')
#
# users = ['Petya', 'Daniil', 'Alesha', 'Petrosyan']
#
# greet_users(users)

# def move_numbers(numbers, processed_numbers):
#     while numbers:
#         current_list = numbers.pop()
#         processed_numbers.append(current_list)
#
# numbers = [1,2,3,4,5]
# processed_numbers = []
#
# move_numbers(numbers,processed_numbers)
#
# print('numbers:', numbers)
# print('processed_numbers:', processed_numbers)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_list = unprinted_designs.pop()
#         completed_models.append(current_list)
#
# unprinted_designs = ['pop','append', 'time']
# completed_models = []
#
# def show_completed_models(completed_models):
#     for model in completed_models:
#         print(model)
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_list = unprinted_designs.pop()
#         completed_models.append(current_list)
#
# unprinted_designs = ['pop','append', 'time']
# completed_models = []
#
# def show_completed_models(completed_models):
#     for model in completed_models:
#         print(model)
#
# print_models(unprinted_designs, completed_models)
# print(unprinted_designs)
# show_completed_models(completed_models)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         # current_list = unprinted_designs.pop()
#         # completed_models.append(current_list)
#         completed_models.append(unprinted_designs.pop())
#
# unprinted_designs = ['pop','append', 'time']
# completed_models = []
#
# def show_completed_models(completed_models):
#     for model in completed_models:
#         print(model)
#
# print_models(unprinted_designs[:], completed_models)
# print(unprinted_designs)
# print(unprinted_designs[:])
# show_completed_models(completed_models)

#=====Task 7-8=====
# def make_great(magicians):
#     for i in range(len(magicians)):
#         magicians[i] = 'Great ' + magicians[i]
#     # print(magicians)
#
# magicians = ['Bob', 'Dilan', 'Garry']
#
#
# def show_magicians(magicians):
#     for n in magicians:
#         print(n)
#
# # print('---before---')
# # show_magicians(magicians)
# # make_great(magicians)
# # print('---after---')
# # show_magicians(magicians)


#=====Task 9=====
# Новый список без изменения исходного
# Создай список фокусников. Напиши функцию
# make_great(magicians), которая создаёт новый
# список с приставкой "Great " и возвращает его.
# Выведи исходный и новый списки.
# def make_greats(magicians):
#     new_list = []
#     for i in magicians:
#         i = 'Great ' + i
#         new_list.append(i)
#     return new_list
#
#
# magicians = ['Bob','Edward','Nikolya']
#
# print(magicians)
# great_magicians = make_greats(magicians)
# print(great_magicians)

# #=====Task 10=====
#
# def big_products(products, purchased):
#     while products:
#         cur = products.pop()
#         purchased.append(cur)
#     return purchased
#
#
# products = ['kiwi', 'strawberry', 'blackcurrunt']
# purchased = []
#
#
#
# def show_list(items):
#     for item in items:
#         print(item)
#
#
# def make_uppercase(items):
#     new_list = []
#     for i in items:
#         i = i.upper()
#         new_list.append(i)
#     return new_list
#
#
# list_products = big_products(products[:], purchased)
# print(list_products)
# show_list(purchased)
# new_l = make_uppercase(purchased)
# print(new_l)
#
# class Dog():
#
#     def __init__(self,name,age):
#         pass


# class Cat():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Имя нашего кота:{self.name}, а годиков ему: {self.age}')
#
#     def meow(self):
#         print(f'{self.name} говорит "Мяу"')
#
# cat1 = Cat('Hooxik', 2.5)
# cat2 = Cat('Gendalf', 99)
#
# cat1.info()
# cat1.meow()
# cat2.meow()
#
# # =====Task 4=====
# # Создай класс Car: brand, speed Метод drive()
# # Добавь метод: increase_speed(value) - увеличивает скорость
#
# class Car():
#     def __init__(self, brand, speed:int):
#         self.brand = brand
#         self.speed = speed
#
#     def drive(self):
#         print(f'{self.brand} is driving at {self.speed} km/h')
#
#     def increase_speed(self, value):
#         self.speed = self.speed + value
#         print(f'Нажимаем газ и скорость увеличивается до {self.speed} км/ч')
#
# car1 = Car('Tiguan', 180)
#
# car1.increase_speed(190)
# car1.drive()
#
#
# # =====Task 6=====
# class Student():
#     def __init__(self,name, grade):
#         self.name = name
#         self.grade = grade
#
#     def is_passed(self):
#         if self.grade >= 60:
#             print(f'{self.name} "Passed"')
#         else:
#             print(f'{self.name} "Failed"')
#
# stud1 = Student('Kent', 56)
# stud2 = Student('Pen', 75)
# stud3 = Student('Larry', 60)
#
# print(stud1.is_passed(), stud1.name)
# stud2.is_passed()
# stud3.is_passed()


# =====Task 7=====
class Student():
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade

    def is_passed(self):
        if self.grade >= 60:
            print(f'{self.name} "Passed"')
        else:
            print(f'{self.name} "Failed"')


# stud1 = Student('Kent', 56)
# stud2 = Student('Pen', 75)
# stud3 = Student('Larry', 60)
# students = [stud1,stud2, stud3]
# for s in students:
#     s.is_passed()


class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # self.amount = amount
        self.balance = self.balance + amount
        print(f'ПОПОЛНЕНИЕ. +{amount} РУБ. Ваш новый баланс: {self.balance}')

    def withdraw(self, amount):
        # self.amount = amount
        if amount > self.balance:
            print('Недостаточно средств')
        else:
            self.balance = self.balance - amount
            print(f'ПОКУПКА. -{amount} РУБ. Ваш новый баланс: {self.balance}')


    def sms(self):
        print(f'{self.owner}, Ваш баланс составляет {self.balance} РУБ.')


bank1 = BankAccount('Genry', 23500)

# bank1.sms()
# bank1.deposit(1000000)
# bank1.withdraw(60000)
# bank1.withdraw(1000000000)


class Employee():
    def __init__(self, name:str, salary:int):
        self.name = name
        self.salary = salary

    def info(self):
        print(f'{self.name} получает на своей работе скромные {self.salary}к')


    def apply_bonus(self, percent):
        self.salary = self.salary * ((percent + 100)/100)
        print(f'{self.name} получил прибавку к зарплате в качестве {percent}%. Его текущая зарплата стала {self.salary:2f}к')

empl1 = Employee('Петр', 60)


# empl1.info()
# empl1.apply_bonus(20)
# empl1.apply_bonus(10)


class Animal():
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'{self.name} - кличка животного')

    def make_sound(self):
        print(f'{self.name} издает какой-то звук')


class Dog(Animal):
    def __init__(self, name):
     super().__init__(name)

    def make_sound(self):
        print(f'Собака не просто издает звуки, а "лает"')


# anim1 = Animal('Billy')
# anim2 = Dog('Rex')
#
# anim1.info()
# anim1.make_sound()
# # anim1.Dog.make_sound()
# anim2.make_sound()
# anim2.info()

class Vehicle():
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f'Транспорт марки {self.brand}')

    def start(self):
        print(f'Транспорт марки {self.brand} начал движение')

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def drive(self):
        print(f'Автомобиль {self.brand} в пути')

Veh1 = Vehicle('BMW')
Car1 = Car('Tiguan')


# Veh1.start()
# Car1.start()
# Car1.drive()
# Car1.info()

# =====Task 2=====  Person → Employee Person: name Employee(Person): salary  используй super() добавь метод info()

class Person():
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'{self.name} кушает арбузик каждый день и не ходит на работу')

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
    def info(self):
        super().info()
        print(f'{self.name} ходит на работу и получают зп {self.salary}, нет времени кушать арбузики')


# pers1 = Person('Mike')
# pers2 = Employee('Steev',100)
# pers1.info()
# pers2.info()


# =====Task 3=====   Book → EBook  Book: title, author EBook(Book): file_size  выведи полную информацию
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f'Название книги: {self.title} , Писатель: {self.author}:')

class EBook(Book):
    def __init__(self,title, author, file_size):
        super().__init__(title,author)
        self.file_size = file_size

    def info(self):
        super().info()
        print(f'Размер книги: {self.file_size} Мб')

# book1 = Book('"Пышка"', 'Ги де Мопассан')
# book2 = EBook('"Пышка"', 'Ги де Мопассан',2)
#
# book1.info()
# print('--------')
# book2.info()


# =====Task 3=====  Car → ElectricCar в Car: метод fuel_type() → "Gasoline"
# в ElectricCar: переопредели → "Electric" вызвать метод и увидеть разницу

class Car():
    def