n = int(input("Введите число: "))
original = n
reversed_num = 0

temp = n
# Переворот числа
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

# Сравнение с оригиналом
if original == reversed_num:
    print(f"{original} — палиндром")
else:
    print(f"{original} — не палиндром")