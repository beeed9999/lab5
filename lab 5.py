n = 5

# Прямоугольник
print("Прямоугольник:")
for i in range(n):
    print("*" * n)

# Треугольник
print("\nТреугольник:")
for i in range(1, n + 1):
    print("*" * i)

# Ёлочка
print("\nЁлочка:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Ромб
print("\nРомб:")
# Верхняя часть
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Нижняя часть
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))