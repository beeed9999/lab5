"""Бинарный поиск первого вхождения элемента в отсортированном массиве."""


def binary_search(numbers: list[int], target: int) -> int:
    """Вернуть индекс первого target или -1, если элемента нет."""
    left, right = 0, len(numbers) - 1
    found_index = -1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            found_index = middle
            right = middle - 1  # продолжаем поиск слева, чтобы найти первое вхождение
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return found_index


def read_sorted_numbers() -> list[int]:
    while True:
        try:
            numbers = [int(item) for item in input("Введите отсортированные числа через пробел: ").split()]
        except ValueError:
            print("Разрешены только целые числа.")
            continue
        if not numbers:
            print("Введите хотя бы одно число.")
        elif numbers != sorted(numbers):
            print("Массив должен быть отсортирован по возрастанию.")
        else:
            return numbers


def main() -> None:
    numbers = read_sorted_numbers()
    while True:
        try:
            target = int(input("Какое число найти: "))
            break
        except ValueError:
            print("Введите целое число.")

    index = binary_search(numbers, target)
    if index == -1:
        print("Элемент не найден.")
    else:
        print(f"Элемент найден: индекс {index}, позиция {index + 1}.")


if __name__ == "__main__":
    main()