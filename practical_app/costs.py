# Задача 7. Учёт финансов
from flask import Flask
from datetime import datetime


app = Flask(__name__)
storage = {}

# /add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день
# Дата для /add/ передаётся в формате YYYYMMDD
@app.route('/add/<date>/<int:number>')
def day_costs(date, number):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    if not date_check(year, month, day):
        return 'Дату надо ввести в формате YYYYMMDD'
    storage.setdefault(year,{}).setdefault(month,0)
    storage[year][month] += number
    return storage

# /calculate/<int:year> — получение суммарных трат за указанный год
@app.route('/calculate/<int:year>')
def year_costs(year):
    try:
        total = 0
        for costs in storage[year].values():
            total += costs
        return str(total)
    except KeyError:
        return f'Похоже, в {year} году расходов не было'

# /calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц
@app.route('/calculate/<int:year>/<int:month>')
def month_costs(year, month):
    try:
        expenses = str(storage[year][month])
        return expenses
    except KeyError:
        return f'Похоже, в {month} месяце {year} года расходов не было'
    
def date_check(year, month, day):
    try:
        datetime(year, month, day)
        check_ok = True
    except ValueError:
        check_ok = False
    return check_ok


if __name__ == '__main__':
    app.run(debug=True)