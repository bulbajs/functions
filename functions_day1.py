def is_odd(x):
    return x%2==0

# print(is_odd(7))
# print(is_odd(10))

def count_odds(x):
    """ Программа находит из списка нечетные числа
        и суммирует их количество
    """
    count = 0
    for i in x:
        if is_odd(i)==False:
            count += 1
    return count

print(f'Итого сумма нечетных чисел равна = {count_odds([1,2,3,4,5,6,7])}')
print(help(count_odds))