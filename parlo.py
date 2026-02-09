#SI FA PARTIRE PER SECONDO
import socket
import sys
messaggio = sys.argv[1]
s = socket.socket()
s.settimeout(20)
indirizzo = '127.0.0.1' #QUI VA MESSO L'IP DEL COMPAGNO
porta = 6364
s.connect((indirizzo, porta))
s.sendall(messaggio.encode())
risposta = s.recv(1024)
print(risposta.decode())
s.close()
