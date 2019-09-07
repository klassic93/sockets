import socket

# create new socket for server
sock = socket.socket()

# set params for socket
# the first - host, the second - port
sock.bind(('', 9090))

# set quantity connections
# If backlog is specified, it must be
# at least 0 (if it is lower, it is set to 0);
sock.listen(1)

# return connection and client address
conn, addr = sock.accept()

# runserver
while True:
    """
    Here we can get some data. And we can get them
    as match as we want. But we don`t know how many data
    send us client because we will split them into 1024 bytes (1kb)
    If data is over exit the loop
    """
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

# close connection
conn.close()
