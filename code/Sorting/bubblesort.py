array = [6, 5, 3, 1, 8, 7, 2, 4]

def bs(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = len(array)
for i in range(n):
    # the -i is to push one item ahead
    # the -1 is to stop list error
    for j in range(0, n-i-1):
        if array[j] > array[j + 1]:
            #swap
