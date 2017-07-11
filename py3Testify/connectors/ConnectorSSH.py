#!/usr/bin/python3

import paramiko
import os


class ConnectorSsh(object):
    def __init__(self):
        self.user = 'connector'
        self.host = 'host'

    def connect_to(self, user, host, command):
        print("ssh "+user+"@"+host)
        client = paramiko.SSHClient()
        client._policy = paramiko.WarningPolicy()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_config = paramiko.SSHConfig()
        user_config_file = os.path.expanduser("~/.ssh/config")
        if os.path.exists(user_config_file):
            with open(user_config_file) as f:
                ssh_config.parse(f)

        cfg = {'hostname': host, 'username': user}

        user_config = ssh_config.lookup(cfg['hostname'])
        for k in ('hostname', 'username', 'port'):
            if k in user_config:
                cfg[k] = user_config[k]

        if 'proxycommand' in user_config:
            cfg['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])

        client.connect(**cfg)
        stdin, stdout, stderr = client.exec_command(command)
        print('STDOUT: '+stdout.read().decode('utf-8'))
        print('STDERR: '+stderr.read().decode('utf-8'))
