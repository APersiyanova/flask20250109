import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/test')  # Endpoint - это URL-адрес, чтобы приложению получить доступ к ресурсам или функциям веб-сервиса
def test_function(): # view function определяет, как веб-приложение реагирует на HTTP-запросы
    return 'It is my test page, generated in %s' % \
        datetime.datetime.now(datetime.UTC)

@app.route('/hello/world')
def greet():
    return 'Hello, world!'

@app.route('/endpoint/counter')
def myfunc():
    if not hasattr(myfunc, '_state'):  # инициализация значения
        myfunc._state = 0
    myfunc._state = myfunc._state + 1
    return f'Текущая страница запускалась {myfunc._state} раз (раза)'