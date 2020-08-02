# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
#
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
#
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
#
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
#
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。
#
#  注意:
#
#
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
#  所有的目标基因序列必须是合法的。
#  假定起始基因序列与目标基因序列是不一样的。
#
#
#  示例 1:
#
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# 返回值: 1
#
#
#  示例 2:
#
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# 返回值: 2
#
#
#  示例 3:
#
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# 返回值: 3
#
#  👍 44 👎 0

#dfs

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        count = 0
        bank = set(bank)
        change_map = {
            'A': 'CGT',
            'C': 'AGT',
            'G': 'ACT',
            'T': 'ACG'
        }

        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            # terminator
            nonlocal min_count
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not current_bank:
                return
                # process
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse
                    current_bank.add(new)

        dfs(start, 0, bank)
        return min_count if min_count < len(bank) + 1 else -1
# leetcode submit region end(Prohibit modification and deletion)

# bfs
def minMutation(start,end,bank):
     count = 0
     bank = set(bank)
     change_map = {
         'A': 'CGT',
         'C': 'AGT',
         'G': 'ACT',
         'T': 'ACG'
     }
     queue = [(start,0)]
     while queue:
         # terminator
        node,step = queue.pop(0)
        if node == end:
            return step
        for i , s in enumerate(node):
            for char in change_map[s]:
                new = node[:i] + char +node[i+1:]
                if new in bank:
                    queue.append((new,step+1))
                    bank.remove(new)
     return -1

if __name__ == '__main__':
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    res = minMutation(start,end,bank)
    print(res)