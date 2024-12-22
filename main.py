from flask import Flask
import csv
import json
import argparse

app = Flask(__name__)


def csv_to_json(file_path):
    data = []
    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    filtered_data = {}
    for entry in data:
        address = entry["address"]
        expire = int(entry["expire"])
        if address not in filtered_data or expire > int(
            filtered_data[address]["expire"]
        ):
            filtered_data[address] = entry

    return json.dumps(filtered_data, indent=2)


@app.route("/leases", methods=["GET"])
def serve_json():
    csv_file_path = "/var/lib/kea/dhcp4.leases"
    json_data = csv_to_json(csv_file_path)
    return json_data, 200, {"Content-Type": "application/json"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = parser.parse_args()
    app.run(debug=True, host=args.host)


if __name__ == "__main__":
    main()
