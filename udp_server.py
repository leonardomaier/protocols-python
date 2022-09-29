import socket

LOCAL_IP, LOCAL_PORT, BUFFER_SIZE = '127.0.0.1', 20001, 1024

msg_from_server = "Hello World UDP Client"

bytes_to_send = msg_from_server.encode()

udp_server_socket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_server_socket.bind((LOCAL_IP, LOCAL_PORT))

print('udp server up and running')

while True:

    bytes_address_pair = udp_server_socket.recvfrom(BUFFER_SIZE)

    message = bytes_address_pair[0]

    address = bytes_address_pair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    udp_server_socket.sendto(bytes_to_send, address)
