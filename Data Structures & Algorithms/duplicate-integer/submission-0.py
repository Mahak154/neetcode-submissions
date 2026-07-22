class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=[]
        for a in nums:
            if a not in s:
                s.append(a)
            else:
                return True
        return False
                
        