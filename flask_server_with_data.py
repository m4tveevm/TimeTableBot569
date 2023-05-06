from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/schedule')
def get_schedule():
    df = pd.read_csv('data.csv', sep=';', encoding='utf-8')
    data = df.to_dict()
    return data


if __name__ == '__main__':
    app.run(port=8082, debug=True)
