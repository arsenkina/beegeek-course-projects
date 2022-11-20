ENG_LOWER_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ENG_UPPER_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RUS_LOWER_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RUS_UPPER_ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encode(lwr_alph, upr_alph, step, text):
    result = ''
    for c in text:
        if not c.isalpha():
            result += c
            continue

        if c.isupper():
            alph = upr_alph
        else:
            alph = lwr_alph

        new_i = (alph.index(c) + step) % len(alph)
        new_c = alph[new_i]
        result += new_c

    return result


def decode(lwr_alph, upr_alph, step, text):
    return encode(lwr_alph, upr_alph, -step, text)


def main():
    mode = input('Введите "шифрование" или "дешифрование"\n')
    language = input('Введите язык алфавита: "русский" или "английский"\n')
    step = int(input('Введите шаг сдвига\n'))
    text = input('Введите текст\n')

    if mode == 'шифрование':
        job = encode
    else:
        job = decode

    if language == 'русский':
        print(job(RUS_LOWER_ALPHABET, RUS_UPPER_ALPHABET, step, text))
    else:
        print(job(ENG_LOWER_ALPHABET, ENG_UPPER_ALPHABET, step, text))


if __name__ == '__main__':
    main()
