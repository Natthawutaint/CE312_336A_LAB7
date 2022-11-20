#EX3
global array
array = array = [1,13,15,17,26,19,15,40,32]

def selectionSort(array):
   for j in range(len(array)-1,0,-1):
       pos=0
       for k in range(1,j+1):
           if array[k]>array[pos]:
               pos = k

       temp = array[j]
       array[j] = array[pos]
       array[pos] = temp


selectionSort(array)
print(array)