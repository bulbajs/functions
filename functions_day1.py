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

#Массивы

# A=[0]*10
# top = 0
# x = int(input('Введите число:'))
# while x!=0 and top<10:
#     A[top]=x
#     top+=1
#     for k in range(9,-1,-1):
#         print(A[k])
#     x = int(input('Введите число:'))


A = [0]*10
top = 0
S = 0
x = int(input('Введите число:'))
while x!=0 and top<10:
    A[top]=x
    top+=1
    S=S+x
    x=int(input('Введите число='))

print('Cумма:', S)
print("Введенные числа")
for k in range(top):
    print(A[k])
