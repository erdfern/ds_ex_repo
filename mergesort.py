# Issues:
# 1. Comprehensibility
#    - No comments/docstring for mergeSort function
#    - Index variables have non-descriptive naming, could be i, leftIdx, rightIdx
#    - list_to_be_sorted_by_merge; name is too long
# 2. Reproducibility
#    - Nothing that could be improved in _this_ file
# 3. Consistency
#    - Unit tests could be added to confirm correctness of mergeSort implementation
# 4. Correctness
#    - ^
# 5. Reusability
#    - Main function so nothing gets executed on import
# 6. Clarity
#    - Top level execution could be made clearer with use of a _main function (underscore to make it module-private)
#    - Recursion check can be greatly simplified with early return
#    - ASSIGNMENT function is redundant, should be inlined
#    - Module imports should be at top of file
# 7. Thoroughness
# 8. Robustness
#    - Adding type hints could improve robustness
import matplotlib.pyplot as plt
from typing import List
import unittest


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        list: List[int] = []
        mergeSort(list)
        self.assertListEqual(list, [])

    def test_length_one(self):
        list: List[int] = [0]
        mergeSort(list)
        self.assertListEqual(list, [0])

    def test_simple_list(self):
        list = [3, 2, 1, 0]
        expected = [0, 1, 2, 3]
        mergeSort(list)
        self.assertListEqual(list, expected)

    def test_jumbled_list(self):
        list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        mergeSort(list)
        self.assertListEqual(list, expected)


def mergeSort(list_to_sort_by_merge: List[int]) -> None:
    """
    Sorts a list of integers in ascending order using the merge sort algorithm.

    This function operates in-place, directly modifying the input list.

    Args:
        list_to_sort: The list of integers to be sorted.

    Time Complexity:
        O(n log n) in the average and worst cases, where n is the length of the list.
        This is because the list is repeatedly divided in half and merged back together.

    Space Complexity:
        O(n) auxiliary space due to the temporary lists created during merging.

    Example:
        >>> numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        >>> mergeSort(numbers)
        >>> print(numbers)
        [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    # Base case: a list with 0 or 1 elements is inherently sorted
    if (len(list_to_sort_by_merge)) <= 1:
        return

    mid = len(list_to_sort_by_merge) // 2
    left = list_to_sort_by_merge[:mid]
    right = list_to_sort_by_merge[mid:]

    # Recursively sort halves
    mergeSort(left)
    mergeSort(right)

    i = 0
    leftIdx = 0
    rightIdx = 0

    while leftIdx < len(left) and rightIdx < len(right):
        if left[leftIdx] <= right[rightIdx]:
            list_to_sort_by_merge[i] = left[leftIdx]
            leftIdx += 1
        else:
            list_to_sort_by_merge[i] = right[rightIdx]
            rightIdx += 1
        i += 1

    while leftIdx < len(left):
        list_to_sort_by_merge[i] = left[leftIdx]
        leftIdx += 1
        i += 1

    while rightIdx < len(right):
        list_to_sort_by_merge[i] = right[rightIdx]
        rightIdx += 1
        i += 1


def _main():
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # Plot unsorted list
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()

    # Plot sorted list
    mergeSort(my_list)
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()


if __name__ == "__main__":
    _main()
