# Runs the chat server.
# It accepts clients, handles their messages, and echoes responses.

def handle_client(sock, addr):
    # talk to one client
    # read messages, if type=chat echo back same text
    # if type unknown, send error
    # loop until client disconnects, then close socket
    pass

def main():
    # start server on host/port
    # accept clients in a loop
    # spin off a thread per client with handle_client
    # keep running until stopped with ctrl+c
    pass