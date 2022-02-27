import random
import argparse

parser = argparse.ArgumentParser(description='sort')
parser.add_argument('-method', type=int, default=0)
args = parser.parse_args()


class sort(object):
    def __init__(self):
        print('sort')

    def insertionSort(self, a):
        for i in range(len(a)):
            index = i - 1
            cur = a[i]
            while index >= 0 and a[index] > cur:
                a[index + 1] = a[index]
                index -= 1
            a[index + 1] = cur
        return a

    def selectionSort(self, a):
        for i in range(len(a) - 1):
            min_index = i
            for j in range(i + 1, len(a)):
                if a[j] < a[min_index]:
                    min_index = j
            if i != min_index:
                a[i], a[min_index] = a[min_index], a[i]
        return (a)

    def BubbleSort(self, a):
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a


class mergesort(object):
    def __init__(self):
        print('merge sort')

    def merge(self, a, p, q, m):  # a[p...q], a[(q+1)...m]
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

    def mergeSort(self, a, p, m):
        if (p < m):
            q = (p + m) // 2
            mergesort.mergeSort(self, a, p, q)
            mergesort.mergeSort(self, a, q + 1, m)
            mergesort.merge(self, a, p, q, m)

    # Exercise 2.3-7
    # Given a theta(nlgn) time algorithm for determining whether there exist two elements in a set S whose sum is exactly value x.
    def checkSum(self, a, x):
        mergesort.mergeSort(self, a, 0, len(a) - 1)
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
class inversion(object):
    def __init__(self):
        print('inversion num')

    def inversions(self, a, p, q, m):  # a[p...q], a[(q+1)...m]
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

    def inversionNum(self, a, p, m):
        num = 0
        if (p < m):
            q = (p + m) // 2
            num += inversion.inversionNum(self, a, p, q)
            num += inversion.inversionNum(self, a, q + 1, m)
            num += inversion.inversions(self, a, p, q, m)
        return num


class quicksort(object):
    def __init__(self):
        print('quick sort')

    def partition(self, a, p, r):
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

    def randomizedPartition(self, a, p, r):
        i = random.randint(p, r)
        a[i], a[r] = a[r], a[i]
        return quicksort.partition(self, a, p, r)

    def quickSort(self, a, p, r):
        if p < r:
            q = quicksort.partition(self, a, p, r)
            quicksort.quickSort(self, a, p, q - 1)
            quicksort.quickSort(self, a, q + 1, r)


class linearsort(object):
    def __init__(self):
        print('linear sort')

    def countingSort(self, a):
        c = [0 for _ in range(max(a) + 1)]
        b = [0 for _ in range(len(a))]
        # c[i] contains the number of elements equal to i
        for e in a:
            c[e] += 1
        # c[i] contains the number of elements less than or equal to i
        for i in range(1, max(a) + 1):
            c[i] = c[i] + c[i - 1]
        j = len(a) - 1
        while j >= 0:
            b[c[a[j]] - 1] = a[j]
            c[a[j]] = c[a[j]] - 1
            j = j - 1
        return b

    def bucketSort(self, a):
        n = len(a)
        tmp = max(a) + 1
        a = [a[i] / tmp for i in range(n)]
        b = [[] for _ in range(n)]
        for i in range(n):
            t = int(n * a[i])
            b[t].append(a[i])
        ans = []
        for i in range(n):
            sort.insertionSort(self, b[i])
            ans = ans + b[i]
        ans = [int(ans[i] * tmp) for i in range(n)]
        return ans


A = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
A1 = [2, 5, 3, 0, 2, 3, 0, 3]
sort1 = sort()
sort2 = mergesort()
sort3 = quicksort()
sort4 = linearsort()
# sort2.mergeSort(A, 0, len(A) - 1)
# sort3.quickSort(A, 0, len(A) - 1)
print(sort4.bucketSort(A1))
