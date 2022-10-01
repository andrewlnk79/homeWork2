chislo1 = float(input('введите число1='))
chislo2 = float(input('введите число2='))
print('ввелите операцию'+"mod —  взятие остатка от деления" +"pow — возведение в степень" +"div — целочисленное деление" )
operation = input()
if chislo2 == 0 and (operation == '/' or operation == 'mod' or operation == 'div'):
    print("Деление на 0!")
elif operation == '+':
    print(chislo1 + chislo2)
elif operation == '-':
    print(chislo1 - chislo2)
elif operation == '/':
    print(chislo1 / chislo2)
elif operation == '*':
    print(chislo1 * chislo2)
elif operation == 'mod':
    print(chislo1 % chislo2)
elif operation == 'pow':
    print(chislo1 ** chislo2)
elif operation == 'div':
    print(chislo1 // chislo2)