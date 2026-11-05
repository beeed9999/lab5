n = int(input("Введите число: "))
original = n
factors = []

divisor = 2
# Поиск множителей
while divisor * divisor <= n:
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1

# Добавление оставшегося простого числа
if n > 1:
    factors.append(n)

print(f"{original} = {' x '.join(map(str, factors))}")