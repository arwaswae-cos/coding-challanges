class Solution:
    
    tens = {11:"Eleven", 12:"Twelve", 13:"Thirteen", 14: "Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen",
        10: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty",
        5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
    }
    ones = {
        0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    def uptothree (self,m):
        ret = ''
        if m==0:
            return ''
        if m>=100:
            ret += f'{self.ones[m//100]} Hundred '
            m %= 100
        if m < 10:
            return (ret + f'{self.ones[m]}').strip()
        if m < 20:
            return (ret + f'{self.tens[m]}').strip()
        return (ret + f'{self.tens[m//10]} {self.ones[m%10]}').strip()
        
    def numberToWords(self, num: int) -> str:    
        value = ['', ' Thousand ', ' Million ', ' Billion ' ]
        ret = ''
        i = 0
        while num>0:
            
            m = num%1000
            r = self.uptothree(m)
            ret = r + value[i] + ret if r != '' else ret
            num = num//1000
            i += 1
        return ret.strip() if ret != '' else 'Zero'