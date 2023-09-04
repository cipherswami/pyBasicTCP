######################################################
# Author: Aravind Potluri <aravindswami135@gmail.com>
# Description:  Basic python TCP Server that echos 
#               back captilized text.           
######################################################

# Macros
serverIP = "0.0.0.0"    # Accept from any IP.
serverPORT = 8080       # Server Port   

# Importing Libraries
import socket

# Creating socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
    print("[+] Socket successfully created")
except:
    print(f"[-] Socket creation failed")
    sock.close()
    exit()

# Binding socket and listening for connection
try:
    sock.bind((serverIP, serverPORT))
    print(f"[+] socket successfully binded on port {serverPORT}")
except:
    print(f"[-] Socket binding failed")	
    sock.close()
    exit()

# Establishing the connection
try:
    sock.listen(2)
    print("[+] wating for connection...")
    clientSock, clientAddr = sock.accept()
    print(f"[+] Accepted connection from : {clientAddr}\n")
except:
    print("[-] Connection establishment faild")
    sock.close()
    exit()

while True:
    try:
        # Receive data from any client
        data = clientSock.recv(1024) # Assuming MAX data to be received is 1024 Bytes.
        if len(data) == 0:
            raise socket.error # To escape the infinte loop, after breaking the tcp pipeline
        msg = data.decode('UTF-8')
        print(f"[#] Received message: {msg}")

        # Data processing
        msg = msg.upper()

        # Echoing back the captilized msg to client
        clientSock.send(msg.encode('UTF-8'))
        print(f"[#] Sent Response: {msg}\n")

    except KeyboardInterrupt:
        print(" [!] Server shutting down.")
        break

    except socket.error:
        print("[!] Connection closed by client")
        break

    except Exception as err:
        print(f"[!] {str(err)}")
        break

# Close the server socket
sock.close()
