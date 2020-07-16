# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表
#  👍 217 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
#1、clarification:异位词是字母出现的频率一样  但是位置不一样  （大小写是否敏感）
#2、possible solutions

    #暴力 sort, sorted_str 相等与否

def isAnagram_force( s, t) :
# leetcode submit region end(Prohibit modification and deletion)
    s=sorted(s)
    t=sorted(t)
    if s == t :
        return True
    else:
        return False
#也就是说只需要统计两个字符串中字符的频率
    #map的话 key 是字符  value 是次数
def isAnagram_hash(s,t):
    count={}
    if len(s) != len(t):
        return False
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False
    for value in count.values():
        if value != 0:
            return False
    return True

    return

#使用set 最快速的解法
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    se=set(s)
    if se == set(t):
        for i in se:
            if s.count(i) != t.count(i):
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    s='cat'
    t='car'
    res=isAnagram(s,t)
    print(res)