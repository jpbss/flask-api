from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, Flask!")

@app.route('/sobre')
def about():
    return jsonify(message="Api para prática de devops")

@app.route('/mult/<int:x>/<int:y>')
def multiply(x, y):
    result = x * y
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
