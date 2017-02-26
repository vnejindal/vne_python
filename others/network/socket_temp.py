#/usr/bin/python -t

"""
import socket
import fcntl
def open_socket():
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) 
    sock.bind(('10.10.10.10', 18888))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)
    #fcntl.ioctl(sock, socket.SIO_RCVALL, socket.RCVALL_ON)

open_socket()
"""
from socket import socket, AF_PACKET, SOCK_RAW, PF_PACKET
#s = socket(AF_PACKET, SOCK_RAW)
s = socket(PF_PACKET, SOCK_RAW)
#s.bind(("eth0", 0))
s.bind(("tap0", 0))

# We're putting together an ethernet frame here, 
# but you could have anything you want instead
# Have a look at the 'struct' module for more 
# flexible packing/unpacking of binary data
# and 'binascii' for 32 bit CRC
src_addr = "\x26\x29\x85\xb4\x44\x55"
dst_addr = "\xff\xff\xff\xff\xff\xff"
#src_addr = "\x01\x02\x03\x04\x05\x06"
#dst_addr = "\x01\x02\x03\x04\x05\x06"
payload = ("["*30)+"PAYLOAD"+("]"*30)
checksum = "\x1a\x2b\x3c\x4d"
ethertype = "\x08\x01"

s.send(dst_addr+src_addr+ethertype+payload+checksum)
