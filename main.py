from flask import Flask, request

from db import get_reading, add_reading
from server.api.add_data.services import add_data_service

app = Flask(__name__)


@app.post("/data")
def post_data():
    """Act as a request router."""

    plaintext_data = request.data.decode("utf-8")
    post_data_response = add_data_service(plaintext_data=plaintext_data)
    return post_data_response


@app.get("/data")
def get_data():
    # TODO: check what dates have been requested, and retrieve all data within the given range

    return {"success": False}


if __name__ == "__main__":
    app.run()
