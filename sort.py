noc = 0
nos = 0


# Bubble Sort
def bubble_sort(arr):
    noc = 0  # num of comparison
    nos = 0  # num of swapping
    n = len(arr)
    for i in range(n):
        for j in range(i, n - 1):
            noc += 1
            if arr[j - 1] > arr[j]:
                nos += 1
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print_stat(noc, nos)
    return arr


# Selection Sort
def selection_sort(arr):
    noc = 0  # num of comparison
    nos = 0  # num of swapping
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            noc += 1
            if arr[i] > arr[j]:
                nos += 1
                arr[i], arr[j] = arr[j], arr[i]
    print_stat(noc, nos)
    return arr


# Insertion Sort
def insertion_sort(arr):
    noc = 0  # num of comparison
    nos = 0  # num of swapping
    n = len(arr)
    for i in range(n - 1):
        noc += 1
        if arr[i] > arr[i + 1]:
            for j in range(i):
                noc += 1
                if arr[i + 1] < arr[j]:
                    nos += 1
                    arr[i + 1], arr[j] = arr[j], arr[i + 1]
    print_stat(noc, nos)
    return arr


# Shell Sort
def shell_sort(arr):
    noc = 0  # num of comparison
    nos = 0  # num of swapping
    n = len(arr)
    gap = round(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            noc += 1
            # Compare with the number in same column : j-gap
            while (j >= gap and arr[j - gap] > temp):
                nos += 1
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = round(gap / 2)
    print_stat(noc, nos)
    return arr


# Merge Sort
# Part One: seperate
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    half = round(n/2)
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge(left, right)


# Part Two: Sort & Merge
def merge(left, right):
    global noc
    sorted_result = []
    l_index=0
    r_index=0
    while l_index<len(left) and r_index<len(right):
        noc += 1
        if left[l_index] < right[r_index]:
            sorted_result.append(left[l_index])
            l_index += 1
        else:
            sorted_result.append(right[r_index])
            r_index += 1
    # add all left
    sorted_result += left[l_index:]
    sorted_result += right[r_index:]
    return sorted_result


# Quick Sort
# Divide and Conquer
def quick_sort(arr, left, right):
    global noc
    global nos
    # return arr if the size of it is 1
    if left>=right:
        return arr
    # the pivot was selected as the rightmost element
    pivot = arr[right]
    l_index = left
    r_index = right
    storeIndex = left
    for i in range(left, right):
        noc += 1
        if arr[i] <= pivot:
            if i != storeIndex:
                nos +=1
                arr[storeIndex], arr[i] = arr[i], arr[storeIndex]
            storeIndex += 1
    # now all the element in range of [storeIndex, right-1] are greater than pivot
    arr[right], arr[storeIndex] = arr[storeIndex], arr[right]
    # now the storeIndex is the loc of pivot
    quick_sort(arr, left, storeIndex-1)
    quick_sort(arr, storeIndex+1, right)
    return arr


# Heap Sort
def heap_sort(arr):
    n = len(arr)
    first = int(n/2-1)
    for start in range(first,-1,-1):
        max_heapify(arr,start,n-1)
    for end in range(n-1,0,-1):
        arr[end],arr[0] = arr[0],arr[end]
        max_heapify(arr,0,end-1)
    return arr


def max_heapify(arr,start,end):
    global noc
    global nos
    root = start
    while True:
        child = root*2 +1
        noc += 1
        if child > end : break
        noc += 1
        if child+1 <= end and arr[child] < arr[child+1] :
            child = child+1
        noc+=1
        if arr[root] < arr[child] :
            nos += 1
            arr[root],arr[child] = arr[child],arr[root]
            root = child
        else :
            break


def print_stat(noc, nos):
    if nos != -1:
        print("\tnum. of comparison done : " + str(noc) + "\n\tnum. of swapping done : " + str(nos))
    else:
        print("\tnum. of comparison done : " + str(noc))


array = [11, 1, 13, 3, 2, 6, 10, 5, 7, 14, 4, 9, 12, 0, 8]

print("The length of array to sorted is : " + str(len(array)) + "\n")

print("\nNo.1 Bubble Sort:")
b = bubble_sort(array.copy())
print(str(array) + " \n\t>> " + str(b))

print("\nNo.2 Selection Sort:")
c = selection_sort(array.copy())
print(str(array) + " \n\t>> " + str(c))

print("\nNo.3 Insertion Sort:")
d = insertion_sort(array.copy())
print(str(array) + " \n\t>> " + str(d))

print("\nNo.4 Shell Sort:")
e = shell_sort(array.copy())
print(str(array) + " \n\t>> " + str(e))

print("\nNo.5 Merge Sort:")
f = merge_sort(array.copy())
print_stat(noc, -1)
noc = 0
nos = 0
print(str(array) + " \n\t>> " + str(f))

print("\nNo.6 Quick Sort:")
f = quick_sort(array.copy(),0,len(array)-1)
print_stat(noc, nos)
print(str(array) + " \n\t>> " + str(f))
noc = 0
nos = 0

print("\nNo.7 Heap Sort:")
f = heap_sort(array.copy())
print_stat(noc, nos)
print(str(array) + " \n\t>> " + str(f))
