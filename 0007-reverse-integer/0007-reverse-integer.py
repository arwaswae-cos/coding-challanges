class Solution:
    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1])
        if -2**31 > temp or temp > 2**31-1:
               return 0 
        return temp if x>0 else -temp    
            
            

            
            
        