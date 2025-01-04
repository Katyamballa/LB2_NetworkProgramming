from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/content', methods=['GET'])
def handle_content_type():
    # Получение значения заголовка Content-Type
    content_type = request.headers.get('Content-Type')

    # Обработка в зависимости от Content-Type
    if content_type == 'application/json':
        response = {
            "message": "This is a JSON response",
            "status": "success"
        }
        return make_response(jsonify(response), 200)

    elif content_type == 'application/xml':
        xml_response = """
        <response>
            <message>This is an XML response</message>
            <status>success</status>
        </response>
        """
        return app.response_class(response=xml_response, status=200, mimetype='application/xml')

    else:
        return make_response("This is a plain text response", 200)

if __name__ == '__main__':
    app.run(port=8000)