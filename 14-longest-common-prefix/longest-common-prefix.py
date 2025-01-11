class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans =""
        s = strs[0]
        e = strs[-1]
        for i in range(min(len(s), len(e))):
            if s[i]!= e[i]:
                return ans
            ans += s[i]
        return ans
            

