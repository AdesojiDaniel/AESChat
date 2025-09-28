# This handles all socket I/O details.
# It connects, listens, and sends/receives JSON messages with length framing.

def connect(host, port):
    # Make a TCP client connection and return the socket.
    pass

def bind_and_listen(host, port):
    # Create a server socket bound to host/port and start listening.
    pass

def send_json(sock, object):
    # Turn object into json bytes.
    # Prefix with 4-byte length
    # Send over sock
    pass

def recv_json(sock):
    # Read length header, then json bytes, decode back into a dict
    pass

def _recv_exact(sock, n):
    # Helper: Read  n bytes from sock or raise error if disconnected
    pass
