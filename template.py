#!/usr/bin/python3

import argparse
import colors
from py3Testify.connectors.ConnectorSSH import ConnectorSsh


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--list", help="list available projects")
    parser.add_argument("-o", "--list_loc", help="list available projects from other location")
    parser.add_argument("-r", "--run", help="run specific test plan")

    parser.add_argument("-j", "--jump", dest="JUMP_FILE", help="load jump route from file")
    parser.add_argument("-p", "--plan", dest="TEST_PLAN", help="load test plan from file")
    parser.add_argument("-v", "--verbose", dest="VERBOSE", action='store_true', help="verbose output")

    args = parser.parse_args()
    if args.VERBOSE:
        print('got verbose one...')


if __name__ == "__main__":
    main()
    print(colors.red('[localhost]'))
    sh = ConnectorSsh()
    sh.connect_to('myuser', 'myhost', 'uname -n')









