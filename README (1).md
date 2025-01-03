
# Лабораторная работа: Работа с HTTP-протоколом и публичными API

## Описание
В этом задании необходимо установить Python веб-фреймворк (Flask или Bottle) и запустить простой веб-сервер на порту `8000`. Сервер должен возвращать приветственное сообщение при обращении к корневому URL (`/`).

---

## Установка и настройка

### 1. Убедитесь, что Python установлен
На MacBook убедитесь, что Python 3 установлен. Если его нет, установите его через [Homebrew](https://brew.sh/):
```bash
brew install python
```

Проверьте версию Python:
```bash
python3 --version
```

---

### 2. Создайте виртуальную среду (рекомендуется)
Виртуальная среда позволяет изолировать зависимости проекта:

1. Создайте виртуальную среду:
   ```bash
   python3 -m venv venv
   ```

2. Активируйте её:
   ```bash
   source venv/bin/activate
   ```

3. Убедитесь, что `pip` работает:
   ```bash
   pip --version
   ```

---

### 3. Установите Flask или Bottle

#### Flask:
Установите Flask с помощью команды:
```bash
pip install Flask
```

#### Bottle:
Установите Bottle с помощью команды:
```bash
pip install bottle
```

---

## Запуск сервера

### Для Flask
Создайте файл `flask_server.py` с таким содержимым:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! Flask server is running."

if __name__ == '__main__':
    app.run(port=8000)
```

Запустите сервер:
```bash
python3 flask_server.py
```

### Для Bottle
Создайте файл `bottle_server.py` с таким содержимым:
```python
from bottle import route, run

@route('/')
def hello():
    return "Hello, World! Bottle server is running."

if __name__ == '__main__':
    run(host='localhost', port=8000)
```

Запустите сервер:
```bash
python3 bottle_server.py
```

---

## Проверка работы сервера

1. Откройте браузер.
2. Перейдите по адресу:
   ```
   http://localhost:8000/
   ```
3. Вы должны увидеть сообщение:
   - Для Flask: `Hello, World! Flask server is running.`
   - Для Bottle: `Hello, World! Bottle server is running.`

---

## Завершение работы
Если вы использовали виртуальную среду, деактивируйте её после работы:
```bash
deactivate
```

---

## Структура проекта
- `flask_server.py`: Сервер на Flask.
- `bottle_server.py`: Сервер на Bottle.
- `README.md`: Инструкция по установке и запуску.

---

## Автор
Kateryna
