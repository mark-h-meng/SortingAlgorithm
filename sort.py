
# Bubble Sort
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n - 1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


# Selection Sort
def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Insertion Sort
def InsertionSort(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            for j in range(i):
                if arr[i+1]<arr[j]:
                    arr[i+1], arr[j] = arr[j], arr[i+1]
    return arr


ary = [1, 3, 2, 6, 5, 7, 4, 9, 0, 8]
b = BubbleSort(ary)
c = SelectionSort(ary)
d = InsertionSort(ary)
print(str(b) + "\n")
print(str(c) + "\n")
print(str(d) + "\n")
