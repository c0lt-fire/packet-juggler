import socket
import array
import datetime
import SocketServer

class UdpSender(object):
	 def __init__(self, address):
	 	self._dest_ip = address[0]
	 	self._dest_port = address[1]
	 	self._sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
	 def send(self,datagram):
	 	print datetime.datetime.now(),"  SEND: ",self._dest_ip,":", self._dest_port, [datagram]
	 	self._sock.sendto(datagram, (self._dest_ip, self._dest_port))


class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        # socket.sendto(data.upper(), self.client_address)


def SenderTest():
	UDP_IP = "127.0.0.1"
	UDP_PORT = 2323
	MESSAGE = "Hello, World!"

	print "UDP target IP:", UDP_IP
	print "UDP target port:", UDP_PORT
	print "message:", MESSAGE

	udpSender = UdpSender((UDP_IP,UDP_PORT))

	udpSender.send(MESSAGE)

def RecvTest():
	HOST = "127.0.0.1"
	PORT = 2323
	server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
	server.serve_forever()

if __name__ == '__main__':
	# SenderTest()
	RecvTest()
	


