from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/currency', methods=['GET'])
def get_currency_rate():
    # Получаем параметры из URL
    today = request.args.get('today')
    key = request.args.get('key')

    # Статический ответ с курсом валют
    if today and key:
        response = {
            "USD": "41.5",
            "EUR": "44.0",
            "message": f"Параметры запроса: today={today}, key={key}"
        }
        # Возвращаем JSON с правильной кодировкой UTF-8
        return make_response(jsonify(response), 200)
    else:
        error_response = {
            "error": "Missing parameters",
            "message": "Ensure 'today' and 'key' are present in the URL."
        }
        return make_response(jsonify(error_response), 400)

if __name__ == '__main__':
    app.run(port=8000)