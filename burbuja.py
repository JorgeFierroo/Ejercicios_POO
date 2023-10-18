arr = [10,2,7,1,25,4,18,5,28]

def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                cum = arr[j]
                arr[j], arr[j+1] = arr[j+1], cum 
                print(arr)
    return arr
            
print(Bubble_sort(arr))