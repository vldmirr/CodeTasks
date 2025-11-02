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
    
    #Pascal's Triangle
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        
        for i in range(numRows):
            
#             [1]
#           [1, 1]
#          [1, 1, 1]
#         [1, 1, 1, 1]
#       [1, 1, 1, 1, 1]
#        .............
            row = [1] * (i + 1)
            print(row)
            
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
        
        return triangle

d=[4,3,2,1]
#d=[9,9]
#d=[9]

#1
#2

o=Solution()
print(o.plusOne([4, 3, 2, 1]))
print(o.generate(5))
