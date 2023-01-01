# problem link - https://leetcode.com/problems/bulls-and-cows/description/


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        d={}
        s=[]
        g=[]
        for i in range(10):
            d[i]=0
            s.append(0)
            g.append(0)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
            else:
                s[int(secret[i])]+=1
                g[int(guess[i])]+=1
        cow=sum([min(g[i],s[i]) for i in range(10)])
        return ""+str(bull)+"A"+str(cow)+"B"
