from flask import Flask, request
from process_file import process_json
import logging
from logging.handlers import TimedRotatingFileHandler


app = Flask(__name__)

# Create rotating logs every 2 minutes
logger = logging.getLogger("Rotating Logger")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('json_processing_logs.txt', when='m', interval=2)
logger.addHandler(handler)

@app.route("/<prefix>", methods='POST')
def process(prefix):

    content = request.get_json(silent=True)
    logger.info(content)
    content_processed  = process_json(content, prefix) # Process and write to file


app.run(host='0.0.0.0', port=8080)

