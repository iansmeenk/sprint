import sys

from flask import Flask, request
import logging
from logging.handlers import TimedRotatingFileHandler

from data_processing import process_json


prefix = sys.argv[1]
app = Flask(__name__)

# Create rotating logs every 2 minutes
logger = logging.getLogger("Rotating Logger")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/srv/runme/'+prefix+'/Raw.txt', when='m', interval=2)
logger.addHandler(handler)


@app.route("/", methods=['POST'])
def process():
    """
    Take a post request, process the body as json, and write to file
    """
    logger.info(request.data)
    content = request.data # Get the json blob to process
    process_json(content, prefix) # Process and write to file
    return "Request Processed\n"


app.run(host='0.0.0.0', port=8080)

