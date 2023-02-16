#!/bin/bash
echo "Enter your message"
read message
echo "Enter destination port"
read port

echo -n "say: $message, to: $port" | nc -4u -w0 127.0.0.1 8080
echo "message sent"

netcat -ul 8081

exit 0