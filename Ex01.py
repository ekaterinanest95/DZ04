# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

number = float(input())
d = list('0.001')
d.reverse()
h = d.index('.')
print(h)
print(round(number, h))
