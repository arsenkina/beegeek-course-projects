from random import randint

MIN_NUM = 1


def is_number(s):
    return s.isdigit()


def get_number_with_bounds(max_num):
    def helper(s):
        return is_number(s) and MIN_NUM <= int(s) <= max_num

    return helper


def get_valid(predicate, text):
    data = input(text + '\n')

    while not predicate(data):
        data = input(text + '\n')

    return data


def main():
    max_num = int(get_valid(
        is_number,
        'Введите верхнюю границу для случайного выбора числа'))

    num = randint(MIN_NUM, max_num)
    attempts = 0

    while True:  # game cycle
        print('Рыба карась – игра началась!')

        while True:  # number choose cycle
            predict = int(get_valid(
                get_number_with_bounds(max_num),
                f'Пожалуйста, введите число от {MIN_NUM} до {max_num}'))

            if predict > num:
                print('Слишком много, попробуйте еще раз')
                attempts += 1

            elif predict < num:
                print('Слишком мало, попробуйте еще раз')
                attempts += 1

            else:
                break

        print(f'Вы угадали, поздравляем! Вам потребовалось {attempts} попыток')
        attempts = 0

        print('Хотите сыграть ещё раз?')
        answer = get_valid(lambda ans: ans.lower() == 'да' or ans.lower() == 'нет',
                           'Введите \'Да\' или \'Нет\'').lower()

        if answer == 'да':
            continue
        else:
            break


if __name__ == '__main__':
    main()
