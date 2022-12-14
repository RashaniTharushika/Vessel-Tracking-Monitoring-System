import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from credit_balance import credit_balance
from registering import registering
from vfc import vfc

load_dotenv()

_FILE_PATH = os.getenv("FILE_PATH")
_PORT = os.getenv('PORT')
_HOST = os.getenv('HOST')

app = Flask(__name__)


@app.route("/balance")
def check_balance():
    balance = credit_balance(_FILE_PATH)

    response = {
        'balance': balance
    }
    return jsonify(response)


@app.route("/vfc")
def call_vfc():
    vfc(_FILE_PATH)

    return "Success"


# @app.route("/register")
# def register():
#     registering(_FILE_PATH)
#
#     return "Test2"


if __name__ == '__main__':
    app.run(debug=True, port=_PORT, host=_HOST)
