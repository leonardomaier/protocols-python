
import socket

msg_from_client = "Hello UDP Server"

bytes_to_send = str.encode(msg_from_client)

server_address_port = ("127.0.0.1", 20001)

buffer_size = 1024

udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_client_socket.sendto(bytes_to_send, server_address_port)

msg_from_server = udp_client_socket.recvfrom(buffer_size)

msg = "Message from Server {}".format(msg_from_server[0])

print(msg)
