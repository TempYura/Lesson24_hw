import os

from flask import Flask, request, abort, jsonify, Response
from marshmallow import ValidationError
from typing import Generator, Optional, Any, Union, Mapping, Iterable

from config import LOG_DIR_NAME
from model import BatchRequestSchema
from utils import perform_action, read_file


app: Flask = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query() -> Response:
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    data: dict | None = request.json
    try:
        validated_data: dict | None = BatchRequestSchema().load(data)
    except ValidationError as e:
        abort(400, e)

    filename: str = LOG_DIR_NAME + validated_data['filename']
    if not os.path.isfile(filename):
        abort(400, "no such file")

    result: Generator = read_file(filename)
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