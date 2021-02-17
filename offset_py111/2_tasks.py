# Считалочка
# Дано N человек, считалка из K слогов.
# Считалка начинает считать с первого человека.
# Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
# Игра происходит до тех пор, пока не останется последний человек.
# Для данных N и К дать номер последнего оставшегося человека.

def compute_last_number(N: int, k: int) -> int:
    numbers = list(range(1, N + 1))
    i = 0
    j = 0
    while len(numbers) > 1:
        i += 1
        if j == len(numbers):
            j = 0
        if i % k == 0:
            numbers.pop(j)
        else:
            j += 1
    return numbers[0]


if __name__=='__main__':
    N = 8
    k = 4
    print(compute_last_number(N, k))
