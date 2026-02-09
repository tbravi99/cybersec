#QUESTO SCRIPT VA AVVIATO PER PRIMO
import socket
server_socket = socket.socket()
host = '127.0.0.1' #QUESTO E' IL MIO IP LOCALE
port = 6364 #Questa è la porta che ho settato
server_socket.bind((host, port))
server_socket.listen(1)
f = open('logfile.txt', 'w')
f.write(f"Server listening on {host} : {port}\n")
richiesta = ''
for i in range(100):
    conn, addr = server_socket.accept() #accept è un medoto
    f.write(f"Connected by {addr}\n")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                richiesta = data.decode()
                if richiesta == 'SHUTDOWN': #qui esce dal ciclo while, ma non dal try
                    break
                else:
                    risposta = f"Ho ricevuto il tuo messaggio: {richiesta}\n"
                    f.write(risposta)
                    conn.sendall(risposta.encode())
        if richiesta == 'SHUTDOWN': #qua esce dal FOR
            break
    finally:
        conn.close()
f.close()
server_socket.close()
