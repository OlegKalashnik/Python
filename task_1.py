# Написать генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200,
# без использования ключевого слова yield, полностью истощить генератор. Например:

def iterator_without_yield(max_number):
    return (num for num in range(1, max_number + 1, 2) if num ** 2 < 200)


gen1 = iterator_without_yield(110)
print(type(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))

print(next(gen1))
