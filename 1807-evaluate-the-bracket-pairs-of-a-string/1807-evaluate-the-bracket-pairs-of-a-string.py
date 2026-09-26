class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        knowledge = dict(knowledge)
        ret, h = [], -1
        for i, j in enumerate(s):
            if j == "(":
                h = i
            elif j == ")":
                ret.append(knowledge.get(s[h + 1 : i], "?"))
                h = -1
            elif h < 0:
                ret.append(j)
        return "".join(ret)
