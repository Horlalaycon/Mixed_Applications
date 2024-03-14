# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon

import socket

""" This python program is used to convert dns to ip address"""


def convert_dns(host):
    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set time out
    sock.settimeout(1)

    # get ip address
    ip_addr = socket.gethostbyname(host)

    print(f'host: {host} ip_addr is: {ip_addr}')


dns = input("Enter DNS (google.com):")

convert_dns(dns)
