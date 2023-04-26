import socket

# creating the socket
S = socket.socket()
print('Socket Created')

S.bind(('localhost', 9999))
S.listen(3)
print('waiting for connections')

while True:
    c, addr = S.accept()
    name = c.recv(1024).decode()
    print("Connected with address", addr, name)
    c.send(bytes('Welcome to socket programming', 'utf-8'))
    c.close()
