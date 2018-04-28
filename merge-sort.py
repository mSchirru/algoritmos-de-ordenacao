
def merge_sort(lista):
  
  if len(lista) > 1:
    mid = len(lista) // 2
    
    lado_esquerdo = lista[:mid]
    lado_direito = lista[mid:]
    
    merge_sort(lado_esquerdo)
    merge_sort(lado_direito)
  
    i = 0 
    j = 0
    k = 0
    
    while i < len(lado_esquerdo) and j < len(lado_direito):
        if lado_esquerdo[i] < lado_direito[j]:
          lista[k] = lado_esquerdo[i]
          i += 1
        else: 
          lista[k] = lado_direito[j]
          j += 1
        k += 1
    
    while i < len(lado_esquerdo):
      lista[k] = lado_esquerdo[i]
      i += 1
      k += 1
      
    while j < len(lado_direito):
      lista[k] = lado_direito[j]
      j += 1
      k += 1
  print(lista)

lista = [10,5,30,1,2,444,64,80,5,1,444,65,64]

print(merge_sort(lista))
