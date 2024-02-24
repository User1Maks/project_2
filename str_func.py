def str_funcs(word):
    """Возвращает каждое слово в верхнем регистре"""
    # word = input('Введите текст: ')  # пропишем аргумент функции
    return word.upper()


def str_funcs_2():
    """Возвращает каждую букву слова в верхнем регистре """
    user_input = input('Введите текст: ')
    return user_input.title()


print(str_funcs(f"{input('Введите текст: ')}"))
# print(str_funcs_2())
