# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# a = int(input('Enter the number: '))
# list =[]
# for i in range(1,a+1):
#     if(a%i==0):
#       list.append(i)
# print(f'{a} = {list}')


# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

# import random
# list = [random.randint(0,15) for i in range (20)]
# print(list)
# new_list =[]
# [new_list.append(i) for i in list if i not in new_list ]
# print(new_list)


# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import pathlib

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())
if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())
if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())
print(f'{first}{second}{third}')



