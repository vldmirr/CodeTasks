# Дан отсортированный массив различных целых чисел и искомое значение. 
# Вернуть индекс, если искомое значение найдено. Если нет, вернуть индекс, на котором оно было бы, если бы оно было вставлено по порядку.

# Вам необходимо написать алгоритм, имеющий  O(log n)сложность во время выполнения.



class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        result=0
        for i,num in enumerate(nums):
            #*числа = [1,3,5,6], цель = 5
            if num==target:
                return i
            if target>num:
                result+=1
        return result

            
obj=Solution()

print(obj.searchInsert([-1,3,5,6],0))
        