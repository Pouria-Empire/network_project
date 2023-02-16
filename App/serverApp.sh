#!/bin/bash
echo "Enter port to listen"
read portL
echo "Enter Message to Reply"
read Message
netcat -ul $portL
echo -n $Message | nc -4u -w0 127.0.0.1 $portL+1
# while true;
# do
#     netcat -ul $portL
# done
exit 0