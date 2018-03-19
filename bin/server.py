import socket
import sys


PORT = 30001
MESSAGE = 'the respberry pi is online'

for i in range(1, len(sys.argv)):
    if sys.argv[i] == '-p':
        PORT = sys.argv[i + 1]
    if sys.argv[i] == '-m':
        MESSAGE = sys.argv[i + 1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(('', PORT))
print 'Listening for broadcast at ', s.getsockname()

while True:
    data, address = s.recvfrom(65535)
    if data.decode('utf-8') == MESSAGE:
        print 'Receive heartbeat from {}'.format(address)
