from random import randint

MIN_NUM = 1
MAX_NUM = 100


def main():
    num = randint(MIN_NUM, MAX_NUM)
    print('Рыба карась – игра началась!')

    while True:
        predict = int(input())

        if predict > num:
            print('Слишком много, попробуйте еще раз')

        elif predict < num:
            print('Слишком мало, попробуйте еще раз')

        else:
            print('Вы угадали, поздравляем!')
            break


if __name__ == '__main__':
    main()
