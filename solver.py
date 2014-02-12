from flask import Flask
from flask import request
import operator
import sympy
import json

app = Flask(__name__, static_url_path="/static")

x = sympy.symbols("x")

equation = [(3*x+1, 7)]

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route("/get")
def get():
    return jsonerfy()

@app.route("/step", methods=["POST"])
def step():
    js = request.get_json()

    if js['op'] == "add":
        op = operator.add
        oop = operator.sub
    elif js['op'] == 'sub':
        op = operator.sub
        oop = operator.add
    elif js['op'] == 'mul':
        op = oop = operator.mul
    elif js['op'] == 'div':
        op = oop = operator.div
    else:
        return "Unknown operation", 400

    v = int(js['value'])

    if js['side'] == 'l':
        l = op(equation[-1][0], v)
        r = oop(equation[-1][1], v)
        equation.append((l, r))
    elif js['side'] == 'r':
        r = op(equation[-1][1], v)
        l = oop(equation[-1][0], v)
        equation.append((l, r))
    else:
        return "Unknown side", 400

    return jsonerfy()


def jsonerfy():
    response = []
    for e in equation:
        response.append("%s=%s" % (e[0], e[1]))
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True)
