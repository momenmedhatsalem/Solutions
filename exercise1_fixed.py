from typing import Set

def id_to_fruit(fruit_id: int, fruits: Set[str]) -> str:
    """
    This method returns the fruit name by getting the string at a specific index of the set.

    :param fruit_id: The id of the fruit to get
    :param fruits: The set of fruits to choose the id from
    :return: The string corrosponding to the index ``fruit_id``

    FIXED: Sets are unordered in Python. Convert to a sorted list to have consistent ordering.
    """
    fruits_list = sorted(list(fruits))  # Convert to sorted list for consistent ordering
    idx = 0
    for fruit in fruits_list:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")


# Test the fixed function
if __name__ == "__main__":
    name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})
    name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})
    name4 = id_to_fruit(4, {"apple", "orange", "melon", "kiwi", "strawberry"})
    
    print(f"Index 1: {name1}")
    print(f"Index 3: {name3}")
    print(f"Index 4: {name4}")
    print(f"\nSorted list: {sorted(['apple', 'orange', 'melon', 'kiwi', 'strawberry'])}")
