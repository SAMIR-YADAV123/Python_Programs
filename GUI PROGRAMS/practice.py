import socket
host='localhost'
port=5000
m = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
m.bind((host,port))
m.listen(2)
c,addr = m.accept()

print(" connection from:",str(addr))
c.send(b"connection,how are u")
msg="bye"
c.send(msg.encode())
c.close()
