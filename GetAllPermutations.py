class Solution(object):
    def nextPermutation(self, nums):
        print(nums)

        print(self.get_permutations(nums))

    def get_permutations(self, nums):
        if len(nums) == 1:
            return [nums[0]]

        numbers = self.get_permutations(nums[1:])
        result = []

        for result_num in numbers:
            for i in range(0, len(result_num)+1):
                first = result_num[0:i]
                second = result_num[i:]
                str = first + nums[0] + second
                result.append(str)
        return result


my_sol = Solution()

nums = ['1','2', '3']
my_sol.nextPermutation(nums)