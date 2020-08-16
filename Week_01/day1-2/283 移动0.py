def moveZeroes(nums) :
    """
    Do not return anything, modify nums in-place instead.
    """
    #双指针 j始终指向不为0的元素
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            #j中始终为不为0的元素
            nums[j]=nums[i]
            # 这一步相当关键 把替换的位置设为0
            if i!=j:
                nums[i]=0
            j=j+1

    return nums

if __name__ == '__main__':
    nums=[0,1,0,3,12]
    num=moveZeroes(nums)
    print(num)