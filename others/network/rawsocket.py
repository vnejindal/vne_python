"""
This file implements raw socket functionality for sending a packet 

Its functionality is derived from: 
https://sandilands.info/sgordon/teaching/netlab/its332ap5.html
https://csl.name/post/raw-ethernet-frames/
http://www.binarytides.com/raw-socket-programming-in-python-linux/

class rawpacket_v1 is written entirely afresh to cater to exact requirements

Author: Vinay Jindal <vinay.jindal@gmail.com>

"""
import socket 
import binascii

class rawpacket:
    """
    Raw packet to be sent on network raw socket
    """
    def __init__(self, payload):
        
        self.payload = payload 
        self.eth_hdr = ''
        self.ip_hdr = ''
        self.tpt_hdr = ''
        
        self._create_ethheader()
        self._create_ipheader()
        self._create_tptheader()
        
    def _create_ethheader(self):
        """
        # Create an Ethernet frame header 
        # - Destination MAC: 6 Bytes 
        # - Source MAC: 6 Bytes 
        # - Type: 2 Bytes (IP = 0x0800) 
        # Change the MAC addresses to match the your computer and the destination 
        """
        self.eth_hdr = [0x00, 0x23, 0x69, 0x3a, 0xf4, 0x7d, # 00:23:69:3A:F4:7D 
            0x90, 0x2b, 0x34, 0x60, 0xdc, 0x2f, # 90:2b:34:60:dc:2f 
            0x08, 0x00]
        
    def _create_ipheader(self):    
        """
        # Create IP datagram header 
        # - Version, header length: 1 Byte (0x45 for normal 20 Byte header) 
        # - DiffServ: 1 Byte (0x00) 
        # - Total length: 2 Bytes 
        # - Identificaiton: 2 Bytes (0x0000) 
        # - Flags, Fragment Offset: 2 Bytes (0x4000 = Don't_Fragment)
        # - Time to Line: 1 Byte (0x40 = 64 hops) 
        # - Protocol: 1 Byte (0x01 = ICMP, 0x06 = TCP, 0x11 = UDP, ...)
        # - Header checksum: 2 Bytes 
        # - Source IP: 4 Bytes 
        # - Destination IP: 4 Bytes 
        """
        self.ip_hdr = [0x45, 
                  0x00, 
                  0x00, 0x54, #Total Length
                  0x80, 0xc6, 
                  0x40, 0x00, 
                  0x40, 
                  0x11,  # Protocol
                  0x36, 0x8a, # checksum - change this! 
                  0x0a, 0xa8, 0x01, 0x07, # 192.168.1.7 
                  0x0a, 0xa8, 0x01, 0x01] # 192.168.1.1 
 
    def _create_tptheader(self):
        """
        Creates Transport Header;
            For UDP Transport 
            - Source Port
            - Destination Port
            - Length 
            - Checksum 
        """
        self.tpt_hdr = [0x15, 0xb3, 
                        0x15, 0xb4,
                        0x00, 0x11,  #Length
                        0x00, 0x00]  #Checksum
    
    def get_packet(self):
        """
        create full packet and returns it 
        Encapsulates it in ethernet header, ip header and transport header
        # Frame structure: 
        # etherent_hdr | ip_hdr | icmp_hdr | icmp_data 
        #    14 B   | 20 B |  16 B  |  48 B 
        """
        eth_hdr_str = "".join(map(chr, self.eth_hdr)) 
        ip_hdr_str = "".join(map(chr, self.ip_hdr)) 
        tpt_hdr_str = "".join(map(chr, self.tpt_hdr))
        
        return eth_hdr_str + ip_hdr_str + tpt_hdr_str + payload
    
   

