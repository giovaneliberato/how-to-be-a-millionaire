

def minimum_swaps(arr):
    """
      Time Complexity: O(n)
      Sapce complexity O(1)
    """
    swaps = 0
    n = len(arr)
    for idx in range(n):
        while arr[idx]-1 != idx:
            ele = arr[idx]
            arr[ele-1], arr[idx] = arr[idx], arr[ele-1]
            swaps += 1
    return swaps
