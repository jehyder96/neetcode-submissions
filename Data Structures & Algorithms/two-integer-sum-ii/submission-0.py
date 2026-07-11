class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Explore: 
        So, we're given an array of numbers and we need to return the indices of two numbers that
        add up to a given target number

        Some constraints are that index 1 and index 2 ([index1, index2]) must be less than AND cannot
        be equal

        Lastly, there will always be exaclty one valid solution

        Brainstorm:

        We need to solve this using a two pointer approach

        plan:
        """

        i = 0
        j = len(numbers) - 1

        while i < j:
            target_sum = numbers[i] + numbers[j]

            if target_sum == target:
                return[i + 1, j + 1]
            elif target_sum < target:
                i += 1
            else:
                j -= 1
        return []