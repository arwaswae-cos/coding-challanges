class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry, n = 0, len(num)
        for i in range(1,n+1):
            p = num[-i]+k%10+carry 
            num[-i] = p if p<10 else p%10
            carry = p//10
            k = k//10 
        if k!=0:
            lst = list(map(int, str(k+carry)))
            num = lst + num
            carry = 0
        if carry != 0:
            num = [carry] +num
    
        return num