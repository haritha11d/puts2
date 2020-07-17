from flask import Flask, request

app = Flask(__name__)


@app.route('/mean')
@app.route('/average')
@app.route('/avg')
def mean():
    pass


if __name__ == "__main__":
    app.run()
