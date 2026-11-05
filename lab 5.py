n = int(input("Введите число: "))

count = 0
total = 0
product = 1
reversed_num = 0

# Разбор числа по цифрам
while n > 0:
    digit = n % 10
    count += 1
    total += digit
    product *= digit
    reversed_num = reversed_num * 10 + digit
    n //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {product}")
print(f"Перевёрнутое число: {reversed_num}")