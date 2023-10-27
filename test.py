# list1 = [3, 2, 8, 5, 10, 6]
# max_number = max(list1)
# print(max_number)
import list1 as list1

# def N(x):
#     return x + 1
#
# print(N(5))
#
# plus = lambda x: x + 1
# # print(plus(2))
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = list(map(lambda x: x + 1, list1))
# print(list2)


# def is_palindrome(string):
#     pointer1 = 0
#     pointer2 = len(string) - 1
#     while pointer2 - pointer1 > 0:
#         if string[pointer1] != string[pointer2]:
#             return False
#         pointer1 += 1
#         pointer2 -= 1
#     return True

# Задача №33:
# Задана натуральная степень k. Сформировать случайным образом список \
#     коэффициентов (значения от 0 до 100) многочлена и записать в файл \
#         многочлен степени k.
# Пример:
#     k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.
# '''

import random


def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))


