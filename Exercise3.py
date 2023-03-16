#Un esempio di snippet in Python che decodifica una stringa in base 64:
#from base64 import b64decode
#s = 'aGVubG8gOik='
#print(b64decode(s))

from base64 import b64decode
#n Python per convertire un oggetto bytes in un oggetto int è conveniente utilizzare la funzione int.from_bytes(b, endianness), ove b è il nostro oggetto bytes, mentre endianness è una stringa 'big' oppure 'little' che sta ad indicare in che ordine devono essere letti i byte di b: rispettivamente da sinistra verso destra e viceversa.
z = 664813035583918006462745898431981286737635929725
primo = b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=")
#non so secondo quale base ci andava il 20 ho solo provato finchè non uscivano più 0x00/
secondo= z.to_bytes(20, 'big')#Per convertire un intero z in bytes puoi usare invece la funzione (z).to_bytes(n, endianness): n indica il numero di bytes da utilizzare per la conversione, seguendo l'ordine dato da endianness.
#al posto di 'big' ci potrebbe stare 'little' dipende dalla grandezza del byte
print(primo + secondo)

