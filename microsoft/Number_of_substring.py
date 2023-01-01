# problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        i=0
        j=0
        curr={"a":0,"b":0,"c":0}
        tot=0

        res=0
        while j<len(s):
            if s[j] in curr:
                if curr[s[j]]==0:
                    tot+=1
                curr[s[j]]+=1
            if tot==3:
                res+=(len(s)-j)
                # print(s[i:]," ",res)
                while tot==3 and i<j:
                    if curr[s[i]]==1:
                        tot-=1
                    if tot==3:
                        # print(s[i:]," ",res)
                        res+=(len(s)-j)
                    curr[s[i]]-=1
                    i+=1
            j+=1
        return res