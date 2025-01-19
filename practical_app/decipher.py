# Задача 3. Дешифратор
import sys


def decrypt(text):
    letters = []
    dots = 0
    for symbol in text:
        if symbol != '.':
            letters.append(symbol)
        else:
            dots += 1
        if dots == 2 and letters:
            letters.pop()
            dots = 0
    return ''.join(letters)


# res = decrypt('Abra..-kid..ubrqz..')
# print(res)
if __name__ == '__main__':
    res = decrypt(sys.stdin.read())
    print(res)