class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found_vals = {}
        for n in nums:
            if n in found_vals.keys(): return True
            found_vals[n] = True
        return False
