import math


def insertionSort(a):
    for i in range(len(a)):
        index = i - 1
        cur = a[i]
        while index >= 0 and a[index] > cur:
            a[index + 1] = a[index]
            index -= 1
        a[index + 1] = cur
    return a


def selectionSort(a):
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]
    return (a)


def merge(a, p, q, m):  # a[p...q], a[(q+1)...m]
    l = a[p:q + 1]
    r = a[q + 1:m + 1]
    i, j = 0, 0
    for k in range(p, m + 1):
        if i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
        elif i == len(l):
            a[k:m + 1] = r[j:]
            break
        else:
            a[k:m + 1] = l[i:]
            break


def mergeSort(a, p, m):
    if (p < m):
        q = math.floor((p + m) / 2)
        mergeSort(a, p, q)
        mergeSort(a, q + 1, m)
        merge(a, p, q, m)


def binarySearch(a, x):
    n = len(a)
    l, r = 0, n
    # for i in range(n):
    #     if l > r or mid >= n:
    #         return None
    #     if a[mid] == x:
    #         return mid
    #     elif a[mid] < x:
    #         l = mid + 1
    #         mid = (l + r) // 2
    #     else:
    #         r = mid - 1
    #         mid = (l + r) // 2
    while l <= r:
        mid = (l + r) // 2
        if mid < n:
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        else:
            return None
    return None


a = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
# a = [5, 2, 4, 7, 1, 3, 2, 6]
a1 = insertionSort(a)
print('Insertion Sort:', a1)
a2 = selectionSort(a)
print('Selection Sort:', a2)
mergeSort(a, 0, len(a) - 1)
print('Merge Sort:', a)
s = binarySearch(a, a[8])
print(s)
