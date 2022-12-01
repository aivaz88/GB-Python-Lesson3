# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

x = int(input('Задайте число: '))
fib_list = [1, 0, 1]
for i in range(1, x):
    fib_num = fib_list[-1] + fib_list[-2]
    fib_list.append(fib_num)
    fib_list.insert(0, ((-1)**i)*fib_num)
print(fib_list)