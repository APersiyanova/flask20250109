# Задача 5. Максимальное число
'''Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, 
разделённых слешем /. Endpoint должен вернуть текст «Максимальное переданное число {number}»'''

from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers = numbers.split('/')
    numbers = list(map(int, numbers))
    max_number = max(numbers)
    return f'Максимальное переданное число - <i>{str(max_number)}</i>'


if __name__ == '__main__':
    app.run(debug=True)