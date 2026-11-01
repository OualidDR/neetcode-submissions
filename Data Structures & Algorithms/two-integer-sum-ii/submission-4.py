class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1 in range(len(numbers)-1) :
            for index2 in range((index1 +1), len(numbers)) :
                if (numbers[index1] + numbers[index2]) == target :
                    return [numbers[index1], numbers[index2]]



        