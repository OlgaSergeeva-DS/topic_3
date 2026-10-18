import timeit
import random
import matplotlib.pyplot as plt


# ========== 1. АЛГОРИТМЫ СОРТИРОВКИ ==========
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ========== 2. ПРОВЕРКА НА 10 ЧИСЛАХ ==========
def test_10_random_numbers():
    """Генерирует 10 случайных чисел от 1 до 50 и проверяет сортировки."""
    arr = [random.randint(1, 50) for _ in range(10)]

    # Формируем текстовый отчет
    report = []
    report.append("=== Тест на 10 случайных числах (от 1 до 50) ===")
    report.append(f"Исходный список: {arr}")
    report.append(f"Пузырьком:       {bubble_sort(arr)}")
    report.append(f"Выбором:         {selection_sort(arr)}")
    report.append(f"Вставками:       {insertion_sort(arr)}\n")

    return report


# ========== 3. СРАВНЕНИЕ ВРЕМЕНИ И ГРАФИК ==========
def run_timing_and_plot():
    """Сравнение времени выполнения алгоритмов."""
    sizes = [100, 500, 1000, 2000, 3000]

    times_bubble = []
    times_selection = []
    times_insertion = []

    # Формируем заголовок для текстового отчета
    report = []
    report.append("=== Сравнение времени выполнения (в секундах) ===")
    report.append(f"{'Размер':>8} | {'Пузырёк':>10} | {'Выбор':>10} | {'Вставки':>10}")
    report.append("-" * 46)

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        t_bubble = timeit.timeit(lambda: bubble_sort(arr), number=1)
        t_selection = timeit.timeit(lambda: selection_sort(arr), number=1)
        t_insertion = timeit.timeit(lambda: insertion_sort(arr), number=1)

        times_bubble.append(t_bubble)
        times_selection.append(t_selection)
        times_insertion.append(t_insertion)

        # Добавляем строку в отчет
        report.append(f"{size:>8} | {t_bubble:>10.5f} | {t_selection:>10.5f} | {t_insertion:>10.5f}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_bubble, marker='o', label='Пузырьком (Bubble)')
    plt.plot(sizes, times_selection, marker='s', label='Выбором (Selection)')
    plt.plot(sizes, times_insertion, marker='^', label='Вставками (Insertion)')

    plt.title('Сравнение времени выполнения алгоритмов сортировки O(n²)')
    plt.xlabel('Размер списка (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot_sorting.png')
    plt.close()

    return report


# ========== 4. ГЛАВНЫЙ БЛОК ==========
if __name__ == "__main__":
    print("Запуск программы...")

    # Получаем текстовые результаты
    final_report = []
    final_report.extend(test_10_random_numbers())
    final_report.extend(run_timing_and_plot())

    # Записываем всё в текстовый файл
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(final_report))

    # Выводим в консоль
    print("\n".join(final_report))

    print("\n✅ Готово!")
    print("📄 Текстовый отчет сохранен в файл: results.txt")
    print("📈 График сохранен в файл: plot_sorting.png")