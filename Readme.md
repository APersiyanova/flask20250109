python3 -m venv venv
source ./venv/bin/activate 
pip install requests
pip freeze
pip freeze | grep -i flask
pwd

Запуск приложения: python3 -m flask run --port=5555
Перейдите в браузере по адресу: http://127.0.0.1:5555/Endpoint

python3 -m flask run --port=8080
http://127.0.0.1:8080/Endpoint

mytest.py
# https://ru.stackoverflow.com/questions/358/Глобальные-переменные-в-python-сохранить-локальную-переменную-от-вызова-к-вызов

порты с номерами ниже 1024 доступны только для суперпользователя системы
sudo 
# https://www.opennet.ru/man.shtml?topic=sudo&category=8&russian=0

https://developer.mozilla.org/en-US/docs/Web/HTTP/Status




