import os

from flask import Flask, request, abort, jsonify
from marshmallow import ValidationError

from config import LOG_DIR_NAME
from model import BatchRequestSchema
from utils import perform_action, read_file

app = Flask(__name__)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
#

@app.route("/perform_query", methods=["POST"])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    data = request.json
    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as e:
        abort(400, e)

    filename = LOG_DIR_NAME + validated_data['filename']
    if not os.path.isfile(filename):
        abort(400, "no such file")

    result = read_file(filename)
    for query in validated_data['queries']:
        try:
            result = perform_action(
                cmd=query['cmd'],
                value=query['value'],
                data=result
            )
        except Exception as err:
            abort(400, err)

    return jsonify(list(result))


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)