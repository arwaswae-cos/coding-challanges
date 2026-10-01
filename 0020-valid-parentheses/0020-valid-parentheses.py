class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)==1:
            return False
        l = []
        for i in s:
            if i == '(' or i=='{' or i=='[':
                l.append(i)
            else:
                if l==[]:
                    return False
                if i == ']' and l[-1] != '[' :
                    return False
                if i=='}' and l[-1] != '{':
                    return False
                if i==')' and l[-1] != '(':
                    return False
                l.pop()
        return True if l==[] else False