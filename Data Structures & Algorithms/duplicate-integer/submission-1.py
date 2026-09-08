class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        humble=set()
        for num in nums:
            if num in humble:
                return True
            humble.add(num)
        
        return False