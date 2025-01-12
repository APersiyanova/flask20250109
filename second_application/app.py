'''Разработайте веб-сервер, возвращающий страницы по следующим адресам:
/hello_world
Создайте страницу с текстом «Привет, мир!».
/cars
Создайте страницу, возвращающую список машин через запятую: Chevrolet, Renault, Ford, Lada.
/cats
Создайте страницу с названием случайной породы кошек из следующего списка: корниш-рекс, русская голубая, шотландская вислоухая, мейн-кун, манчкин.
/get_time/now
Создайте страницу с текстом «Точное время: {current_time}», где current_time — точное текущее время.
/get_time/future
Создайте страницу с текстом «Точное время через час будет {current_time_after_hour}», где current_time_after_hour — точное время через один час
/get_random_word
Создайте страницу со случайным словом из книги «Война и мир» Льва Толстого
https://docs.python.org/3/library/datetime.html#timedelta-objects
https://tproger.ru/translations/regular-expression-python
/counter
Создайте страницу с числом, показывающим, сколько раз открывалась данная страница.'''

from flask import Flask
from random import choice
import datetime

app = Flask(__name__)

@app.route('/hello_world')
def hello():
    return 'Привет, мир!'

@app.route('/cars')
def retcars():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    return str(cars)[1:-1].replace("'","")

@app.route('/cats')
def cat():
    cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
    return f'{choice(cats)}'

@app.route('/get_time/now')
def curtime():
    current_time = datetime.datetime.now()
    return 'Точное время: %s' % current_time

@app.route('/get_time/future')
def futtime():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'

@app.route('/get_random_word')
def ranworld():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt') 
    with open(BOOK_FILE) as book:
        contents = book.read()
    words = contents.splitlines()
    word = choice(words)
    return word

@app.route('/counter')
def counter():
    if not hasattr(counter, 'visits'):
        counter.visits = 0
    counter.visits += 1
    return f'{counter.visits}'