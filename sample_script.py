import json
import sys
import os

prefix = sys.argv[1]
find_command = "find /srv/runme --name {0}*".format(prefix)
os.system(find_command)