class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        res=[]
        freq = dict(sorted(freq.items(),key = lambda x :x[1],reverse=True))
        return list(freq.keys())[:k]
        

        