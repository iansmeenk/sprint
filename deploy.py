#!/usr/bin/env python

import paramiko
import time

def deploy(path, server, prefix):
    """ssh into remote server & search for json files
    beginning with prefix
    
    params
    -----
    path: filepath to .pem file to ssh into amazon server
    server: amazon server to ssh to
    prefix: prefix of json files to search for
    """
    # connect to server
    print 'Connecting to box'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username='testtest', key_filename=path)
    # clone repo
    ssh.exec_command('rm -rf sprint')
    ssh.exec_command('git clone https://github.com/iansmeenk/sprint.git')
    print 'Pull from github successful'
    ssh.exec_command('cd sprint')
    ssh.exec_command('screen -d -m -S flask python applet.py %s' % prefix)
    print 'Script initialized'
    ssh.close()

# test deploy
# deploy('/Users/danielle/Desktop/HardWork/USF/Module3/MSAN603/GroupProject/Sprint_DDIHS.pem', 'ec2-54-218-16-236.us-west-2.compute.amazonaws.com', 'name_')
