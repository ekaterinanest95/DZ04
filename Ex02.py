# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input())
r = 2
g = n
numbers = []
for i in range(1, n):
    if(g % r == 0):
        numbers.append(r)
        g = g // r
    else:
        r += 1

print(numbers)