s = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d" #stringa 
flag = bytes.fromhex(s) #la funzione bytes.fromhex(s) restituisce l'oggetto bytes che corrisponde alla stringa esadecimale s.
print(flag)
string = flag.hex()# metodo .hex() è possibile ottenere la corrispondente stringa esadecimale
print(string)