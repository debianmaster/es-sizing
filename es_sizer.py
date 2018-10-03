from flask import Flask, request, jsonify
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route("/es/", methods=['GET'])
def es_storage_calculator():
    try:
        bytes_per_lines = int(request.args.get('bytes_per_lines'))
        lines_per_sec = int(request.args.get('lines_per_sec'))
        pods_per_nodes = int(request.args.get('pods_per_nodes'))
        number_of_nodes = int(request.args.get('number_of_nodes'))
        retention_days = int(request.args.get('retention_days'))
    except Exception as _:
        return abort(400)

    bytes_per_sec = (bytes_per_lines * lines_per_sec)

    total_pods = (pods_per_nodes * number_of_nodes)
    total_bytes_per_sec = bytes_per_sec * total_pods
    total_bytes_per_day = total_bytes_per_sec * (60 * 60 * 24)
    total_gb_per_day = total_bytes_per_day / (1024 * 1024 * 1024)
    total_elastic_storage = total_gb_per_day * retention_days

    response = {
        "es": {
            "input": {
                "bytes_per_lines": bytes_per_lines,
                "lines_per_sec": lines_per_sec,
                "pods_per_nodes": pods_per_nodes,
                "number_of_nodes": number_of_nodes,
                "retention_days": retention_days
            },
            "output": {
                "TOTAL_ES_STORAGE_GB": total_elastic_storage,
                "total_gb_per_day": total_gb_per_day,
                "total_bytes_per_day": total_bytes_per_day,
                "total_bytes_per_sec": total_bytes_per_sec,
                "bytes_per_sec": bytes_per_sec,
                "total_pods": total_pods
            }
        }
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
