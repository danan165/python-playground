import flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("hello.html")


@app.route("/multiply/<x>/<y>/", methods=['GET', 'POST'])
def multiply(x, y):
    result = int(x) * int(y)
    context = {"result": result}
    return flask.render_template("multiply.html", **context)


if __name__ == "__main__":
    app.run()

