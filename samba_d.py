#!usr/bin/env python

import configparser
import subprocess

'''
Installs samba
Change the .conf files with necessary changes
'''

'''
@bug does not save the comments of original .conf file
'''

samba_config_path = '/etc/samba/smb.conf'

subprocess.call('sudo apt-get install samba'.split())
config = configparser.ConfigParser()
config.read(samba_config_path)

config.set('global', 'logging', 'file')
config.set('global', 'log level', '2')

hostname = subprocess.check_output('hostname').decode('utf-8')
config.set('global', 'netbios name', hostname)

with open(samba_config_path, 'w') as f:
    config.write(f)

