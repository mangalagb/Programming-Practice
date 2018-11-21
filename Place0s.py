def place_zeros(nums):
    position_to_insert = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            if position_to_insert != i:
                temp = nums[i]
                nums[i] = 0
                nums[position_to_insert] = temp
            position_to_insert += 1
    print(nums)

# nums = [9,8,45,7,8,-6, 0, 0]
# place_zeros(nums)

nums = [0,9,0, 98,0,0,0,87]
place_zeros(nums)
