#暴力法
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表
#  👍 8648 👎 0
#暴力法
def twoSum( nums, target) :
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j])==target:
                return [i,j]
        return []

#两遍hash 先遍历a
#a,b -> a + b == target -->
# for each a : check (target - a )  exist in nums
def twoSum_twicehash(nums,target):
    hashmap = {}
    #构造了一个数频hash
    for i, num in enumerate(nums):
        hashmap[num] = i
    for i , num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i,j]
    return



if __name__ == '__main__':
    nums=[3,2,3]
    target=6
    res=twoSum_twicehash(nums,target)
    print(res)


