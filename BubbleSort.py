def sort (arr):
    for i in range(len(arr)):
        for j in range (i+1, len(arr)):
            if (arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

array = [13, 4, 2, 7, 0, 19, 5, 2]

sort(array)

for i in array:
    print(i)