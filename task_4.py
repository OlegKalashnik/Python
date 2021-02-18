# Создать список, содержащий цены на товары (10 – 20 товаров), например:
# [57.8, 46.51, 97, ...]
# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# - Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# - Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
prices = [65.67, 567, 7.3, 67.5, 45.78, 124.80, 46, 878.89, 45.89, 3.78, 12.98, 56]
for i, price in enumerate(prices, 1):
    if '.' in str(price):
        cents = str(str(price)[str(price).find('.') + 1:])
        if len(cents) == 1:
            cents += '0'
    else:
        cents = 0
    if i == len(prices):
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)))
    else:
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)), end=', ')

# - Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
prices = [65.67, 567, 7.3, 67.5, 45.78, 124.80, 46, 878.89, 45.89, 3.78, 12.98, 56]
print(prices)
for i, price in enumerate(sorted(prices), 1):
    if '.' in str(price):
        cents = str(str(price)[str(price).find('.') + 1:])
        if len(cents) == 1:
            cents += '0'
    else:
        cents = 0
    if i == len(prices):
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)))
    else:
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)), end=', ')
print(prices)

# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.
prices = [65.67, 567, 7.3, 67.5, 45.78, 124.80, 46, 878.89, 45.89, 3.78, 12.98, 56]
sr_prices = sorted(prices, reverse=True)
print(sr_prices)

# - Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
for i, price in enumerate(sorted(prices)[-5:], 1):
    if '.' in str(price):
        cents = str(str(price)[str(price).find('.') + 1:])
        if len(cents) == 1:
            cents += '0'
    else:
        cents = 0
    if i == 5:
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)))
    else:
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)), end=', ')

for i, price in enumerate(sr_prices[4:: -1], 1):
    if '.' in str(price):
        cents = str(str(price)[str(price).find('.') + 1:])
        if len(cents) == 1:
            cents += '0'
    else:
        cents = 0
    if i == 5:
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)))
    else:
        print('«{} руб {:02d} коп»'.format(int(price), int(cents)), end=', ')
