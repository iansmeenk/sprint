import os
import json
import sys

prefix = sys.argv[1]
#find_command = "find /srv/runme --name {0}*".format(prefix)
#os.system(find_command)
directory = '/srv/runme'

def process_json(data):
    """process json and write to <prefix>.txt
    
    prefix is determined when deploy is run
    
    params
    -----
    data: dictionary read from requests.get_json()
    """
    try:
        name = data["name"]
        age = data["prop"]["age"]
        if data["prop"]["age"] >= 0:
            output_file = open(directory + '/' + prefix + '.txt', 'a')
            output_file.write(name+'\t'+str(age)+'\n')
            output_file.close()
    except:
        print 'JSON not formatted correctly!'
