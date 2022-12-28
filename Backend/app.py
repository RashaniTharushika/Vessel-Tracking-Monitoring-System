import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

from credit_balance import credit_balance
from registering import registering
from vfc import vfc
from single_vessel_positioning import single_vessel_position
from helper import input_form_data

load_dotenv()

_FILE_PATH = os.getenv("FILE_PATH")
_PORT = os.getenv('PORT')
_HOST = os.getenv('HOST')

app = Flask(__name__)
CORS(app)


@app.route("/balance")
def check_balance():
    balance, status, error = credit_balance(_FILE_PATH)

    response = {
        'balance': balance,
        'status': status,
        'error': error
    }
    return jsonify(response)


@app.route("/vfc")
def call_vfc():
    tracked = vfc(_FILE_PATH)
    status = "Success"

    # TODO: error handling
    response = {
        'status': status,
        'tracked':tracked
    }
    return jsonify(response)


@app.route("/register")
def register():

    # TODO: error handling
    no_of_reg = registering(_FILE_PATH)
    status = "Success"

    response = {
        'status': status,
        'no_of_regs': no_of_reg,
        'cost': str(no_of_reg * 100)
    }
    return jsonify(response)


@app.route("/svp")
def svp():
    # TODO: error handling
    vessel_position = single_vessel_position(_FILE_PATH)
    status = "Success"

    response = {
        'status': status,
        'vessel_position': vessel_position,
        'cost': str(vessel_position * 7)
    }
    return jsonify(response)


@app.route("/form", methods=['POST'])
def getForm():
    if request.get_json() is not None:
        input_params = request.get_json()
        status, rows = input_form_data(input_params, _FILE_PATH)

        response = {
            'status': status,
            'rows': rows
        }

        return jsonify(response)

    response = {
        'status': "Failed"
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=_PORT, host=_HOST)
