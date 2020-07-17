def threeSum(nums) :
    #将数组排序
    res=[]
    nums.sort()
    for i in range(len(nums)-2):
        #少 原理是：target 数如果两个都一样 那就不用寻找了 可以直接下一个
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l , r= i+1, len(nums)-1
        #设置左右指针 向中间收敛
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
                #这里是elif 而不是if
            elif s > 0:
                r -= 1
            else:
                #找到结果
                res.append((nums[i], nums[l], nums[r]))
                #缺失思路 可能出现多个结果  所以继续寻找 继续寻找还需要比较左右指针是否和当前的数一致，如果一致则选下一个数
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return  res



if __name__ == '__main__':
    nums=[-1,0,1,2,-1,-4]
    res=threeSum(nums)
    print(res)