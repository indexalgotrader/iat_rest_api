import pytz
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from helpers.mongo_helper import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

IST = pytz.timezone('Asia/Kolkata')


@app.route('/')
def index():
    return jsonify({'status': 'done', 'time': datetime.now(IST)})


@app.route('/get_counters')
@cross_origin()
def get_counters():
    strategy_id = int(request.args.get('strategy_id'))

    all_counters = []
    results = strategy_execution.find({'strategy': strategy_id}).sort([("run_counter", pymongo.DESCENDING)])

    for item in results:
        all_counters.append({
            '_id': item['_id'], 'run_counter': item['run_counter'],
            'execution_date': item['execution_date'], 'pnl': item['pnl']
        })

    return jsonify(all_counters)


@app.route('/get_by_id')
@cross_origin()
def get_data_by_id():
    obj_id = request.args.get('obj_id')
    data = strategy_execution.find_one({'_id': obj_id})

    return jsonify(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port=int(5000))
