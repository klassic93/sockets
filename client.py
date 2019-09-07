import socket

# create new socket for server
client_sock = socket.socket()

# get connection to server socket
# we remember host and port our server socket
client_sock.connect(('127.0.0.1', 9090))

# send data to server
# into python3 we can use only byte type (not str)
client_sock.send(b'Some string. Its have to return on upper')

# read data
# expect 'SOME' because can get only 4 bytes
data = client_sock.recv(4)

# close connection
client_sock.close()

# output returned data
print(data)
