for i in range(1, 1000):
    if i % 2 != 0:
        cube = i ** 3
        digit_sum = 0

        while cube > 1:
            digit_sum += int(cube % 10)
            cube /= 10

        # сложнее, но тоже работает
        # operand = 1e8
        # while operand >= 1:
        #     digit_sum += cube // operand
        #     if digit_sum > 0:
        #         cube %= operand
        #     operand /= 10

        if digit_sum > 0 and digit_sum % 7 == 0:
            print(f'число: {i} sum: {digit_sum}')
