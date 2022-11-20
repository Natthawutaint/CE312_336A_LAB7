#EX2
global array
array = array = [1,13,15,17,26,19,15,40,32]

def insertionSort(array):
   for index in range(1,len(array)):
     arrayi = array[index]
     i = index
     while i>0 and array[i-1]>arrayi:
         arrayi=array[i-1]
         pos = i-1
     array[i]=arrayi

insertionSort(array)
print(array)