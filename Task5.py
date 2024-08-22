# Create a basic text-based chat application in Python where two users can exchange messages in real-time using the command line.
# Implement a simple client-server model for message exchange.
import socket
import threading


# Function to handle the server side
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = '127.0.0.1'  # localhost
    port = 12345  # Reserve a port for the service.

    # Bind to the port
    server_socket.bind((host, port))

    # Start listening for incoming connections (max 1 connection)
    server_socket.listen(1)
    print("Server started! Waiting for a connection...")

    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")

    while True:
        # Receive data from the client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Client: {message}")

        # Get input from server user
        response = input("You (Server): ")
        # Send the response to the client
        client_socket.send(response.encode('utf-8'))

    # Close the connection
    client_socket.close()


# Function to handle the client side
def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = '127.0.0.1'  # localhost
    port = 12345  # The same port as the server

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    while True:
        # Get input from client user
        message = input("You (Client): ")
        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

        # Receive response from the server
        response = client_socket.recv(1024).decode('utf-8')
        if not response:
            break
        print(f"Server: {response}")

    # Close the connection
    client_socket.close()


# Main function to choose between server and client
if __name__ == "__main__":
    choice = input("Do you want to start the server or the client? (server/client): ").strip().lower()

    if choice == 'server':
        start_server()
    elif choice == 'client':
        start_client()
    else:
        print("Invalid choice! Please choose either 'server' or 'client'.")
