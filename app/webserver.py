from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    data = "Home"
    return jsonify(data), 200


@app.route("/credentials", methods=['GET'])
def getCreds():
    return jsonify({
        "user": "admin",
        "pwd": "admin@123"
    })


@app.route("/consume", methods=['POST'])
def inputData():
    data = request.get_json(force=True)
    day = data.get('day', 'Sunday')
    tm = data.get('tm', '00')

    rtn = {"sts": "Run"}

    if day == "Sunday" and int(tm) > 1:
        rtn = {"sts": "NoRun"}

    return jsonify(rtn), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5025)