class rawpacket_v1:
    def __init__(self, smac, dmac, srcip, dstip, sport, dport, payload, proto = 'UDP'):
        
        self.smac = smac
        self.dmac = dmac
        self.srcip = srcip
        self.dstip = dstip
        self.sport = sport 
        self.dport = dport
        self.payload = payload
        self.proto = proto
        if self.proto == 'UDP':
            self.totlen = 12 + 20 + 8 + len(self.payload)
        else:  # In case of TCP or others...assumend only...
            self.totlen = 12 + 20 + 20 + len(self.payload)
	print self.totlen
        
     ######### NEW FUNCTIONS ###########
    def _get_int_to_hex(self, ival, fill = 4):
        """
        Get binary value after filling leading 'fill' zeros
        """
        return binascii.unhexlify(hex(ival)[2:].zfill(fill))
        
    def _get_binary_macaddr(self, macaddr):
        """
        returns binary string representation of macaddr string
        """
        return binascii.unhexlify(''.join(macaddr.split(':')))
    
    def _get_binary_ipaddr(self, ipaddr):
        """
        returns binary ipaddr of string dotted decimal notation 
        """
        return ''.join([self._get_int_to_hex(int(x),2) for x in ipaddr.split('.')])
        #return binascii.unhexlify(''.join(ipaddr.split('.')))
    
    def _get_eth_hdr(self):
        """
        returns binary string representation of ethernet header
         - Destination MAC: 6 Bytes 
         - Source MAC: 6 Bytes 
         - Type: 2 Bytes (IP = 0x0800) 
        """
        smac = self._get_binary_macaddr(self.smac)
        dmac = self._get_binary_macaddr(self.dmac)
        return ''.join([dmac,smac, ''.join(map(chr,[0x08, 0x00]))])

    def _get_ip_hdr(self):
        """
        returns binary representation of ip header
        # Create IP datagram header 
        # - Version, header length: 1 Byte (0x45 for normal 20 Byte header) 
        # - DiffServ: 1 Byte (0x00) 
        # - Total length: 2 Bytes 
        # - Identificaiton: 2 Bytes (0x0000) 
        # - Flags, Fragment Offset: 2 Bytes (0x4000 = Don't_Fragment)
        # - Time to Line: 1 Byte (0x40 = 64 hops) 
        # - Protocol: 1 Byte (0x01 = ICMP, 0x06 = TCP, 0x11 = UDP, ...)
        # - Header checksum: 2 Bytes 
        # - Source IP: 4 Bytes 
        # - Destination IP: 4 Bytes 
        """
        return ''.join([chr(0x45), 
                  chr(0x00), 
                  self._get_int_to_hex(self.totlen),
                  #binascii.unhexlify(hex(self.totlen)[2:].zfill(4)),
                  ''.join(map(chr,[0x80, 0xc6, 
                  0x40, 0x00, 
                  0x40, 
                  0x11,  # Protocol
                  0x00, 0x00])), # checksum - set to 0x00 
                  self._get_binary_ipaddr(self.srcip),
                  self._get_binary_ipaddr(self.dstip)
                  ])
     
    
    def _get_tpt_hdr(self):
        """
        Creates Transport Header;
            For UDP Transport 
            - Source Port
            - Destination Port
            - Length 
            - Checksum 
        """
        return ''.join(map(self._get_int_to_hex,[self.sport, 
                        self.dport,
                        self.totlen - 20 - 12, 
                        0x00
                        ]))           

    def get_packet(self):
        """
        New version of get packet function 
        """
        eth_hdr = self._get_eth_hdr()
        ip_hdr = self._get_ip_hdr()
        tpt_hdr = self._get_tpt_hdr()
        return eth_hdr + ip_hdr + tpt_hdr + self.payload
            
    ######### NEW FUNCTIONS ###########
    
class rawsocket:
    """
    Defines class to represent a raw socket and send data to it
    """
    def __init__(self, interface):
        self.interface = interface
        self.protocol = 0 # = ICMP, 6 = TCP, 17 = UDP, etc. 
        # Create a raw socket with address family PACKET 
        self.sock_fd = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        #Windows: self.sock_fd = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        # Bind the socket to an interface using the specific protocol 
        self.sock_fd.bind((self.interface,self.protocol)) 
 

        
    def send_packet(self, payload):
        """
        sends a raw packet to opened raw socket
        """
        # Convert byte sequences to strings for sending 
        
        self.sock_fd.send(payload) 


payload = 'Hello Vne'
pkt = rawpacket_v1('00:0a:ff:12:ff:fe',
                   '00:0a:ff:12:ff:ff',
                   '10.10.10.10',
                   '10.10.10.11',
                   5555,
                   5655,
                   payload)

rs = rawsocket('lo')
rs.send_packet(pkt.get_packet())
