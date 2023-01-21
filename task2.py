"""    Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    Пример:
    [2, 3, 4, 5, 6] => [12, 15, 16];
    [2, 3, 5, 6] => [12, 15]
 
from math import ceil
def mult_pair(var:str):
    a=[int(s) for s in s.split()]
    b=[]
    for i in range(ceil(len(a)/2)):
        b.append(a[i]*a[-i-1])
    return b

s=input('Введи несколько чисел, разделяя пробелом: ')
print(mult_pair(s)) """

from math import ceil

def mult_pair(var:str):
    a = [int(s) for s in var.split()]
    b = [a[i] * a[-i-1] for i in range(ceil(len(a)/2))]
    return b

s = input('Введи несколько чисел, разделяя пробелом: ')
print(mult_pair(s))