#!/usr/bin/env python

import paramiko
import time

## Example Deploy Script
## This file uses paramiko to login to a box. Note that this is a skeleton file and you will need to do a bunch to complete the assignment.

print "Connecting to box"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('', username = '', key_filename = '' )


ssh.exec_command("rm -rf sprint; git clone https://github.com/iansmeenk/sprint.git")
print "Pull from Github successful"
time.sleep(10)
print "Script fully executed ... exhilarating"
ssh.close()
## EOF ##


