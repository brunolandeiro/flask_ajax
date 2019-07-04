from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/getSelect')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    if(a == 1):
        return jsonify(result=['aaa', 'bbb', 'ccc'])
    if(a == 2):
        return jsonify(result=['ddd', 'eee', 'fff'])
    if (a == 3):
        return jsonify(result=['ggg', 'me paga', 'um chopp'])


@app.route('/')
def index():
    return render_template('index.html')
