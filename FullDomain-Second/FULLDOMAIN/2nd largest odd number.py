arr = [1, 2, 8, 9, 788, 0, 7, 5, 3, 22, 34, 5, 6, 7, 500, 501, 502, 503]

def secondLargeOddNumber(arr):
    largest = 0
    second_largest = 0

    for num in arr:
        if num % 2 == 0:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num

    return second_largest

print(secondLargeOddNumber(arr))
