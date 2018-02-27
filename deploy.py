import paramiko


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
    # start screen
    ssh.exec_command('screen -d -m -S flask python ~/sprint/applet.py %s' % prefix)
    print 'Script initialized'
    ssh.close()

if __name__ == '__main__':
    # test deploy
    # deploy()
