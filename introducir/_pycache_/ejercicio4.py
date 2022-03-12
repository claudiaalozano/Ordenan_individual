b = import random from randin(0,10)
def busqueda_dicotomica (lista):
  n = len(lista)
  for b in range (n):
    valor = lista[b]
    i = n - 1
    while i>=0:
      if b < lista [i]:
        lista[i+1] = lista[i]
        lista[i]= b
        i = i - 1
      else:
        break
lista = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
