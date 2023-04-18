import socketserver
import pickle

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ip = self.client_address[0]
        d = pickle.loads(self.request[0][4:]) #préfixe ignoré
        print(f"{ip}\t{d['asctime']}_"f"{d['name']}_{d['levelname']} - {d['msg']}")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9696
    with socketserver.UDPServer((HOST, PORT), MyHandler) as srv:
        srv.serve_forever()