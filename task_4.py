# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}}
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus_adv(*args):
    workers = {}
    for name in sorted(args):
        workers.setdefault(name.split()[1][0], {}).setdefault(name[0], []).append(name)
    return dict(sorted(workers.items()))


workers_dict = thesaurus_adv(
    "Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
    "Василий Суриков", "Элла Кодорова", "Юлия Чижова", "Николай Ялехеев", "Роман Уваров", "Жанна Вавельева",
    "Максим Туриков", "Олия Чижова", "Юлия Кижова", "Виктория Ужова", "Юрий Антонов"
)
for key, val in workers_dict.items():
    print(key, val)
