class Solution:
    """求两数之和"""

    def twoSUM(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                result = [dict[target - nums[i]], i]
                print(result)
                return result


Solution().twoSUM([1, 3, 4, 6, 7], 5)
