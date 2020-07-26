[week 2 ]- 学习笔记

# 学习感悟
除了每天的日常刷题，总结学习内容和答题模板也是必不可少的。   
我会时常参考一些别的同学的总结，发现了有些的总结非常好，我就会拿过来参考。 比如这篇的总结[Leolai0926](https://github.com/LeoLai0926/AlgorithmQIUZHAO/tree/master/Week_02)   
下面是参考了这个同学和老师的代码模板进行的一个学习总结。以及自己做的题目的总结  
一开始想追着同学们的进度每天多做一些题，但就会发现只有数量没有质量的刷题是不行的。于是放慢了步骤，力争用一道题会一个系列的题，熟背模板后多加理解。时间总感觉不够用，之后还仍需要多多复习本周知识点。

# 代码模板
## 树
> 二叉树的层序遍历满足数组中第 i 个结点的左子结点索引为 2i, 右子结点的索引为 2i+1. 可以利用这个特性类解决问题.   
> 二叉搜索树(BST)的中序遍历是递增的

### 树的前中后序遍历代码模板
```
def preorder(self, root):
    if root: 
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```

### 递归代码模板

#### 思维要点
1.不要人肉进行递归(最大误区)   
2.找到最近最简方法, 将其拆解成可重复解决的问题(重复子问题)   
3.数学归纳法思维   

```
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data, ...)

    # drill down
    self.recursion(level + 1, param1, param2', ...)

    # reverse the current level status if needed
```

### DFS代码模板
```
visited = set() #十分重要
def dfs(node, visited):
    if node in visited: # terminator
        # already visited
        return

    visited.add(node)

    # process current node here
    # ...

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```
### BFS代码模板
```
def bfs(graph, start, end):
    queue = []
    queue.append([start])

    visited = set()     # 与树中的bfs最大的不同

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```
### Heap Sort （堆排序）
堆排序利用堆的特性来对数组进行排序, 在大根堆中, 最大元素始终为根节点. 堆排序循环的从堆中取出根节点来排序. 具体步骤如下:   
1.从未排序的数组构造大根堆 heap   
2.提取最大元素 A[0].   
3.交换 A[-1] 与 A[0]. (此时最大元素已位于堆的最后)   
4.从堆中 pop 出最大值   
5.对堆进行 max_heapify   
6.转至2, 除非堆已空   
```
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)
```

```
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
```
### 二叉树遍历
最简易递归模板
```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序递归
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归 
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```
通用模板 可以适应不同的题目，添加参数、增加返回条件、修改进入递归条件、自定义返回值
```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return      
            # 前序递归
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right) 
            # # 中序递归
            # dfs(cur.left)
            # res.append(cur.val)
            # dfs(cur.right)
            # # 后序递归
            # dfs(cur.left)
            # dfs(cur.right)
            # res.append(cur.val)      
        res = []
        dfs(root)
        return res
```
### 迭代模板 
前中序后通用模板
```
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        
        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res
        
        # # 后序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]
```

#### 层序遍历模板
```
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur, res = [root], []
        while cur:
            lay, layval = [], []
            for node in cur:
                layval.append(node.val)
                if node.left: lay.append(node.left)
                if node.right: lay.append(node.right)
            cur = lay
            res.append(layval)
        return res
```
#### N叉树遍历
N叉树通用递归模板
```
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res
```
N叉树迭代模板
```
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        # s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            # for child in node.children[::-1]:
            #     s.append(child)
            s.extend(node.children[::-1])
        return res
```
#### 复习题目
[二叉树前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/)   
[二叉树中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/)   
[二叉树后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/)   
[二叉树层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/)      
[二叉树前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)

## 题目总结

### 树 DFS：栈 和BFS：队列

|  题目   | 过的遍数  | 题目类型 | 思考 |
|  ----  | ----  |   ----  | ----  |
| 94 144 二叉树的前中序遍历 | 代码 + 手写 | 二叉树的遍历  | 熟记递归模板和迭代模板 迭代 栈的操作|
| 429 层序遍历 590 N叉树的后序遍历  | 代码  | N叉树的遍历  |  层序遍历 BFS 队列操作 需要熟背模板|
| 104 二叉树的最大深度  | 代码 +手写  | DFS  |  DFS->栈的操作 |
| 98 验证二叉搜索树  | 代码 | 树的递归  |  二叉搜索树性质 递增  -> 联系 中序遍历是递增的   |


### 堆

|  题目   | 过的遍数  | 题目类型 | 思考 |
|  ----  | ----  |   ----  | ----  |
|   最小的K个数  | 代码  | 堆  | 还需要复习堆的性质和操作  以及熟背代码模板  |
| 347前K个高频元素  | 代码  |  hashmap和堆 | 返回频率高的元素->频率 ->hashmap 高的->堆     |
| 239 滑动窗口的最大值  | 代码  | 双端队列 堆  |  **仍需要复习** |


### 回溯 动态规划

|  题目   | 过的遍数  | 题目类型 | 思考 |
|  ----  | ----  |   ----  | ----  |
| 46 全排列  | 代码 +画图 | 回溯 |  需要继续理解 加熟记代码 |
| 77 组合   | 代码 +画图 | 回溯 |  需要继续理解  |
| 49 丑数   | 代码   | 动态规划 | **仍需要复习** |


