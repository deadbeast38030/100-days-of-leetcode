class Solution(object):
    def searchRange(self, nums, target):
        a=[]
        for i in range(0,len(nums)):
            if nums[i]== target:
                a.append(i)
                break
        if not a:
            return [-1, -1]    
        nums.reverse()
        for j in range(0,len(nums)):
            if nums[j]== target:
                a.append(len(nums)-(j+1))
                break
        return a