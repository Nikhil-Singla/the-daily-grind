class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        n = n - 1000    # Since n can only be upto 100,000
                        # This means after 999, every number can ONLY 
                        # have one comma at most. 

        return n + 1    # Add one as we start counting from "0" 
