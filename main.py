from flask import Flask, request

from server.api.add_data.services import add_data_service
from server.api.get_data.services import get_data_service

app = Flask(__name__)


# Time taken for the assignment around 1 h 15 minutes
# Updated flask version (some error occurred with pydantic package with provided version)

@app.post("/data")
def post_data():
    """Act as a request router."""

    plaintext_data = request.data.decode("utf-8")
    post_data_response = add_data_service(plaintext_data=plaintext_data)
    return post_data_response


@app.get("/data")
def get_data():

    from_timestamp = request.args.get('from')
    to_timestamp = request.args.get('to')
    get_data_response = get_data_service(from_timestamp=from_timestamp, to_timestamp=to_timestamp)
    return get_data_response


if __name__ == "__main__":
    app.run()
