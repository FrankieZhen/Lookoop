# 2018-9-2
# Binary Indexed Tree
# https://www.hackerearth.com/zh/practice/notes/binary-indexed-tree-made-easy-2/
# 推荐看： https://www.cnblogs.com/whensean/p/6851018.html
# 网页底部有数据结构总览表： https://en.wikipedia.org/wiki/Fenwick_tree

# 来源于LeetCode
# 307. Range Sum Query - Mutable
# Binary Indexed Tree

# 关键在于 k -= (k & -k) 和 k += (k & -k), 前者用于update后者用于sum
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.lens = len(nums)

        # 初始化存储sum的数组
        self.BIT = [0] * (self.lens + 1)
        # map(update, range(self.lens), nums)
        for i in range(self.lens):
            k = i + 1 
            while k <= self.lens:
                self.BIT[k] += nums[i]
                k += (k & -k)

        

    def update(self, i, val):
        """
        update 操作一直都是遍历左侧
        :type i: int
        :type val: int
        :rtype: void
        """

        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.lens:
            self.BIT[i] += diff
            i += (i & -i)
        # print(self.BIT)
        

    def sumRange(self, i, j):
        """
        sum: 遍历右侧
        上一层已经把左侧的值加上去了，而左侧的索引又是小于右侧，所以是合理的
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        j += 1
        while j > 0:
            res += self.BIT[j]
            j -= (j & -j)
            
        while i > 0:
            res -= self.BIT[i]
            i -= (i & -i)

        return res
        


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
obj.update(1, 2)
obj.update(1, 44)
obj.update(2, 44)
r1 = obj.sumRange(0, 2)
print(r1,obj.nums)