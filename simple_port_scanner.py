# Programmer: Rob Laudadio
# GitHub: roblaud
# Program that scans ports open on a given ip address
# Created following an online ethical hacking tutorial by HackerSploit

import socket

# AF_INET specifies IPV4, SOCK_STREAM specifies TCP, timeout set to 10 seconds
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

# Ask user for what to scan
host = input('Please enter the IP address for scanning: ')
port = int(input('Please enter the port: '))

def portScanner(port):
    # connect_ex will return an error and not throw an exception
    if s.connect_ex((host, port)):
        print('Port closed')
    else:
        print('Port open')

portScanner(port)