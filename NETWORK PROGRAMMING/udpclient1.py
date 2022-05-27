import  socket

host='localhost'
port=5000

m=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
m.bind((host,port))


while True:
    msg, addr = m.recvfrom(1024)
    if not msg:
        break
    print("recieved:",msg.decode())

m.close()