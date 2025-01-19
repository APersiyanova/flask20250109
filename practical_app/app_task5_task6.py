# Задача 5. Максимальное число
'''Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, 
разделённых слешем /. Endpoint должен вернуть текст «Максимальное переданное число {number}»'''

from flask import Flask
import os

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers = numbers.split('/')
    numbers = list(map(int, numbers))
    max_number = max(numbers)
    return f'Максимальное переданное число - <i>{str(max_number)}</i>'

# Задача 6. Превью файла
'''Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) 
и RELATIVE_PATH — и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути'''

@app.route('/<int:size>/<path:relative_path>')
def show_content(size, relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_dir,relative_path)
    with open(relative_path) as file:
        # result_text = file.read(size)
        result_text = file.read()[:size]
        result_size = len(result_text)
        return f'Из файла <i>{abs_path}</i> прочитано {result_size} символов:<br><br><b>{result_text}</b>'


if __name__ == '__main__':
    app.run(debug=True)