def bynar_serach(array, number):
    low = 0
    high = len(array) -1
    cycles = 0
    while low <= high:
        cycles += 1
        mid = (low + high) // 2
        if number < array[mid]:
            high = mid - 1
        elif number > array[mid]:
            low = mid + 1
        else:
            return mid, cycles
            break
