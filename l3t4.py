# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите целое число: "))
binNum = ""
while (num > 0):
    if (num % 2 == 0):
        binNum = binNum + '0'
    else:
        binNum = binNum + '1'
    num = num // 2
for i in reversed(binNum):
    print(i, end='')