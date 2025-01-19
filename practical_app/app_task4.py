# Задача 4. Хорошего дня!
# Реализуйте endpoint /hello-world/<имя>, который возвращает строку 
# «Привет, <имя>. Хорошей пятницы!». 

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/hello-world/<user_name>')
def welcome(user_name):
    weekday_num = datetime.today().weekday()
    weekdays_tuple = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    weekday = weekdays_tuple[weekday_num]
    return f'Привет, <b>{user_name}</b>! Have a good {weekday}! You\'re the best programmer in the world!'

if __name__ == '__main__':
    app.run(debug = True)