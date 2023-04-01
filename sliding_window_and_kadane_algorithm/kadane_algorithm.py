# The idea of Kadane’s algorithm is to maintain a variable max_ending_here
# hat stores the maximum sum contiguous subarray ending at current index and a
# variable max_so_far stores the maximum sum of contiguous subarray found so far,
# Everytime there is a positive-sum value in max_ending_here
# compare it with max_so_far and update max_so_far if it is greater than max_so_far.
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


def get_max_sum(arr, length):
    # This function returns the maximum sum for contiguous part of the array
    present_sum = 0
    max_sum = -1

    for index in range(length):
        present_sum = present_sum + arr[index]
        max_sum = max(max_sum, present_sum)

        if present_sum < 0:
            present_sum = 0

    # Returns the maximum sum of the contiguous part of array
    return max_sum


user_input = input("Enter numbers separated by a comma:").strip()
arr = [int(item) for item in user_input.split(",")]

# using the len() function to calculate the length of the array
length = len(arr)

ans = get_max_sum(arr, length)

print(f"The maximum sum of the array is {ans}")
