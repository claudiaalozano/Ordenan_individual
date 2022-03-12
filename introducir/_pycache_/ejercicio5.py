def ordenar_topologica (lista):
  a = len (valores) - 1
  for i in range (0 , a):
    for j in range(0 , a):
      if lista[j] > lista[j + 1]:
        b = lista[j]
        lista[j]= lista [j +1]
        lista [j + 1]= b
  return
print ("Lista inicial: " , valores )
print ("Lista ordenada: " , ordenar_topologica(valores))

valores = [1 , 20 , 13 , 5 , 9 , 1 , 1 , 13 , 20 , 9 , 5]