# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых
# чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде,
# тот и выиграл спор.

number = int(input("Enter number: "))
maxNumber = number

while (number != 0):
     if (number > maxNumber):
      maxNumber = number
# maxNumber = number if number > maxNumber else maxNumber
number = int(input("Введите цифру: "))

print(f"Максимальный элемент: {maxNumber}")






# n = int(input())

# max_number = 1000 (Здесь лучще написать: max_number = n
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
#         print(max_number)
#
#         n = int(input())
#         max_number = -1
#         while n < 0: (ЦИКЛ НЕ ВЫЙДЕТ ИЗ МИНУС)
#             n = int(input())
#         if max_number < n:
#             n = max_number (max_number = n)
#         print(n)



