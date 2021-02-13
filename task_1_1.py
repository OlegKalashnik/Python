duration = int(input('Введите время в секундах: '))

days = duration // 86400
hours = (duration - days * 86400) // 3600
minutes = (duration - days * 86400 - hours * 3600) // 60
seconds = duration % 60

if days > 0:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
elif hours > 0:
    print(f'{hours} час {minutes} мин {seconds} сек')
elif minutes > 0:
    print(f'{minutes} мин {seconds} сек')
else:
    print(f'{seconds} сек')
