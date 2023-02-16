
import os,sys,socket,time
import _thread as thread
import requests
import traceback
import TLS.clienttls as tls

#********* CONSTANT VARIABLES *********
BACKLOG = 50            # how many pending connections queue will hold
MAX_DATA_RECV = 4096  # max number of bytes we receive at once
DEBUG = True            # set to True to see the debug msgs

def main():

    # check the length of command running
    if (len(sys.argv)<2):
        print ("No port given, using :8080 (http-alt)")
        port = 8080
    else:
        port = int(sys.argv[1]) # port from argument

    # host and port info.
    host = '127.0.0.1'               # blank for localhost
    
    print ("Xclient Server Running on ",host,":",port)

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # associate the socket to host and port
        s.bind((host, port))
    
    except (socket.error):
        if s:
            s.close()
        print ("Could not open socket:")
        sys.exit(1)

    # get the connection from client
    while 1:
        conn, client_addr = s.recvfrom(MAX_DATA_RECV)
        
        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))
        
    s.close()
#************** END MAIN PROGRAM ***************


def proxy_thread(conn, client_addr):

    # get the request from browser
    print(conn)
    
    tls.senMessage(conn)


#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
    main()

