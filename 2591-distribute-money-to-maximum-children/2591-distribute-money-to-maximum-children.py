class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children           #giving each child $1
        eighters = (money//7)       #grouping #7s group 
        remainder = money%7         #the money left after making groups of 7s. 

        #if remainder = 0, distribute every group of 7 and every child already have a 1. so 7+1. #Every children will have $8
        if children >= eighters and remainder == 0:
            return eighters
            
        #if there are less childrens than the eighters, every child will exceed above eight, no onve will have exactly $8. 
        if children < eighters:
            return children-1

        # Handle cases where there's leftover money after forming $7 groups
        if remainder > 0:
            if children == eighters:
                # All children would get $8, but we have leftover - sacrifice one
                return eighters - 1
            elif children > eighters:
                # Not all children can get $8
                if remainder == 3 and (children - eighters) == 1:
                    # Special case: $3 leftover with exactly one child left
                    # Must sacrifice one $8 allocation to avoid giving $4
                    return eighters - 1
                else:
                    # Otherwise, keep all $8 allocations and give remainder to one child
                    return eighters

        
        
        
        
        