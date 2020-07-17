#思路是先取两边的柱子 作为左右指针  向中间收敛
def maxArea(height) :
    area=0
    #从两边向中间逼近
    i=0
    j=len(height)-1
    while i<j :
        if height[i]<height[j]:
            area=max(area,height[i]*(j-i))
            i=i+1
        else:
            area=max(area,height[j]*(j-i))
            j=j-1

    return area


    return area
if __name__ == '__main__':
    height=[1,8,6,2,5,4,8,3,7]
    res=maxArea(height)
    print(res)