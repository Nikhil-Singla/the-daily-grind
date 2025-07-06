# Q1:

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        orderedList = ["electronics", "grocery", "pharmacy", "restaurant"]
        validBS = set(orderedList)
        
        def validOne(couponCode, businessCode, activityStat):
            if not couponCode:
                return False

            if not activityStat:
                return False

            if businessCode not in validBS:
                return False
            
            for i in couponCode:
                if i.isalnum() or i == '_':
                    continue
                else:
                    return False

            return True

        sepCoupons = {i : [] for i in validBS}
        
        for i, j, k in zip(code, businessLine, isActive):
            if validOne(i, j, k):
                sepCoupons[j].append(i)

        retVal = []
        for i in orderedList:
            if sepCoupons[i]:
                retVal.extend(sorted(sepCoupons[i]))
        
        return retVal
    
