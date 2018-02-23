# Sprint

*Devin Bowers, Holly Capell, Danielle Savage, Ian Smeenk, Spencer Stanley*

Deploy code to an AWS box to accept HTTP post requests at port 8080 and process json file contained therein.

## Contents

+ `deploy.py`: Connects to AWS instance via SSH and runs `applet.py`. \<prefix\> is specified in this file.
+ `applet.py`: Runs flask app which listens on port 8080, logs post requests, and processes valid json, writing results to file \<prefix\>.txt
+ `data_processing.py`: contains function `process_json()`, called by `applet.py` to parse information from json in post requests

