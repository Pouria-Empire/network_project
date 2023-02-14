
import os,sys,socket,time
import _thread as thread
import requests
import traceback
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
    host = ''               # blank for localhost
    
    print ("Proxy Server Running on ",host,":",port)

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # associate the socket to host and port
        s.bind((host, port))

        # listenning
        # s.listen(BACKLOG)
    
    except (socket.error):
        if s:
            s.close()
        print ("Could not open socket:")
        sys.exit(1)

    # get the connection from client
    while 1:
        # data,ADDR = udpSerSock.recvfrom(BUFSIZE)
        conn, client_addr = s.recvfrom(MAX_DATA_RECV)
        
        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))

    # get the connection from client
    while 1:
        conn, client_addr = s.accept()

        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))
        
    s.close()
#************** END MAIN PROGRAM ***************

def printout(type,request,address):
    if "Block" in type or "Blacklist" in type:
        colornum = 91
    elif "Request" in type:
        colornum = 92
    elif "Reset" in type:
        colornum = 93

    print ("\033[",colornum,"m",address[0],"\t",type,"\t",request,"\033[0m")


def proxy_thread(conn, client_addr):

    # get the request from browser
    request = conn.recv(MAX_DATA_RECV)

    print(request)
    # parse the first line
    first_line = request.split(b'\n')[0]

    # get url
    url = first_line.split(b' ')[1][1:]
    print("\n "+str(first_line))

    printout("Request",first_line,client_addr)

    webserver = url.decode("utf-8")
    port = 80

    try:
        # create a socket to connect to the web server

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((webserver, port))
        a1 = "GET / HTTP/1.1\r\nHost:"+webserver +"\r\n\r\n"
        sock.send(a1.encode('ascii'))
        data = sock.recv(MAX_DATA_RECV)
        conn.send(data)
        # while 1:
        #     # receive data from web server
        #     data = sock.recv(MAX_DATA_RECV)
            
        #     if (len(data) > 0):
        #         # send to browser
        #         conn.send(data)
        #     else:
        #         break
        sock.close()
        conn.close()
    except :
        if sock:
            sock.close()
        if conn:
            conn.close()
        traceback.print_exc()
        printout("Peer Reset",first_line,client_addr)
        sys.exit(1)

#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
    main()

