"""
This module creates a list of non-unique elements from a given list.
"""
def checkio(data):
    """ 
        Creates a list of non-unique elements from a given list.
        
        Args:
            data: list of ints, list
            
        Returns: 
            non-unique elements (list)
    """
    non_unique_items = []
    for item in data:
        if data.count(item)> 1:
            non_unique_items.append(item)
    return non_unique_items


if __name__ == "__main__":
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"