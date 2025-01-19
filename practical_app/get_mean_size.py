# Задача 2. Средний размер файла
# Input: ls -l | python3 get_mean_size.py   Output: 
import sys

def get_mean_size(data):
    total = 0
    count = 0
    devider = 1024
    prefixes = {0: 'B', 1: 'kB', 2: 'mB', 3: 'gB', 4: 'tB'}
    key = 0
    for line in data:
        total += int(line.split()[4])
        count += 1
    mean = total / count
    while mean > devider:
        mean /= devider
        key += 1
    res = f'Средний размер файла: {mean} {prefixes[key]}'
    return res

if __name__ == '__main__':
    data = sys.stdin.readlines()[1:]
    if not data:
        print('Похоже, в папке нет файлов или к ней нет доступа.')
    else:
        mean_size = get_mean_size(data)
        print(mean_size)