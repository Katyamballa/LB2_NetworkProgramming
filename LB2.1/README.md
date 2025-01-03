
Работа с HTTP-протоколом и публичными API

Описание
В этом задании необходимо установить Python веб-фреймворк (Flask или Bottle) и запустить простой веб-сервер на порту `8000`. Сервер должен возвращать приветственное сообщение при обращении к корневому URL (`/`).

---

Установка и настройка

1. Убедитесь, что Python установлен
На MacBook убедитесь, что Python 3 установлен. Если его нет, установите его через [Homebrew](https://brew.sh/):
brew install python

Проверьте версию Python:
python3 --version

---

2. Создайте виртуальную среду (рекомендуется)
Виртуальная среда позволяет изолировать зависимости проекта:

1. Создайте виртуальную среду:
   python3 -m venv venv


2. Активируйте её:

   source venv/bin/activate
   

---

Установите Flask

Flask:
Установите Flask с помощью команды:

pip install Flask

---

Запуск сервера

Для Flask
Создайте файл `flask_server.py` с таким содержимым:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! Flask server is running."

if __name__ == '__main__':
    app.run(port=8000)


Запустите сервер:

python3 flask_server.py


---

## Проверка работы сервера

1. Откройте браузер.
2. Перейдите по адресу:
   ```
   http://localhost:8000/
   ```
3. Вы должны увидеть сообщение:
   - Для Flask: `Hello, World! Flask server is running.`


---

## Автор
Kateryna
