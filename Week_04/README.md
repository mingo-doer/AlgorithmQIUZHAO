# 学习笔记
这周因为在写论文  所以题目刷的比较少的
在第一次看完老师说的DP思路后，第一次直接AC了两道medium题，贼开心

dp 思路    
 1.划分各种子空间   
 2.定义好状态空间   
 3.动态规划
 
### Tip：
要去思考，可以自顶向下递归的 都可以自底向上动态规划。     
主要就是要找到重复子问题，保存每个子问题的最优状态，定义状态方程

## 例题：
回文子串 动态规划状态图   
[题解](https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/)   

编辑距离 主要是想到动态规划方程   
[编辑距离优秀题解](https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/)   

## 代码模板总结：

### 递归模板 
```
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

### 分治模板 
```
# Python
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

