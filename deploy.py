#!/usr/bin/env python

import paramiko
import time

## Example Deploy Script
## This file uses paramiko to login to a box. Note that this is a skeleton file and you will need to do a bunch to complete the assignment.

# print "Connecting to box"
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('', username = '', key_filename = '' )


# ssh.exec_command("rm -rf sprint; git clone https://github.com/iansmeenk/sprint.git")
# print "Pull from Github successful"
# time.sleep(10)
# print "Script fully executed ... exhilarating"
# ssh.close()
## EOF ##

def deploy(path, server, prefix):
    # connect to server
    #try:
    print 'Connecting to box'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username = 'ec2-user', key_filename=path)
    # clone repo
    ssh.exec_command('rm -rf sprint')
    ssh.exec_command('git clone https://github.com/iansmeenk/sprint.git')
    print 'Pull from github successful'
    ssh.exec_command('cd sprint')
    ssh.exec_command('crontab -l > mycron; echo "* * * * * python sample_script.py %s" >> mycron; crontab mycron; rm mycron' % prefix)
    print 'Script initialized'
    ssh.close()
    #except Exception as inst:
        #print("Error" + str(inst))

# test deploy
deploy('/Users/danielle/Desktop/HardWork/USF/Module3/MSAN603/GroupProject/Sprint_DDIHS.pem', 'ec2-54-218-16-236.us-west-2.compute.amazonaws.com', 'name_')
