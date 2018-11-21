 # Find the longest unbroken series of increasing numbers in a list of random numbers',
 # If given [15, 2, 38, 71, 2, 524, 98], return [2, 38, 71]


def find_series(nums):
    print(nums)

    result = []
    count = 1
    local_count = 1
    local_result = []
    prev = None

    for current_num in nums:
        if prev is None:
            prev = current_num
            local_result.append(current_num)
            result = local_result.copy()
            continue

        if current_num > prev:
            local_count += 1
            local_result.append(current_num)
            if local_count > count:
                count = local_count
                result = local_result.copy()
        else:
            if local_count > count:
                count = local_count
                result = local_result.copy()
            local_count = 1
            local_result.clear()
            local_result.append(current_num)

        prev = current_num
    print(result, count)





nums = [15, 2, 38, 71, 2, 524, 98]
find_series(nums)
