# 147. Insertion Sort List (Medium)

Given the `head` of a singly linked list, sort the list using **insertion sort**, and return the sorted list's head.

The steps of the **insertion sort** algorithm:

1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.

2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.

3. It repeats until no input elements remain.


## Example 1:
```
输入: head = [4,2,1,3]
输出: [1,2,3,4]
```

## Example 2:
```
输入: head = [-1,5,3,4,0]
输出: [-1,0,3,4,5]
```