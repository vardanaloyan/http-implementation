import socket

target_host = "127.0.0.1"

target_port = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
request = "GET /test/ HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host

print("*"*28)

print(request)

print("*"*28)
client.send(request.encode())

print("*"*28)
while response := client.recv(4096):
    print(response.decode())
print("*"*28)
