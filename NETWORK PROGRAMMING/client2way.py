import socket
host='localhost'
port=12345
m=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
m.connect((host,port))
while True:
      msg=m.recv(1024)
      if not msg:
          break
      print("SERVER-->>:",msg.decode())
      msg=input("CLIENT-->>")
      m.send(msg.encode())
m.close()
