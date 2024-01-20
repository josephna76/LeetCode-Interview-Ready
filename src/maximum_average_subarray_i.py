def maximum_average_subarray_i(nums, k):
    """
    Given int array nums and int k. Find a *continguous* subarray whose len is equal to k. Round to 10^-5.

    Subarray questions tend to be handled with sliding windows. We'll move this window through the array nums and return the maximum average.
    """
    window_product = 1
    for number in nums[: k - 1]:
        window_product *= number

    left_index = 1
    right_index = k
    for number in nums[left_index:right_index]:
        window_product = max(
            window_product, (window_product / nums[left_index]) * nums[right_index]
        )

    return round(window_product / k, 5)
