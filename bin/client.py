import socket
import sys
import time


PORT = 30001
MESSAGE = 'the respberry pi is online'

for i in range(1, len(sys.argv)):
    if sys.argv[i] == '-p':
        PORT = sys.argv[i + 1]
    if sys.argv[i] == '-m':
        MESSAGE = sys.argv[i + 1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

network = '<broadcast>'
while True:
    try:
        s.sendto(MESSAGE.encode('utf-8'), (network, PORT))
    except:
        pass
    finally:
        time.sleep(2)
