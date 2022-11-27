# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# data = open('file04', 'r+') # код для удаления данных из файла
# data.seek(0)
# data.truncate()
# data.close()

# exit()
import random
from numpy.polynomial import Polynomial as P

p = P([2, 1])

print(p)

k = random.randint(1, 3)
print(k)
poly = p ** k
print(poly)

data = open('file04', 'w')
data.write(str(poly))
data.close()

data = open('file04', 'r')
print(*data)
data.close()


