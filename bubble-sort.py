
def bubble_sort(lista):
  elementos =  len(lista)-1
  flag = False
  While not flag:
    flag = True
    for i in range(elementos):
      if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        flag = False
        print(lista)
        
  return lista

lista = [4,6,2,1,6,76,543,234,645,9,1,0]
print(bubble_sort(lista))
