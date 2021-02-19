# Сорт
# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом

# Для решения данной задачи цеселообразно
# использовать сортировку подсчетом, так как диапозон возможных значений мал
# по сравнению с сортируемым множеством.
from collections import OrderedDict
import random

values = list(range(13, 26))
sequence = [random.choice(values) for i in range(int(1e6))]
zeros = [0 for i in range(len(values))]
dct = OrderedDict(zip(values, zeros))
for e in sequence:
    dct[e] += 1

result = []
for key in dct:
    result.extend([key] * dct[key])

print(result[::int(5e4)])
