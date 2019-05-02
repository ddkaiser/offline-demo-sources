#!/usr/bin/python3

from flask import Flask, jsonify, abort, make_response
import datetime

app = Flask(__name__)

orders = [
    {
        'id': 1,
        'customer': u'John Doe',
        'cart': [{1: 1001}, {1: 2002}],
        'shipped': False
    },
    {
        'id': 2,
        'customer': u'Jane Doe',
        'cart': [{1: 1003}, {2: 1004}],
        'shipped': False
    }
]

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return "Sample Data Services; Current Time: " + str(datetime.datetime.now()) + "\n"

@app.route('/commerce/api/v1.0/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

@app.route('/commerce/api/v1.0/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})

if __name__ == '__main__':
    app.run(debug=True)

