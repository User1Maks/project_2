def str_funcs():
    """Возвращает каждое слово в верхнем регистре"""
    user_input = input('Введите текст: ')
    return user_input.upper()


def str_funcs_2():
    """Возвращает каждую букву слова в верхнем регистре """
    user_input = input('Введите текст: ')
    return user_input.title()


print(str_funcs())
print(str_funcs_2())
