from socket import socket
import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
  def handle(self) -> None:
    self.data = self.request.recv(1024).strip()

    print("{} sent:".format(self.client_address[0]))

    print(self.data)

    self.request.sendall("ACK from TCP Server".encode())


if __name__ == "__main__":

  HOST, PORT = "localhost", 9999

  tcp_server = socketserver.TCPServer((HOST, PORT), TCPHandler)

  tcp_server.serve_forever()