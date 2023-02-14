import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.pouriaarefi.ir", 80))
sock.send(b"GET / HTTP/1.1\r\nHost:www.pouriaarefi.ir\r\n\r\n")
# sock.send(b'GET /pouria.png HTTP/1.1\r\nHost: www.pouriaarefi.ir\r\nConnection: keep-alive\r\nsec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"\r\nsec-ch-ua-mobile: ?0\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36\r\nsec-ch-ua-platform: "Linux"\r\nAccept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Mode: no-cors\r\nSec-Fetch-Dest: image\r\n\n')
response = sock.recv(4096)
sock.close()
print(response.decode())