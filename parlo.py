import socket
s = socket.socket()
indirizzo = '127.0.0.1' #QUI VA MESSO L'IP DEL COMPAGNO
porta = 7654
s.connect((indirizzo, porta))
prompt = s.recv(1024)
username = input(prompt.decode())
s.sendall(username.encode()) #per inviare lo username ad ascolto0.py
prompt = s.recv(1024)
password = input(prompt.decode())
s.sendall(password.encode())
if username == 'admin':
    prompt=s.recv(1024)
    print(prompt.decode())
s.close()
