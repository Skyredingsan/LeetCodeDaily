class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max = -1
        i = 0
        j = 0
        answer = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < 0:
                    if nums[i]==(nums[j]*(-1)) and nums[i]>max:
                        max = nums[i]
            j+= 1
        i+= 1
        answer = max
        return answer
