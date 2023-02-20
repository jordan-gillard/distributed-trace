from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

tracer = trace.get_tracer(__name__)
resource = Resource(attributes={
    SERVICE_NAME: "checkout_msvc"
})
provider = TracerProvider(resource=resource)
otlp_processor = BatchSpanProcessor(OTLPSpanExporter(insecure=True))
provider.add_span_processor(otlp_processor)
trace.set_tracer_provider(provider)
