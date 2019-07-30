from flask import Flask, request
from config import parse, ingest
from db import get_conn
from dao import findAll, findOneOrNone
from logger import get_logger
from json import dumps
import traceback

import os

app = Flask(__name__)


@app.route('/people', methods=['POST', 'GET'])
def show_people():
    """
    Show people is meant to serve as an auto-complete route
    :return:
    """
    conn = get_conn(parse('config.yml', ingest))
    logger = get_logger

    try:

        search = request.args.get('q', '')

        if search is '':
            return dumps(findAll(conn))
        else:
            return dumps(findOneOrNone(conn, search))

    except Exception as error:
        logger.debug(error)
        logger.debug(traceback.format_exc())


if __name__ == '__main__':
    if os.getenv('ENVIRONMENT', 'production') == "production":
        port = 5000
        debug = False
    else:
        port = 5001
        debug = True

    app.run(host='0.0.0.0', port=port, debug=debug)
