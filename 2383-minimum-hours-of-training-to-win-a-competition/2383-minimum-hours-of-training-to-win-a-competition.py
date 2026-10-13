class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res=0
        val=sum(energy)+1-initialEnergy #find minimum energy that we required
        if val>0:
            res+=val
        
        for i in experience: #now calculate experience
            if i>=initialExperience: #if don't have sufficent experience take time for gain experience
                val=i-(initialExperience-1)
                res+=val
                initialExperience+=val
            initialExperience+=i

        return res