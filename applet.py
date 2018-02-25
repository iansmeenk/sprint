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
#handler = TimedRotatingFileHandler('/srv/runme/'+prefix+'/Raw.txt', when='m', interval=2)
handler = TimedRotatingFileHandler('/home/ec2-user/srv/runme/'+prefix+'/Raw.txt',
                                   when='m', interval=2)
logger.addHandler(handler)

# Take a post request and process the body as json
@app.route("/", methods=['POST'])
def process():

    logger.info(request.data)
    content = request.data
    process_json(content, prefix) # Process and write to file
    return "Request Processed\n"


app.run(host='0.0.0.0', port=8080)

