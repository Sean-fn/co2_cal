import flask
from flask import request, jsonify, abort

from cal import Calculator


api = flask.Flask(__name__)

@api.route('/cal', methods=['POST'])
def cal():
    allowed_ip = '0.0.0.0'
    requester_ip = request.remote_addr

    # if requester_ip != allowed_ip:
    #     abort(403, description="Access denied")

    data = {
        'gas': int(flask.request.form.get('gas')),  # 省油（汽油）
        'water': int(flask.request.form.get('water')),  # 省水
        'food_ware': int(flask.request.form.get('food_ware')),  # 使用環保杯筷
        'origin': str(flask.request.form.get('origin')),  # 起點（用於計算車程）
        'destination': str(flask.request.form.get('destination')),  # 終點（用於計算車程）
        'staff': int(flask.request.form.get('staff')),  # 減少臨櫃服務
        'invoice': int(flask.request.form.get('invoice')),  # 發票（原本的發票）
        'electricity': int(flask.request.form.get('electricity')),  # 節電
        'bottle': int(flask.request.form.get('bottle')),  # 減少瓶裝水/寶特瓶
        'paper_box': int(flask.request.form.get('paper_box')),  # 減少紙餐盒
        'garbage': int(flask.request.form.get('garbage')),  # 減少垃圾（廚餘）
        'paperless': int(flask.request.form.get('paperless')),  # 無紙化
    }
    print('before_cal', data)

    calculator = Calculator(data)
    co2data = calculator.calculation()
    print(co2data)
    return flask.jsonify(co2data)

@api.route('/')
def index():
    return "Testing API Connection Success!"  


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000, debug=True)
