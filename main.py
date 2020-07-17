from flask import Flask, request

app = Flask(__name__)


def input_handling():
    if request.method == 'GET':
        values = request.args.get('X', default=0, type=str)
    else:
        values = request.values.get('X', default=0, type=str)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


if __name__ == "__main__":
    app.run()
