""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
    Пример:
    [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def odd_symb_sum(var: str):
    a = [int(s) for s in s.split()]
    sum = 0
    for i in range(len(a)):
        if i % 2 == 1:
            sum += a[i]
    return sum

s = input('Введи несколько чисел, разделяя пробелом: ')
print(odd_symb_sum(s))
 """

def odd_symb_sum(var: str):
    result = sum(int(s) for i, s in enumerate(var.split()) if i % 2 != 0)
    return result

s = input('Введи несколько чисел, разделяя пробелом: ')
print(odd_symb_sum(s))