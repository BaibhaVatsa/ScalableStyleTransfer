import requests
import socket
import datetime

# Create a TCP server socket
serverSocket = socket.socket();

# Bind the tcp socket to an IP and port
serverSocket.bind(("127.0.0.1", 40404));

# Keep listening
serverSocket.listen();

while(True):
    # Keep accepting connections from clients
    (clientConnection, clientAddress) = serverSocket.accept();

    # Send current server time to the client
    serverTimeNow = "%s"%datetime.datetime.now();
    clientConnection.send(serverTimeNow.encode());
    print("Sent %s to %s"%(serverTimeNow, clientAddress));

    # Close the connection to the client
    clientConnection.close();

def style_transfer():
    r = requests.post(
        "https://api.deepai.org/api/fast-style-transfer",
        data={
            'content': 'https://jooinn.com/images/lotus-flowers-15.jpg',
            'style': 'https://cdn.britannica.com/78/43678-050-F4DC8D93/Starry-Night-canvas-Vincent-van-Gogh-New-1889.jpg',
        },
        headers={'api-key': 'b1c8c62e-1063-40d3-a56d-f5e3256a2237'}
    )
    print(r.json())

#style_transfer()

