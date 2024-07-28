def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:

            return (iterations, arr[mid])
        elif arr[mid] < target:

            left = mid + 1
        else:

            right = mid - 1

    if left < len(arr):

        upper_bound = arr[left]
    else:

        upper_bound = "No upper bound found"

    return (iterations, upper_bound)


# Приклад 1:
arr = [0.8, 1.4, 3.1, 4.2, 5.7, 7.7]
target = 3.1
iterations, upper_bound = binary_search(arr, target)
print(f"iterations: {iterations}, upper bound: {upper_bound}") # Виведе: iterations: 1, upper bound: 3.1

# Приклад 2:
arr = [2.1, 3.1, 4.1, 5.1, 6.1]
target = 8.1
iterations, upper_bound = binary_search(arr, target)
print(f"iterations: {iterations}, upper bound: {upper_bound}") # Виведе: iterations: 3, upper bound: No upper bound found

# Приклад 3:
arr = [-4.1, -3.0, -1.8, 0.1, 1.8, 3.4]
target = -2.0
iterations, upper_bound = binary_search(arr, target)
print(f"iterations: {iterations}, upper bound: {upper_bound}") # Виведе: iterations: 3, upper bound: -1.8

# Приклад 4:
arr = [-4.1, -3.0, -1.8, 0.2, 1.8, 3.4]
target = -5.5
iterations, upper_bound = binary_search(arr, target)
print(f"iterations: {iterations}, upper bound: {upper_bound}") # Виведе: iterations: 2, upper bound: -4.1

# Приклад 5:
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target = 6.5
iterations, upper_bound = binary_search(arr, target)
print(f"iterations: {iterations}, upper bound: {upper_bound}") # Виведе: iterations: 3, upper bound: 6.6