'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

# 2018-6-16
# 3Sum
# 暴力破解
# [Finished in 63.4s]
class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        lens = len(nums)
        if lens < 3:
            return res
        i = 0
        while i < lens - 2:
            j = i + 1
            while j < lens - 1:
                k = j + 1
                while k < lens:
                    tmp = []
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp.append(nums[i])
                        tmp.append(nums[j])
                        tmp.append(nums[k])
                        res.append(tmp)
                    k += 1
                j += 1
            i += 1
        if not res:
            return res
        r = []
        for i in res:
            r.append(sorted(i))
        lens = len(r)
        m = 0
        pp = 1
        while m < len(r) - 1:
            n = m + 1
            while n < len(r) and pp == 1:
                if r[m] == r[n]:
                    r.pop(n)
                    n -= 1
                n += 1
            m += 1
        return r


# 双指针法
# 超出时间限制
# [Finished in 15.9s]
class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        lens = len(nums)
        if lens < 3:
            return res
        nums = sorted(nums)
        i = 0
        while i < lens-2 and nums[i] <= 0:
            l = i + 1
            r = lens - 1
            tmp = []
            while l < r:
                if nums[l] + nums[r] < (-nums[i]):
                    l += 1
                elif nums[l] + nums[r] > (-nums[i]):
                    r -= 1
                else:
                        tmp.append(nums[i])
                        tmp.append(nums[l])
                        tmp.append(nums[r])
                        if tmp in res:
                            l += 1
                            r -= 1
                            tmp = []
                        else:
                            res.append(tmp)
                            tmp = []
                            l += 1
                            r -= 1
            i += 1
        return res

# 2018-12-21
# [Finished in 18.3s]
class Solution3:
    def threeSum(self, nums):
        tmp, res = [[i] for i in nums], []
        # print(tmp)
        nums = sorted(nums)
        for m, n in enumerate(nums):
            for k, v in enumerate(tmp[m + 1:]):
                if len(v) == 1:
                    if v[0] + n <= n:
                        tmp.append(v + [n])
                elif len(v) == 2:
                    tmp_res = v + [n]
                    if sum(tmp_res) == 0 and tmp_res not in res:
                        res.append(tmp_res)
            # print(tmp)
        return res

# test
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
m = [     [0,0,0,0,0],[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6],   [], [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0,0,0,0],
        [-1,1,0,1,-1,0,-1,1,-1],[-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15]]

test = Solution3()
for m in m:
    res = test.threeSum(m)
    print ("new____",res)