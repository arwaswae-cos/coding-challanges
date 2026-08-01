class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = s[0] if s!= '' else ''
        t1 = t[0] if t!= '' else ''
        for i in range(1,len(s)):
            if s[i] == '#':
                s1 = s1[:-1]
            else:
                s1 += s[i]
        for i in range(1,len(t)):
            if t[i] == '#':
                t1 = t1[:-1]
            else:
                t1 += t[i]
        return s1.strip('#')==t1.strip('#')
        