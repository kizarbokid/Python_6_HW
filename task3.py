""" 
 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
"""

""" def to_sum_num(var):
    sum=0
    for num in var:
        if num in "123456789":
                sum += int(num)
    return sum """

""" n=input('Введите число: ')
print("Сумма цифр строки = ",to_sum_num(n))
 """
def to_sum_num(var):
    return sum(int(num) for num in var if num in "123456789")

n=input('Введите число: ')
print("Сумма цифр строки = ",to_sum_num(n))