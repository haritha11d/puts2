from flask import Flask, request
from fractions import Fraction
import statistics

app = Flask(__name__)


def input_handling():
    if request.method == 'GET':
        values = request.args.get('X', default=0, type=str)

    else:
        values = request.values.get('X', default=0, type=str)
    try:
        values = [Fraction(value) for value in values.split(',')]
    except ValueError:
        warning = "Something wrong! --> input should consist of a vector of real numbers."
        return warning

    return values


@app.route('/median', methods=['GET', 'POST'])
def median():
    try:
        values = input_handling()
        answer = statistics.median(values)
    except ValueError:
        warning = input_handling()
        return warning
    else:
        if float(answer).is_integer():
            answer = int(answer)
            return "%d \n" % answer
        return str(float(round(answer, 3))) + " \n"
