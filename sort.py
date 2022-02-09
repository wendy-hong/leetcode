import random


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


def BubbleSort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


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
        q = (p + m) // 2
        mergeSort(a, p, q)
        mergeSort(a, q + 1, m)
        merge(a, p, q, m)


# Exercise 2.3-5
def binarySearch(a, x):
    n = len(a)
    l, r = 0, n
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


# Exercise 2.3-7
# Given a theta(nlgn) time algorithm for determining whether there exist two elements in a set S whose sum is exactly value x.
def checkSum(a, x):
    mergeSort(a, 0, len(a) - 1)
    # for i in range(len(a)):
    #     if binarySearch(a, x - a[i]):
    #         return [a[i], x - a[i]]
    i, j = 0, len(a) - 1
    while i < j:
        if a[i] + a[j] == x:
            return [a[i], a[j]]
        elif a[i] + a[j] < x:
            i += 1
        else:
            j -= 1
    return None


# Problem 2-4
# Give an algorithm that determines the number of inversions in any permutation on n elements in Θ(nlgn) worst-case time.
def inversions(a, p, q, m):  # a[p...q], a[(q+1)...m]
    l = a[p:q + 1]
    r = a[q + 1:m + 1]
    i, j = 0, 0
    num = 0
    for k in range(p, m + 1):
        if i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
                num += (len(l) - i)
        elif i == len(l):
            a[k:m + 1] = r[j:]
            break
        else:
            a[k:m + 1] = l[i:]
            break
    return num


def inversionNum(a, p, m):
    num = 0
    if (p < m):
        q = (p + m) // 2
        num += inversionNum(a, p, q)
        num += inversionNum(a, q + 1, m)
        num += inversions(a, p, q, m)
    return num


def partition(a, p, r):
    x = a[r]
    i = p - 1
    count = 0
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
        if a[j] == x:
            count += 1
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1 - count // 2


def randomizedPartition(a, p, r):
    i = random.randint(p, r)
    a[i], a[r] = a[r], a[i]
    return partition(a, p, r)


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q - 1)
        quickSort(a, q + 1, r)


A = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
# insertionSort(A)
# print('Insertion Sort:', A)
# selectionSort(A)
# print('Selection Sort:', A)
mergeSort(A, 0, len(A) - 1)
print('Merge Sort:', A)
s = binarySearch(A, A[8])
print('Binary Search:', s)
A = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
print(checkSum(A, 10))
Inverse = [2, 3, 8, 6, 1]
print(inversionNum(Inverse, 0, len(Inverse) - 1))
A = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70, 55]
quickSort(A, 0, len(A) - 1)
print('Quick Sort:', A)
