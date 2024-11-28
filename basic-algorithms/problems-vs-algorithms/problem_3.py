"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    # Sort the input list in descending order
    sorted_list = merge_sort(input_list, reverse=True)
    # Initialize two empty strings to store the digits of the two numbers
    num1: int = 0
    num2: int = 0
    exp: int = 0

    # Alternate the digits of the input list between the two numbers
    for i, digit in enumerate(sorted_list):
        if i % 2 == 0:
            num1 = 10*num1 + digit
        else:
            num2 = 10*num2 + digit

    return [num1,num2]

def merge_sort(input_list: list[int], reverse=False) -> list[int]:
    if len(input_list) <= 1:
        return input_list
    mid: int = len(input_list) // 2
    left: list[int] = input_list[:mid]
    right: list[int] = input_list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    if reverse:
        return merge_lists(left, right)[::-1]
    return merge_lists(left, right)

def merge_lists(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into a single sorted list.
    """
    result: list[int] = []
    left_index: int = 0
    right_index: int = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, -42]))
    # Expected output: False, all array elements must be in the range [0, 9]

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 2]))
    # Expected output: False because "The number of digits in both the numbers cannot differ by more than 1"
    
    # Other test cases
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[],[]])
    test_function([[1],[1]])
