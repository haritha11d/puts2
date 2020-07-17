from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


if __name__ == "__main__":
    app.run()
