# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

print("введите номер дня недели")
day_num = int(input())
if day_num == 6 or day_num == 7:
    print('выходной день')
else:print("рабочий день")
