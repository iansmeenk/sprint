import os
import json
import sys

#find_command = "find /srv/runme --name {0}*".format(prefix)
#os.system(find_command)
directory = '/home/ec2-user/srv/runme'


def process_json(data, prefix):
    """process json and write to <prefix>.txt

    params
    -----
    data: dictionary read from requests.get_json()

    prefix: directory where output should be written
    """

    def is_valid_age(age):
        if age >= 0:
            return True
        else:
            return False

    def has_name(name):
        if name != '':
            return True
        else:
            return False

    try:
        data = json.loads(data)
        name = data["name"]
        age = data["prop"]["age"]
        if is_valid_age(age) and has_name(name):
            output_file = open(directory + '/' + prefix + '/proc.txt', 'a')
            output_file.write(name + '\t' + str(age) + '\n')
            output_file.close()
    except:
        print 'JSON not formatted correctly!'
