import math

# Заголовок таблицы
print(f"{'x':>8} {'sin(x)':>10}")
print("-" * 20)

# Расчет значений от 0 до Pi
for i in range(11):
    x = i * math.pi / 10
    y = math.sin(x)
    print(f"{x:8.4f} {y:10.4f}")