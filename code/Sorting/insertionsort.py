array = [6, 5, 3, 1, 8, 7, 2, 4]

def isort(array):
    N = len(array)
    for i in range(1, N):
        key = array[i]
        previous = i - 1
        while previous >= 0 and key < array[previous]:
            array[previous+1] = array[previous]
            previous -= 1
        array[previous + 1] = key
    return array

print(isort(array))
