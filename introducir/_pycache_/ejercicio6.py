def ordenar(a,b):
  step = int (input("Introduce el salto entre elementos que desea: "))
  start = 0
  end = 13
  a = lista[start:end]
  b = a.sort()
  print (b)
  

lista = [5 , 7 , 12 , 6 , 18 , 13 , 9 , 10 , 16 , 21 , 19 , 8 , 20 , 3]

if __name__ == "__main__":
    ordenar()