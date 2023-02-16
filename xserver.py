
import os,sys,socket,time
import _thread as thread
import requests
import traceback
import TLS.servertls as tls
#********* CONSTANT VARIABLES *********
BACKLOG = 50            # how many pending connections queue will hold
MAX_DATA_RECV = 4096  # max number of bytes we receive at once
DEBUG = True            # set to True to see the debug msgs

def main():
    tls.runTLSServer()


#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
    main()

