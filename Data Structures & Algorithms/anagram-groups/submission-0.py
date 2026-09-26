class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol=defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            sol[key].append(s)
        
        return list(sol.values())


            
            


        