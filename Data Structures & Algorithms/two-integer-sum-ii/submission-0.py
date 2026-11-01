class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset = set(numbers)
        num = list(numset)
        for index1 in range(len(num)-1) :
            for index2 in range((index1 +1), len(num)) :
                if (num[index1] + num[index2]) == target :
                    return [num[index1], num[index2]]



        