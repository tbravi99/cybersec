#import sys
#nomefile = 'esempio.txt' #qui ho provato a nominare il nome direttmente E FUNZIONA
nomefile= "logfile.txt"
try:
    f = open(nomefile, "r", encoding="utf-8") #QUI HO DOVUTO AGGIUNGERE UTF-8 PER UNA CORRETTA INTERPRETAZIONE DEI CARATTERI
    righe = f.readlines()
    for riga in righe:
        print(riga, end='') #VA A CAPO SOLO DI UNO
    
except FileNotFoundError as e:#GESTIONE DELLE SPECIFICO MESSAGGIO DI ERRORE
    print(f"[-] errore bloccante: {str(e)}")
#GESTIONE ERRORI CON TRY
#EXCEPT
#LETTURA DI UN FILE DI TESTO FORZANDO L'ECODING 
#LETTURA DI TUTTE LE RIGHE IN UNA LISTA
#EVITARE LA STAMPA DEL NEW-LINE IMPLICITA NELLA PRINT
#UTILIZZO DELL' ARGV PER ACCETTARE I PARAMETRI DALLA LINEA COMANDO 
