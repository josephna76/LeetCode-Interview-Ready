def maximum_average_subarray_i(nums, k):
    """
    Given int array nums and int k. Find a *continguous* subarray whose len is equal to k. Round to 10^-5.

    Subarray questions tend to be handled with sliding windows. We'll move this window through the array nums and return the maximum average.
    """
    window_sum = sum(nums[:k])  # Initialize with the sum of the first k elements

    max_average = window_sum / k  # Initialize the maximum average

    left_index = 1
    right_index = k

    while right_index < len(nums):
        window_sum += (
            nums[right_index] - nums[left_index - 1]
        )  # Update the window sum efficiently
        max_average = max(
            max_average, window_sum / k
        )  # Update the maximum average if necessary

        left_index += 1
        right_index += 1

    return round(max_average, 5)
