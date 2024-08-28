
from flask import Flask, jsonify
from src.data_collector import DataCollector
from src.predictor import Predictor

app = Flask(__name__)

data_collector = DataCollector()
predictor = Predictor()

@app.route('/api/v1/predictions', methods=['GET'])
def get_predictions():
    data = data_collector.collect_data()
    predictions = predictor.predict(data)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
