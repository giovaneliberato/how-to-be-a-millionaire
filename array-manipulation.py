
'''
0, 0, 0, 0
0, 1, 0, -1
0, 3, 0, -3
0, 6, 0, -6
'''

'''
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each of the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in the array.
'''
def solution(n, queries):
    # Time: O(q + n)
    # Space: O(n) 
    array = [0]*(n+2)
    for start, end, value in queries:
        array[start] += value
        array[end + 1] += -value
    
    max_value = array[1]
    current_value = array[1]

    for value in array[2:]:
        current_value += value

        max_value = max(max_value, current_value)
    
    return max_value
    
'''
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
0, 1, 9, 16, 16, 31, 24, 16, 1, 0, 0, 0
'''


assert solution(10, [[1, 5, 3], [4, 8, 7], [6, 10, 1]]) == 10
assert solution(2, [[1, 2, 1], [1, 2, 2], [1, 2, 3]]) == 6
assert solution(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 8, 15]]) == 31 # retornou 24

