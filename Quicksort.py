__author__ = 'gowri'


def quick_sort(num, low, high):
    pivot = num[low + (high - low)//2]

    i = low
    j = high

    while i <= j:

        while num[i] < pivot:
            i += 1

        while num[j] > pivot:
            j -= 1

        if i <= j:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
            i += 1
            j -= 1

    if i <= high:
        quick_sort(num, i, high)
    if low <= j:
        quick_sort(num, low, j)

nums = [19,8,2,23,10,1]
print(nums)
quick_sort(nums, 0, len(nums)-1)
print(nums)
