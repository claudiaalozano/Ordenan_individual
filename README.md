# Ordenan_individual

##Ejercicio 4: Ordenación por inserción dicotómica:
Para este ejercicio he empleado el siguiente código:

```b = import random from randin(0,10)
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

if __name__ == "__main__":
  busqueda_dicotomica()
```


##Ejercicio 5: Ordenación topológica:
Para este ejercicio he empleado el siguiente código:

```def ordenar_topologica (lista):
  a = len (valores) - 1
  for i in range (0 , a):
    for j in range(0 , a):
      if lista[j] > lista[j + 1]:
        b = lista[j]
        lista[j]= lista [j +1]
        lista [j + 1]= b
  return
print ("Lista inicial: ")
print("\n".join(map(str , valores)))
print ("Lista ordenada: " )
print("\n".join(map(str , ordenar_topologica(valores))))
valores = [1 , 20 , 13 , 5 , 9 , 1 , 1 , 13 , 20 , 9 , 5]

if __name__ == "__main__":
  ordenar_topologica()
```



##Ejercicio 6: Especificación de está_explorado
Para este ejercicio he empleado el siguiente código:

```def ordenar(a,b):
  step = int (input("Introduce el salto entre elementos que desea: "))
  start = 0
  end = 13
  a = lista[start:end]
  b = a.sort()
  print (b)
  

lista = [5 , 7 , 12 , 6 , 18 , 13 , 9 , 10 , 16 , 21 , 19 , 8 , 20 , 3]

if __name__ == "__main__":
    ordenar()
```
