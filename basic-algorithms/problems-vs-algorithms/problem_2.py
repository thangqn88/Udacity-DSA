"""
Problem 2: Search in a Rotated Sorted Array

You are given a sorted array that has been rotated at a random pivot point. 
For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

You are also given a target value to search for. If the target is found in the 
array, return its index; otherwise, return -1. Assume there are no duplicates 
in the array, and the runtime complexity of your algorithm must be O(log n).

You should implement the function body according to the rotated_array_search 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rotated_array_search(input_list: list[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
    input_list (list[int]): Input array to search
    number (int): Target number to find

    Returns:
    int: Index of the target number or -1 if not found
    """
    if not input_list:
        return -1

    # Find the pivot point in the list
    pivot_index = find_pivot_index(input_list)

    if pivot_index == -1:
        return binary_search(input_list, number, 0, len(input_list) - 1)

    if input_list[pivot_index] == number:
        return pivot_index

    # If the target number is greater than the first element
    if number >= input_list[0]:
        return binary_search(input_list, number, 0, pivot_index - 1)

    # If the target number is less than the first element
    return binary_search(input_list, number, pivot_index + 1, len(input_list) - 1)

def find_pivot_index(input_list: list[int]) -> int:
    left = 0
    right = len(input_list) - 1

    while left <= right:
        mid = (left + right) // 2

        # If the mid element is greater than the next element
        if mid < right and input_list[mid] > input_list[mid + 1]:
            return mid
        # If the mid element is less than the previous element
        if mid > left and input_list[mid] < input_list[mid - 1]:
            return mid - 1
        # If the list is not rotated
        if input_list[left] >= input_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def binary_search(input_list: list[int], number: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2

        if input_list[mid] == number:
            return mid
        if input_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test function using provided test cases
def test_function(test_case: list[list[int], int]) -> None:
    """
    Test the rotated_array_search function with a given test case.

    Args:
    test_case (list[list[int], int]): A list containing two elements:
        - A list of integers representing the input array to search.
        - An integer representing the target number to find.

    Returns:
    None: Prints "Pass" if the rotated_array_search function returns the same 
    result as the linear_search function, otherwise prints "Fail".
    """
    input_list: list[int] = test_case[0]
    number: int = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def linear_search(input_list: list[int], number: int) -> int:
    """
    Perform a linear search for a target number in a list of integers.

    Args:
    input_list (list[int]): The list of integers to search through.
    number (int): The target number to find in the list.

    Returns:
    int: The index of the target number if found, otherwise -1.
    """
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

if __name__ == '__main__':
    # Edge case: Empty input list
    test_function([[], 5])
    # Expected output: Pass

    # Normal case: Number at the beginning of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 4])
    # Expected output: Pass

    # Normal case: Number at the end of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 2])
    # Expected output: Pass

    # Normal case: Number in the middle of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 6])
    # Expected output: Pass
