def cont_digitos(n):
   return len(str(n) )

def exibe():
    n = int(input("Numeros: "))
    print(cont_digitos(n), 'digitos')

while True:     
    exibe()        