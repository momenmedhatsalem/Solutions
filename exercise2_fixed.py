import numpy as np

def swap(coords: np.ndarray):
    """
    This method will flip the x and y coordinates in the coords array.

    :param coords: A numpy array of bounding box coordinates with shape [n,5] in format:
        ::

            [[x11, y11, x12, y12, classid1],
             [x21, y21, x22, y22, classid2],
             ...
             [xn1, yn1, xn2, yn2, classid3]]

    :return: The new numpy array where the x and y coordinates are flipped.

    FIXED: 
    1. coords[:, 1] was assigned twice - now properly swap x1<->y1 and x2<->y2
    2. Make a copy to avoid modifying the original array during simultaneous assignment
    """
    coords = coords.copy()  # Create a copy to avoid modifying original
    coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = coords[:, 1], coords[:, 0], coords[:, 3], coords[:, 2]
    return coords


# Test the fixed function
if __name__ == "__main__":
    coords = np.array([[10, 5, 15, 6, 0],
                       [11, 3, 13, 6, 0],
                       [5, 3, 13, 6, 1],
                       [4, 4, 13, 6, 1],
                       [6, 5, 13, 16, 1]])
    
    print("Original coordinates:")
    print(coords)
    
    swapped_coords = swap(coords)
    
    print("\nSwapped coordinates (x<->y):")
    print(swapped_coords)
    
    print("\nOriginal array unchanged:")
    print(coords)
