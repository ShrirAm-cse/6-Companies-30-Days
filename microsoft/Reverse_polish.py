# problem link - https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ind in range(len(tokens)):
            res=0
            op=False
            if tokens[ind]=="*":
                num1=stack.pop(-1)
                num2=stack.pop(-1)
                res=num2*num1
                # print(res," ",num2," ",num1," ",tokens[ind])
                op=True
            elif tokens[ind]=="/":
                num1=stack.pop(-1)
                num2=stack.pop(-1)
                if (num1<0 and num2<0) or (num1>0 and num2>0):
                    res=num2//num1
                else:
                    res=math.ceil(num2/num1)
                    
                # print(res," ",num2," ",num1," ",tokens[ind])
                op=True
            elif tokens[ind]=="+":
                num1=stack.pop(-1)
                num2=stack.pop(-1)
                res=num2+num1
                # print(res," ",num2," ",num1," ",tokens[ind])
                op=True
            elif tokens[ind]=="-":
                num1=stack.pop(-1)
                num2=stack.pop(-1)
                res=num2-num1
                # print(res," ",num2," ",num1," ",tokens[ind])
                op=True
            if op:
                stack.append(res)
            else:
                stack.append(int(tokens[ind]))
        return stack[0]

                
