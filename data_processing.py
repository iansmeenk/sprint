import os
import json
import sys

#find_command = "find /srv/runme --name {0}*".format(prefix)
#os.system(find_command)
directory = '/Home/ec2-user/srv/runme'

def process_json(data, prefix):
    """process json and write to <prefix>.txt
    
    params
    -----
    data: dictionary read from requests.get_json()
    
    prefix: directory where output should be written
    """
    try:
        name = data["name"]
        age = data["prop"]["age"]
        if data["prop"]["age"] >= 0:
            output_file = open(directory + '/' + prefix + '/proc.txt', 'a')
            output_file.write(name+'\t'+str(age)+'\n')
            output_file.close()
    except:
        print 'JSON not formatted correctly!'
