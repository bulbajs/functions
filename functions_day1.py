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

def draw_box(height: int, width: int):
    for i in range(height):
        print(width * '*')

m = 5
n = 4

# draw_box(m, n)
#
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

def draw_triangle(fill, base):
    mid = base // 2
    for i in range(1,mid+2):
        print(fill * i)
    for j in range(mid,0,-1):
        print(fill * j)


draw_triangle('*',5)