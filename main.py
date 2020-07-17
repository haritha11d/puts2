from flask import Flask, request

app = Flask(__name__)


def input_handling():
    if request.method == 'GET':
        values = request.args.get('X', default=0, type=str)

    else:
        values = request.values.get('X', default=0, type=str)


    return values


@app.route('/mean', methods=['GET', 'POST'])
@app.route('/average', methods=['GET', 'POST'])
@app.route('/avg', methods=['GET', 'POST'])
def mean():
    pass


if __name__ == "__main__":
    app.run()
