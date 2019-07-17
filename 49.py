import socket
mycon=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mycon.connect(('data.pr4e.org',80))
mycon.send(cmd)
while True:
    data=mycon.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mycon.close()
