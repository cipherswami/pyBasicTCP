######################################################
# Author: Aravind Potluri <aravindswami135@gmail.com>
# Description:  Basic python TCP Client that sends 
#               user I/P to server and recevies the 
#               response.           
###################################################### 

# Macros
serverIP = "127.0.0.1"
serverPORT = 8080

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

# Connecting to the server
try:
    sock.connect((serverIP, serverPORT))
    print("[+] Successfully connected to server")
except:
    print("[-] Connection failed")
    sock.close()
    exit()

# Sending the data
while True:
    try:
        # Sending the user input to server
        sock.send(input("\n[#] Enter the msg: ").encode('UTF-8'))

        # Receive the response from server
        data = sock.recv(1024) # Assuming MAX data to be received is 1024 Bytes.
        if len(data) == 0:
            raise socket.error # Broken pipe error
        print(f"[#] Response from server: {data.decode('UTF-8')}")

    except KeyboardInterrupt:
        print(" [!] Client shutting down.")
        break

    except socket.error:
        print("[!] Connection closed by server")
        break

    except Exception as err:
        print(f"[!] {str(err)}")
        break

# Close the server socket
sock.close()
