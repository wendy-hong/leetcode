from leetcode.sort2 import quicksort


def findMinMax(A):
    n = len(A)
    if n % 2 == 0:  # 偶数
        if A[0] > A[1]:
            Min, Max = A[1], A[0]
        else:
            Min, Max = A[0], A[1]
        for i in range(1, n // 2):
            if A[2 * i] < A[2 * i + 1]:
                Min = min(A[2 * i], Min)
                Max = max(A[2 * i + 1], Max)
            else:
                Min = min(A[2 * i + 1], Min)
                Max = max(A[2 * i], Max)
    else:
        Min, Max = A[0], A[0]
        for i in range(1, (n + 1) // 2):
            if A[2 * i - 1] < A[2 * i]:
                Min = min(A[2 * i - 1], Min)
                Max = max(A[2 * i], Max)
            else:
                Min = min(A[2 * i], Min)
                Max = max(A[2 * i - 1], Max)
    return Min, Max


class select(object):
    def __init__(self):
        print('Randomized Select')

    def randomizedSelect(self, A, p, r, i):  # return the ith smallest element in A[p...r]
        if p == r:
            return A[p]
        t = quicksort()
        q = t.randomizedPartition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            return select.randomizedSelect(self, A, p, q - 1, i)
        else:
            return select.randomizedSelect(self, A, q + 1, r, i - k)


class Median(object):
    def __init__(self):
        print('Median')

    def median_index(self, n):
        if n % 2:
            return n // 2
        else:
            return n // 2 - 1

    def partition(self, A, ele):  # return the number of elements less than ele
        i = 0
        for j in range(len(A) - 1):
            if A[j] == ele:
                A[j], A[-1] = A[-1], A[j]
            if A[j] < ele:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[-1] = A[-1], A[i]  # ele is always at the end of the array
        return i

    def selectMedian(self, A, n):  # n is the index of the median of sorted A
        if len(A) <= 1:
            return A[0]
        medians = []
        # find medians of n/5 groups
        for i in range(0, len(A), 5):
            group = sorted(A[i:i + 5])
            A[i:i + 5] = group
            median = group[Median.median_index(self, len(group))]
            medians.append(median)
        # find the median of n/5 medians
        pivot = Median.selectMedian(self, medians, Median.median_index(self, len(medians)))
        # the number of elements less than the median
        index = Median.partition(self, A, pivot)
        if n == index:
            return A[index]
        elif n < index:
            return Median.selectMedian(self, A[:index], n)
        else:
            return Median.selectMedian(self, A[index + 1:], n - index - 1)

    def findMedian(self, A):
        return Median.selectMedian(self, A[:], Median.median_index(self, len(A)))


# Exercise 9.3-5
def arbiSelection(A, n):  # return the element of A, which has n elements in A less than itself
    m = Median()
    med = m.findMedian(A)
    smaller = [item for item in A if item < med]
    larger = [item for item in A if item > med]
    if len(smaller) == n:
        return med
    elif len(smaller) > n:
        return arbiSelection(smaller, n)
    else:
        return arbiSelection(list(larger), n - len(smaller) - 1)


if __name__ == '__main__':
    A = [10, 22, 34, 3, 32, 82]
    s = select()
    print(s.randomizedSelect(A, 0, len(A) - 1, 3))
    print(arbiSelection(A, 3))
