class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs={}
        for i,j in enumerate(nums):
            c = target - j
            if c in hs:
                return [hs[c],i]
            hs[j]=i

    