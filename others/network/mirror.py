"""
Implements the packet mirroring functionality 
"""
from Queue import Queue
from threading import Thread
import socket

from time import sleep

import rawsocket


class packetMirror:
    """This is a class that implements packet mirroring
    """
    def __init__(self, interface = None, start = False):
        print 'Mirroring object created'
        self.interface = interface 
        self.start = start
        self.msgq = Queue()
        self.rawsocket = rawsocket.rawsocket(self.interface)
        
        print 'starting thread'
        try:
            self.thread_id = Thread(target=self.thread_start, args=(self.start,))
            self.thread_id.start()
        except Exception: 
            print 'error occured'
        self.sock = -1
        
    def put_msg(self, packet):
        """
        Put a packet in queue
        """
        if self.start is True: 
            self.msgq.put(packet)
    
    def get_msg(self):
        """
        Reads a message from queue
        """
        return self.msgq.get()
        
    def process_queue(self):
        """
        Starts reading the messages from queue 
        """
        while True:
            msg = self.get_msg()
            print 'msg received: ', msg
            self.process_message(msg)
            self.msgq.task_done()
        
    def process_message(self, msg):
        """
        Processes messages received in queue
        """
        raw_packet = rawsocket.rawpacket_v1(msg[0],
                                            msg[1],
                                            msg[2],
                                            msg[3],
                                            msg[4],
                                            msg[5],
                                            msg[6])
        
        self.rawsocket.sendpacket(raw_packet.get_packet())
        pass
    
    def start_capture(self):
        self.start = True
    
    def stop_capture(self):
        self.start = False
    
    def thread_start(self, start):
        """
        starts the queue thread 
        """
        print 'thread started'
        self.process_queue()
        
    def thread_start_old(self, start):
        """
        starts the queue thread 
        """
        print 'thread started'
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('192.168.1.39', 18888))
        
        self.process_queue()
         
    def __str__(self):        
        ret_str = 'ip = %s:%d itf=%s qsize=%d' % (self.ipaddr, self.port, self.interface, self.msgq.qsize())
        return ret_str
        
    def log_packetmirror_stats(self):
        """
        Prints packet mirroring statistics
        """
        print self
        

pkt_obj = packetMirror('lo')

pkt_obj.start_capture()

while True:
    packet = 'ABCD'
    payload = ['00:0a:ff:12:ff:fe',
               '00:0a:ff:12:ff:ff',
               '10.10.10.10',
               '10.10.10.11',
               5555,
               5655,
               packet]
    
    print 'sending packets'
    pkt_obj.put_msg(payload)
    print pkt_obj
    sleep(1)

