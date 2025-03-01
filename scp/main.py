#!/usr/bin/env python3

import argparse
from scp import SCPClient

def main():
    parser = argparse.ArgumentParser(description='Description of your script.')
    parser.add_argument('hostname', type=str)
    parser.add_argument('port', type=str)
    parser.add_argument('user_id', type=str)
    parser.add_argument('user_pw', type=str)
    parser.add_argument('file_location', type=str)
    args = parser.parse_args()

    # skip the verification of the passing variables for now

    print(f'The passed variable for the file location is: {args.file_location}')
    print(f'The passed variable for the IP for vm is: {args.hostname}')

    # establish TCP connection to vm server via socket
    client = SCPClient(args.hostname, args.port, args.user_id, args.user_pw, args.file_location)
    client.connect_vm()


    # send data to vm


if __name__ == '__main__':
    main()