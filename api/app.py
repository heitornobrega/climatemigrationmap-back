from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)

def read_csv():
    data = {}
    group_by = request.args.get('group_by', default='country')
    csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "migration.csv")
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row["Country or Area"]
            year = row["Year(s)"]
            migration = row["Value"]

            if group_by == 'country':
                if country in data:
                    data[country].append({"Year": year, "Value": migration})
                else:
                    data[country] = [{"Year": year, "Value": migration}]
            elif group_by == 'year':
                if year in data:
                    data[year][country] = migration
                else:
                    data[year] = {country: migration}
            else:
                return jsonify({"error": "Invalid 'group_by' value. Use 'country' or 'year'."}), 400

    return data

@app.route('/migration', methods=['GET'])
def get_migration():
    data = read_csv()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
