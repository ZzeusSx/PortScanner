#!/usr/bin/env python3
#Simple python3 port scanner credits to StackOverFlow!
import argparse
import os
import subprocess
import socket

#parsing arguments
parser=argparse.ArgumentParser()
#taking arguments
parser.add_argument("ip_addr", help="IPv4 address of the target")
parser.add_argument("-v", "--verbose", help="give output in verbosity (show even the closed ports)", action="store_true")

args=parser.parse_args()
print(args.ip_addr)


def __port__(port):
    try:
        s=socket.socket()
        s.settimeout(0.5)
        s.connect((args.ip_addr,port))
        print(args.ip_addr)
        return True
    except:
        return False
    finally:
        s.close()



#edit 0,1025 to change scanning port numbers example 0-10000, 0-65535
if args.verbose:
    for x in range (0,1025):
        if __port__(x):
            print("[+] {}:{} is open".format(args.ip_addr,x))
        else:
            print("[+] {}:{} is closed".format(args.ip_addr,x))

else:
    for x in range (0,1025):
        if __port__(x):
            print("[+] {}:{} is open".format(args.ip_addr,x))

