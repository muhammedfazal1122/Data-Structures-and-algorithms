# def find_factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * find_factorial(num - 1)
#
#
# result = find_factorial(5)
#
# print(f"factorial is {result}")

# def fibonacci(n):
#     if n <= 0:
#         return 0
#
#     elif n == 1:
#         return 1
#
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(10):
#     print(fibonacci(i))


# def find_sum(num):
#     if num == 1:
#         return 1
#     else:
#         return num + find_sum(num - 1)

# print(find_sum(5))

def array_sum(arr, n):
    if n == 0:
        return 0
    else:
        return array_sum(arr, n - 1) + arr[n - 1]


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(array_sum(arr, n))
