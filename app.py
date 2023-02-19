from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import Tracer

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer: Tracer = trace.get_tracer(__name__)

app = Flask(__name__)


@tracer.start_as_current_span("checkout")
@app.route("/checkout")
def checkout():
    return "You have successfully checked out your shopping cart."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
