def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        larger = [j for j in arr[1:] if j > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(larger)


if __name__ == "__main__":
    mylist = [5, 3, 6, 2, 10]
    print(quick_sort(mylist))