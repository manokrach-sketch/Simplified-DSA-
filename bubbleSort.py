# For those familiar with DSA you will come across Bubble sort Algorithm.

arr = [2,3,5,8,9,1]

a = len(arr)

for i in range(a):
    for j in range(a-1):
        if arr[j] > arr[j+1]:
            #swap
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)