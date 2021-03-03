# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield. Полностью истощить генератор.
# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200.
#
# Усложнение(**):
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.

def iterator_with_yield(max_number):
    nums_sum = 0
    for num in range(1, max_number + 1, 2):
        if num ** 2 < 200:
            nums_sum += num
            yield num, nums_sum


gen1 = iterator_with_yield(110)
print(type(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))
