# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input("Введите числа через пробел:\n").split()))
print(numbers)
new_numbers = []

for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print(new_numbers)

