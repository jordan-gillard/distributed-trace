# Distributed Trace
## About
This repository serves as my sandbox for implementing distributed traces in 
multiple microservices, and viewing those traces within the Jaeger UI. All
code uses the most recent version (as of this writing) of the [OpenTelemetry 
Protocol (OTEL)](https://opentelemetry.io).

## Running Locally
Running the code, hitting microservice endpoints, and viewing telemetry
data is easily accomplished using a Docker Compose network. Simply run
the following in your terminal (provided you have Docker installed).
```shell
docker-compose up
```
Then you can ping the microservice API and view the traces in the Jaeger UI.
```shell
# Send a GET request to the checkout microservice
curl 127.0.0.1:8080/checkout

# Then go to the URL for the Jaeger UI and view your traces :)
http://127.0.0.1:16686/
```
