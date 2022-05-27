import  socket
host = 'localhost'
port=5000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
msg= s.recv(1024)
print("recieved :"+msg.decode())
msg=s.recv(1024)
print("recieved :"+msg.decode())
print()
s.close()