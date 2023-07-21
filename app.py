from flask import Flask, jsonify
import csv

app = Flask(__name__)

def read_csv():
    data = []
    with open('temperature.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/temperature', methods=['GET'])
def get_temperature():
    data = read_csv()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
