def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1

    return None

if __name__ == "__main__":
    mylist = [1, 3, 5, 7, 9, 11, 22, 27]

    print(binary_search(mylist, 9))
    print(binary_search(mylist, 25))