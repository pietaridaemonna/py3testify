#!/usr/bin/python3

import sys
import time
import paramiko
import os


class ConnectorSsh(object):
    def __init__(self):
        self.user = 'connector'
        self.host = 'host'
        self.i = 1

    def connect_to(self, user, host, command):
        client = {}
        while True:
            print("connecting to %s (%i/30)" % (host, self.i))

            try:
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
                # execute command
                stdin, stdout, stderr = client.exec_command(command)
                print('STDOUT: ' + stdout.read().decode('utf-8'))
                print('STDERR: ' + stderr.read().decode('utf-8'))
                break
            except paramiko.AuthenticationException:
                print("Authentication failed when connecting to %s" % host)
                sys.exit(1)
            except:
                print("Could not SSH to %s, waiting for it to start" % host)
                self.i += 1
                time.sleep(2)

            # If we could not connect within time limit
            if self.i == 30:
                print
                "Could not connect to %s. Giving up" % host
                sys.exit(1)



