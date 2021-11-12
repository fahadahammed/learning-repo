from helpers.helpers import TimeCalculator as tc

# Devide and Conquer

numbers = [1, 3, 556, 123, 22, 100.99, 10.5, 5.1, 1.1, 1.2, 100.99, 1000, 35.88, 1034]*5999099

# Need to find a number in a defined array of numbers

# Binary search works in sorted array.

numbers.sort()

@tc
def general_way_to_find_an_item(array, item):
    position = None
    for i, v in enumerate(array):
        if v == item:
            if not position:
                position = i

    return position


print(general_way_to_find_an_item(array=numbers, item=100.99))


@tc
def binary_search_iter(array, item):

    low = 0
    high = len(array)-1

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == item:
            return mid

        elif array[mid] < item:
            low = mid + 1

        else:
            high = mid - 1

    return -1


print(binary_search_iter(array=numbers, item=100.99))



def binary_search_recur(array, item, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == item:
            return mid

        # Search the right half
        elif array[mid] < item:
            return binary_search_recur(array, item, mid + 1, high)

        # Search the left half
        elif array[mid] > item:
            return binary_search_recur(array, item, low, mid - 1)


    else:
        return -1

@tc
def xx():
    print(binary_search_recur(array=numbers, item=100.99, low=0, high=len(numbers)-1))

xx()
