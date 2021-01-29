#!/usr/bin/python3

"""
Description:
    - Example of using argparse module

Usage : 
    $ ./argparse_example.py --help
"""

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example of using argparse module")
    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = 'command'

    # get our global options and subcommand
    parser.add_argument('--database', help='Specify a database to use (default = ./tickets.db)')
    parser.add_argument('--service', help='Specify which service to work with')

    # setup download
    download_parser = subparsers.add_parser('download', help='Download all tickets from specified service')
    download_parser.add_argument('-j', '--json', help='Specify a json cache')

    # setup export
    export_parser = subparsers.add_parser('export', help='Export all tickets to specified file')
    export_parser.add_argument('-o', '--output', help='Specify output file',
                                                 required=True)

    args = parser.parse_args()

    # call the command with our args
    ret = getattr(sys.modules[__name__], 'main_{0}'.format(args.command))(args)
    sys.exit(ret)