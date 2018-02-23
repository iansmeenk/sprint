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
    file_name: file path to json file to read
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

    
if __name__ == '__main__':
    prefixed = [filename for filename in os.listdir(directory) if filename.startswith(prefix)]
    print 'Found the Following Files'
    print prefixed

    output_file = open(directory + '/' + prefix + '.txt', 'w')
    output_file.close()

    for f in prefixed:
        try:
            process_file(f)
        except:
            print 'Could not process file...'
