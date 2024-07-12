import flask
from flask import request, jsonify, abort

from cal import Calculator

api = flask.Flask(__name__)


@api.route('/cal/paperless', methods=['POST'])
def paperless():
    value = flask.request.form.get('paperless')
    if value is None or value == '':
        abort(400, description="Missing 'paperless' value")
    try:
        paperless_value = int(value)
    except ValueError:
        abort(400, description="Invalid value for 'paperless'")

    calculator = Calculator({'paperless': paperless_value})
    result = calculator.paperless()
    return jsonify({'paperless': result})

@api.route('/cal/bottle', methods=['POST'])
def bottle():
    value = flask.request.form.get('bottle')
    if value is None or value == '':
        abort(400, description="Missing 'bottle' value")
    try:
        bottle_value = int(value)
    except ValueError:
        abort(400, description="Invalid value for 'bottle'")

    calculator = Calculator({'bottle': bottle_value})
    result = calculator.bottle()
    return jsonify({'bottle': result})

@api.route('/cal/electricity', methods=['POST'])
def electricity():
    value = flask.request.form.get('electricity')
    if value is None or value == '':
        abort(400, description="Missing 'electricity' value")
    try:
        electricity_value = int(value)
    except ValueError:
        abort(400, description="Invalid value for 'electricity'")

    calculator = Calculator({'electricity': electricity_value})
    result = calculator.electricity()
    return jsonify({'electricity': result})


@api.route('/cal', methods=['POST'])
def cal():
    data = {}
    int_fields = ['gas', 'water', 'food_ware', 'staff', 'e_invoice', 'cloud_invoice', 'paper_box', 'garbage']
    str_fields = ['origin', 'destination']

    for field in int_fields:
        value = flask.request.form.get(field)
        if value is not None and value != '':
            try:
                data[field] = int(value)
            except ValueError:
                abort(400, description=f"Invalid value for {field}")

    for field in str_fields:
        value = flask.request.form.get(field)
        if value is not None and value != '':
            data[field] = str(value)

    calculator = Calculator(data)
    co2data = calculator.calculation()
    print(co2data)
    return flask.jsonify(co2data)

@api.route('/')
def index():
    return "Testing API Connection Success!"  

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080, debug=True)