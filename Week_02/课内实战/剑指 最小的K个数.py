# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

#sort 就无敌简单
import heapq


def getleastNum(arr,k):
    arr=sorted(arr)
    return arr[:k]
# 这里练习一下堆的操作
# python 中的堆是小根堆 要对数组中所有的数取相反数 才能用小根堆维护前K小值

def getLeastNumHeap(arr,k):
    if k ==0:
        return list()
    #先取前K个元素入堆
    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    # 再遍历后面的值
    for i in range(k,len(arr)):
        #如果当前遍历的数比大根堆的堆顶数要小，就将堆顶弹出 把小数放进堆里
        if -hp[0] > arr[i]:
            heapq.heappop(hp)
            #将大根堆的值存入数组
            heapq.heappush(hp,-arr[i])
    res = [-x for x in hp]
    return res
