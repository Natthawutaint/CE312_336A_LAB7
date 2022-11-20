#EX1
global array
array = array = [1,13,15,17,26,19,15,40,32]
def bubbleSort(array):
    for k in range(len(array)-1,0,-1):
        for i in range(k):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
bubbleSort(array)
print(array)