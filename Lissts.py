class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s1=""
        
        for e in digits:
            s1+=str(e)

        num=str(int(s1)+1)
        digits=[]
        for i in range(len(num)):
            digits.append(int(num[i]))

        return digits

d=[4,3,2,1]
#d=[9,9]
#d=[9]

o=Solution()
print(o.plusOne([4, 3, 2, 1]))
