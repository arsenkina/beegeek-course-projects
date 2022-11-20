from random import choice


def ask(condition, text, alert):
    data = input(text + '\n')

    while not condition(data):
        print(alert)
        data = input(text + '\n')

    return data


def ask_digit(text):
    return int(ask(lambda data: data.isdigit(), text, 'Нужно ввести число!'))


def ask_yes_no(content):
    result = ask(lambda data: data.lower() in ['да', 'нет'],
                 f'Нужны ли в пароле {content}? Напиши "да" или "нет": ', 'Нужно вводить "да" или "нет"!')
    return result.lower() == 'да'


def build_password(length, chars):
    password = []
    for _ in range(length):
        password.append(choice(chars))
    return ''.join(password)


def main():
    number = ask_digit('Сколько нужно паролей? Укажи число: ')
    length = ask_digit('Введи длину пароля: ')

    chars = ''
    if ask_yes_no('цифры 0123456789'):
        chars += '0123456789'
    if ask_yes_no('заглавные буквы'):
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if ask_yes_no('строчные буквы'):
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if ask_yes_no('символы'):
        chars += '!#$%&*+-=?@^_'
    if not ask_yes_no('неоднозначные символы'):
        for c in chars:
            if c in 'il1Lo0O':
                del c

    for _ in range(number):
        print(build_password(length, chars))


if __name__ == '__main__':
    main()
