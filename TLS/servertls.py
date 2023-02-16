from socket import socket, AF_INET, SOCK_STREAM,SOCK_DGRAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER
MAX_DATA_RECV = 4096

ip = '127.0.0.1'
port = 8442
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain('./TLS/new.pem', './TLS/private.key') #load tls connection

def runTLSServer():
    global ip,port,context
    #create socket and listening on
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(1)

        with context.wrap_socket(server, server_side=True) as tls:
            connection, address = tls.accept()  # waiting for connection
            print(f'Connected by {address}\n')

            data = connection.recv(1024) #recieve data
            print(f'Client Says: {data}')

            (message,destPort) = [x.split(": ")[1] for x in data.decode('utf-8').split(",")] # get message and port from tunnel

            # create socket for sending back the result
            udpServerAppSock = socket(AF_INET,SOCK_DGRAM)
            udpServerAppSock.sendto(message.encode('ascii'),(ip,int(destPort))) # Send udp message
            print("...waiting for response of server app...")

            # recieve response and print it
            recv_data,(ip,destPort) = udpServerAppSock.recvfrom(MAX_DATA_RECV)

            # just for applications without response
            if recv_data is not None:
                connection.sendall(recv_data) 
            else:
                connection.sendall(b'Message sent without response')