def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Si x es mayor, ignora la mitad izquierda
        if arr[mid] < x:
            low = mid + 1

        # Si x es menor, ignora la mitad derecha
        elif arr[mid] > x:
            high = mid - 1

        # x está presente en el medio
        else:
            return mid

    # x no está en la lista
    return -1


# Test array
arr = [1,2,3,4,5,6,7,8,9,9,10,11,12,13,14,15,16,17,18,19,20]
x = 7
print(binary_search(arr,x))