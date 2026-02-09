#QUESTO SCRIPT VA AVVIATO PER PRIMO
import socket
import pickle
server_socket = socket.socket()
host = '127.0.0.1' #QUESTO E' IL MIO IP LOCALE
try:
    f = open('utenti.dump', 'rb')
    utenti = pickle.load(f)  
except: 
    utenti = {'admin':'èsegreta'}
finally:
    f.close() 
port = 7654 #Questa è la porta che ho settato
server_socket.bind((host, port))
server_socket.listen(1)
for i in range(5):
    conn, addr_p = server_socket.accept() #accept è un medoto
    print(f"Connected by {addr_p}\n") #tupla, quello che è all'interno non è modificabile
    #conn.sendall('Indicami il tuo username'.encode())
    conn.sendall(b'Indicami il tuo username: ') #b sta per bytes #dopo username ho messo lo spazio
    username = conn.recv(1024).decode()
    #print(username)
    conn.sendall(b'Indicami la tua password: ') #b sta per bytes #dopo username ho messo lo spazio
    password = conn.recv(1024).decode()
    #print(password)
    if username == 'admin' : 
        if utenti[username] == password:
            conn.sendall(str(utenti).encode())
        else:
            conn.close()
            continue
    else: 
        utenti[username] = password
     #la chiave è username, e lo collego alla password
    conn.close()
server_socket.close()
#print(utenti)
#for u, p in utenti.items():
#   print(f"Utente {u} password {p}")
f = open('utenti.dump', 'wb')
pickle.dump(utenti, f)
f.close()
