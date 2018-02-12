import os
import json
import sys

prefix = sys.argv[1]
#find_command = "find /srv/runme --name {0}*".format(prefix)
#os.system(find_command)
directory = '/home/ec2-user/srv/runme'
#directory = '/Users/danielle/Desktop/HardWork/USF/Module3/MSAN603/GroupProject/Sprint1'

def process_file(file_name):
    print 'trying to load'
    opened_file = open(directory + '/'+ file_name)
    for line in opened_file:
        try:
            loaded_json = json.loads(line)
            print loaded_json
            name = loaded_json["name"]
            age = loaded_json["prop"]["age"]
            if loaded_json["prop"]["age"] >= 0:
                output_file = open(directory + '/' + prefix + '.txt', 'a')
                output_file.write(name+'\t'+str(age)+'\n')
                output_file.close()
        except:
            print 'JSON not formatted correctly!'
    opened_file.close()


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