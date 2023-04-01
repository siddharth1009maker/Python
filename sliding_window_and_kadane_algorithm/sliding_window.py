#  It is an algorithm where we can fast compute the things
# which have a fixed window for calculation and we can fetch the
# result in an optimized manner than using the nested loops(naive approach).
# The main goal of this algorithm is to reuse the result of one window to
# compute the result of the next window.
# https://www.scaler.com/topics/sliding-window-algorithm/


# For Example
# Given an array of integers of size ‘n’, Our aim is to calculate
# the maximum sum of ‘k’ consecutive elements in the array.


def get_max_sum(arr, length, window_size):
    # This function returns the maximum sum for a particular window size in the array

    max_sum = -1
    present_sum = 0

    for index in range(window_size):
        present_sum = present_sum + arr[index]

    max_sum = present_sum

    for index in range(window_size, length):
        present_sum = present_sum - arr[index - window_size]
        present_sum = present_sum + arr[index]
        max_sum = max(max_sum, present_sum)

    # Returns the maximum sum for the given window_size
    return max_sum


# taking the window size
window_size = int(input("Enter the window size: "))

user_input = input("Enter numbers separated by a comma:").strip()
arr = [int(item) for item in user_input.split(",")]

# using the len() function to calculate the length of the array
length = len(arr)

ans = get_max_sum(arr, length, window_size)

print(f"The maximum sum of the array for window size {window_size} is {ans}")
