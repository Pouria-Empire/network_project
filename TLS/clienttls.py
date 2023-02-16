from socket import create_connection,socket,AF_INET,SOCK_DGRAM
from ssl import SSLContext, PROTOCOL_TLS_CLIENT

def senMessage(message):
    hostname='localhost'
    ip = '127.0.0.1'
    port = 8442
    context = SSLContext(PROTOCOL_TLS_CLIENT) #initializing tls connection
    context.load_verify_locations('./TLS/new.pem')  #verifing

    with create_connection((ip, port)) as client:
        with context.wrap_socket(client, server_hostname=hostname) as tls:
            print(f'Using {tls.version()}\n')
            tls.sendall(message)    # send message

            data = tls.recv(1024)   #recieve reply from client
            data2 = tls.recv(1024)   #recieve reply from client
            print(f'Server says: {data} {data2}')   

            udpServerAppSock = socket(AF_INET,SOCK_DGRAM)
            udpServerAppSock.sendto(data,(ip,8081)) # Send back response to client