# Задача 2. Средний размер файла
# Input: ls -l | python3 get_mean_size.py   Output: 
import sys

if __name__ == '__main__':
    data = sys.stdin.readlines()[1:]
    total = 0
    count = 0
    for line in data:
        total += int(line.split()[4])
        count += 1
    mean = total / count
    print(mean)
