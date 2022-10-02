n = int(input('введите число:'))
operation = 1
for i in range(1, n+1):
    operation *= i
    print(operation, end=" ")