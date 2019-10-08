import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("127.0.0.1",5002)
sock.bind(address)
data=''
while data!='bye':
    data,addr = sock.recvfrom(1024)
    print(data.decode())
    data = data.decode()
    d1,d2 = data.split(': ')
    data = d2
    if data=='bye':
        sock.sendto('good bye my friend'.encode(),addr)
    else:
        sock.sendto(data[::-1].encode(),addr)
