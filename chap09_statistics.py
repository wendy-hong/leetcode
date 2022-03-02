import math
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

    def selectMedian(self, A, n):  # return the element which has n numbers in A less than itself
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
    # return the element of A, which has n elements in A less than itself
    def arbiSelection(self, A, n):
        med = Median.findMedian(self, A)
        smaller = [item for item in A if item < med]
        larger = [item for item in A if item > med]
        if len(smaller) == n:
            return med
        elif len(smaller) > n:
            return Median.arbiSelection(self, smaller, n)
        else:
            return Median.arbiSelection(self, list(larger), n - len(smaller) - 1)


# Exercise 9.3-6
def kthQuantiles(A, k):
    t = Median()
    if k == 1:
        return []
    elif k % 2:  # odd
        n = len(A)
        left_index = math.ceil((k // 2) * (n / k)) - 1
        right_index = n - left_index - 1
        left = t.selectMedian(A, left_index)
        right = t.selectMedian(A, right_index)
        t.partition(A, left)
        lower = kthQuantiles(A[:left], k // 2)
        t.partition(A, right)
        upper = kthQuantiles(A[right + 1:], k // 2)
        return lower + [left, right] + upper
    else:
        index = t.median_index(len(A))
        median = t.selectMedian(A, index)
        t.partition(A, median)
        return kthQuantiles(A[:index], k // 2) + [median] + kthQuantiles(A[index + 1:], k // 2)


# Exercise 9.3-7
def k_close2median(A, k):
    t = Median()
    med = t.findMedian(A)
    abs_items = []
    result = []
    for element in A:
        abs_items.append(abs(element - med))
    threshold = t.arbiSelection(abs_items, k - 1)
    for i in range(len(A)):
        if abs_items[i] <= threshold:
            result.append(A[i])
    return result


if __name__ == '__main__':
    A = [20, 11, 2, 3, 5, 6, 10]
    # s = select()
    # print(s.randomizedSelect(A, 0, len(A) - 1, 3))
    m = Median()
    print(m.arbiSelection(A, 2))
    # B = [2, 6, 4, 8, 1, 9, 5]
    # print(kthQuantiles(B, 4))
    # print(k_close2median(A, 3))
