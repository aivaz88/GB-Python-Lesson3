# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
new_list = []
if (len(list) % 2 == 0): 
    x_range = int(len(list) / 2) 
else: 
    x_range = int(len(list) / 2) + 1
for i in range(x_range):
    new_list.append(list[i] * list[-i-1])
print(new_list)