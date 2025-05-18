'''
Challenge: Optimize the function to handle large input lists efficiently.
==============================
Description: Develop a function called find_common_elements that takes two lists as input and returns a new list
 containing elements that are common to both input lists.'''
from logging import exception


def find_common_elements(list1, list2):
    try:
        set1 = set(list1)
        set2 = set(list2)
        print(list1, list2)
        common = set1.intersection(set2)

        return list(common)
    except TypeError as e:
        print(f"TypeError: one or both inputs are not iterable: {e}")
        return[]
    except Exception as e:
        print (f"An unexpected eror occurred: {e}")
        return []

print (find_common_elements ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

