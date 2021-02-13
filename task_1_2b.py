my_list = [x ** 3 for x in range(1, 1000) if x % 2 != 0]

for i in my_list:
    digit_sum = 0
    n = i
    while n > 1:
        digit_sum += int(n % 10)
        n /= 10
    if digit_sum > 0 and digit_sum % 7 == 0:
        print(f'число: {i} sum: {digit_sum}')

    digit_sum = 0
    n = i + 17
    while n > 1:
        digit_sum += int(n % 10)
        n /= 10
    if digit_sum > 0 and digit_sum % 7 == 0:
        print(f'число: {i} sum: {digit_sum}')
#/------------------------------------------/
# можно и просто ещё раз прогнать
# for i in my_list:
#     digit_sum = 0
#     n = i + 17
#     while n > 1:
#         digit_sum += int(n % 10)
#         n /= 10
#     if digit_sum > 0 and digit_sum % 7 == 0:
#         print(f'число: {i} sum: {digit_sum}')
