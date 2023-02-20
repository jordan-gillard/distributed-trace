from flask import Flask

from tracer import tracer

app = Flask(__name__)


@app.route("/checkout")
def checkout():
    with tracer.start_as_current_span("checkout"):
        return "You have successfully checked out your shopping cart."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
