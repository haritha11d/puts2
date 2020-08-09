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
        warning = "Something wrong! --> input should consist of a vector of real numbers.\n"
        return warning
    except TypeError:
        warning = "Something wrong! --> input should consist of a vector of real numbers.\n"
        return warning
    except Exception as e:
        exception = str(e)
        return exception
    return values


@app.route('/')
def index():
    return 'Usage: \n<Operation>?A=<Value1, Value2, ..., ValueN>'


@app.route('/mean', methods=['GET', 'POST'])
@app.route('/average', methods=['GET', 'POST'])
@app.route('/avg', methods=['GET', 'POST'])
def mean():
    try:
        values = input_handling()
        answer = sum(values) / len(values)
    except ValueError:
        warning = input_handling()
        return warning
    except TypeError:
        warning = input_handling()
        return warning
    except Exception as e:
        exception = input_handling()
        return exception

    else:
        if float(answer).is_integer():
            answer = int(answer)
            return "%d \n" % answer
        return str(float(round(answer, 3))) + " \n"


@app.route('/max', methods=['POST', 'GET'])
def maximum():
    try:
        values = input_handling()
        answer = max(values)
    except ValueError:
        warning = input_handling()
        return warning
    except TypeError:
        warning = input_handling()
        return warning
    except Exception as e:
        exception = input_handling()
        return exception

    else:
        if float(answer).is_integer():
            answer = int(answer)
            return "%d \n" % answer
        return str(float(round(answer, 3))) + " \n"


@app.route('/min', methods=['POST', 'GET'])
def minimum():
    try:
        values = input_handling()
        answer = min(values)
    except ValueError:
        warning = input_handling()
        return warning
    except TypeError:
        warning = input_handling()
        return warning
    except Exception as e:
        exception = input_handling()
        return exception

    else:
        if float(answer).is_integer():
            answer = int(answer)
            return "%d \n" % answer
        return str(float(round(answer, 3))) + " \n"


@app.route('/median', methods=['POST', 'GET'])
def median():
    try:
        values = input_handling()
        answer = statistics.median(values)
    except ValueError:
        warning = input_handling()
        return warning
    except TypeError:
        warning = input_handling()
        return warning
    except Exception as e:
        exception = input_handling()
        return exception

    else:
        if float(answer).is_integer():
            answer = int(answer)
            return "%d \n" % answer
        return str(float(round(answer, 3))) + " \n"


if __name__ == '__main__':
    app.run()
