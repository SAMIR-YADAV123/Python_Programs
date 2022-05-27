import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='localhost'
port=12345
s.bind((host,port))
s.listen(5)
t,addr = s.accept()
print("Connection from:"+str(addr))
while True:
    msg=input("SERVER-->>:")
    t.send(msg.encode())
    msg=t.recv(1024)
    if not msg:
        break
    print("CLIENT-->>",msg.decode())
s.close()