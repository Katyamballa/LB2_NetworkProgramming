
# Обработка GET-запроса сервером

## Описание
В этом задании необходимо создать простой сервер, который обрабатывает HTTP GET-запрос. В ответ на запрос сервер возвращает строку `Hello World!`.

---

## Запуск сервера

1. Создайте файл `flask_get_server.py` со следующим содержимым:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def handle_get_request():
        return "Hello World!"

    if __name__ == '__main__':
        app.run(port=8000)
    ```

2. Запустите сервер:
    ```bash
    python3 flask_get_server.py
    ```

3. Перейдите в браузере по адресу:
    ```
    http://localhost:8000/
    ```

4. Вы увидите сообщение: `Hello World!`.


---

## Проверка работы
1. Откройте браузер.
2. Перейдите по адресу `http://localhost:8000/`.
3. Убедитесь, что сервер возвращает строку: `Hello World!`.

---

## Структура проекта
- `flask_get_server.py`: Сервер на Flask.
- `README.md`: Документация по выполнению задания.

---

## Автор
Kateryna
