array = [6, 5, 3, 1, 8, 7, 2, 4]

def ssort(array):
    N = len(array)

    for i in range(N):
        minimum_index = i
        for j in range(i+1, N):
            if array[minimum_index] > array[j]:
                minimum_index = j
        array[minimum_index], array[i] = array[i], array[minimum_index]
    return array
