import socket
c = socket.socket()
c.connect(('localhost', 9999))
name = input("Enter the name:")
c.send(bytes(name, 'utf-8'))
