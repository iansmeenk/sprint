from flask import Flask, request
from process_file import process_json


app = Flask(__name__)

@app.route("/<prefix>", methods='POST')
def process(prefix):

    content = request.get_json(silent=True)
    content_processed  = process_json(content)

    return content_processed


