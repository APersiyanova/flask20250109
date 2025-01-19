# Задача 1. Список процессов
def get_summary_rss(file_relative_path):
    summary_memory = 0
    devider = 1024
    prefixes = {0: 'B', 1: 'kB', 2: 'mB', 3: 'gB', 4: 'tB'}
    key = 0
    with open(file_relative_path) as file: 
        headless_lines = file.readlines()[1:]
    for line in headless_lines:
        columns = line.split()
        summary_memory += int(columns[5])
    res = f'{summary_memory} B'
    # if summary_memory/devider >= 1:
    #     mega_memory = summary_memory/devider
    #     res = f'{mega_memory} Mb'
    # if mega_memory/devider >= 1:
    #     giga_memory = mega_memory/devider
    #     res = f'{mega_memory} Gb' 
    while summary_memory> devider:
        summary_memory /= devider
        key += 1
    res = f'{summary_memory} {prefixes[key]}'
    return res

file_relative_path = 'output_file.txt'
print(get_summary_rss(file_relative_path))