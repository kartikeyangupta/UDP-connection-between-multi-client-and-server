import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = 'hello'
while msg!='bye':
    msg = input('enter the msg you want to send to the server :')
    datatosend = "CLIENT 3 : "+msg
    sock.sendto(datatosend.encode(),("127.0.0.1",5002))
    data,addr = sock.recvfrom(1024)
    print("message encypted by server :",data.decode())
