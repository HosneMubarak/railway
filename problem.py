def maxSum(arrr, size):
    let_max = arrr[0]
    max_end = 0

    for i in range(0, size):
        max_end = max_end + arrr[i]
        if max_end < 0:
            max_end = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (let_max < max_end):
            let_max = max_end

    return let_max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
len_of_arr = len(nums)

result = maxSum(nums, len_of_arr)
print(result)
