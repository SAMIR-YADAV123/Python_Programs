import  socket

host='localhost'
port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(b"whats name bro",(host,port))
msg="bye"
s.sendto(msg.encode(),(host,port))
s.close()