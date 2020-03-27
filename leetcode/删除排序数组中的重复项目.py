"""
题目：删除排序数组中的重复项目，使其最多出现两次
解题说明: 排序数组，意味着元素已经排好序,则比较附近出现的元素
要求：不使用额外的空间
"""


def removeDuplicates():
    # 排序好的列表
    nums = [1, 1, 1, 2, 3, 3, 44,5,5]
    # 定义两个变量i，count，分别用于记录索引和出现的次数
    j, count = 1, 1

    # method 1
    # while i < len(nums):
    #     if nums[i] == nums[i - 1]:
    #         count += 1
    #         if count > 2:
    #             print(i)
    #             nums.pop(i)
    #             i -= 1
    #
    #     else:
    #         count = 1
    #
    #     i += 1
    # return len(nums)

    # method2
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1

        if count <= 2:

            nums[j] = nums[i]
            j += 1
    print(nums)
    return j
print(removeDuplicates())