# 第三周学习总结

## 分治 Divide & Conquer

递归状态树   中心思想就是找重复性 找最小的重复单元 
> 找到子问题      
>合并   



代码模板
```
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

## 回溯
回溯采用的是试错的思想，最简单通过递归来实现   
>找到可能存在的正确答案   
>尝试了所有可能的分步方法后宣告问题没有答案   
[括号生成问题](https://leetcode-cn.com/problems/generate-parentheses/)   
[八皇后](https://leetcode-cn.com/problems/n-queens/)   

## 深度优先搜索 dfs 和广度优先搜索  bfs

### 搜索-遍历
>每个节点都要访问一次   

>每个节点仅仅要访问一次

>对于节点的访问顺序不限   
>>深度优先：dfs depth first search

>> 广度优先 breadth first search   

### 代码模板   
dfs 递归写法
```
#Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)

```
dfs 非递归写法
```
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```
### BFS 代码模板 使用队列
```
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```
## 贪心算法
是在每一步选择中都采取当前状态下最好或者最优，从而希望结果是全局最好或者最优   
贪心算法与动态规划的不同：   
>在于它对每个子问题的解决方案都做出选择，不能回退。     
 
>动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

可以解决的问题：
>贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码
等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。 
>
[coin change](https://leetcode-cn.com/problems/coin-change/)
[分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)

适用贪心算法的场景：
问题能够分解成子问题来解决，子问题的最优解能递推到最终
问题的最优解。这种子问题最优解称为最优子结构。

## 二分查找
前提：
>目标函数单调性（单调递增或者递减）

>存在上下界（bounded）

>能够通过索引访问（index accessible)
代码模板
```
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```
