"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # if first element or not in the array
        if x <= arr[0]:
            return arr[0:k]
        if x >= arr[-1]:
            return arr[len(arr)-k:]
        
        pos, found = binarySearch(arr, x)
        
        # Idea is to set lower and upper limit of possible solutions
        # and compare which one is closer to x (lower or upper) and increment the
        # one that is furher away until k elements remain
        # Also need to set lower/upper start based on if element is found or not in the array
        if found:
            start = 0 if pos - k <= 0 else pos - k
            end = len(arr)-1 if pos + k >= len(arr) else pos + k
        else:
            start = 0 if pos - k < 0 else pos - k
            end = len(arr)-1 if pos + k > len(arr) else pos + k - 1
        while True:
            if end - start < k:
                return arr[start:end+1]
            if (x - arr[start]) <= (arr[end] - x):
                end -= 1
            else:
                start += 1
        
        
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid, True     
    return low, False