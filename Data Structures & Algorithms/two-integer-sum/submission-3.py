class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # Dictionary to store each number's value -> its index

        for index, value in enumerate(nums): # Iterate through the list with both index and value
            complement = target - value # Calculate the number we need to reach the target

            if complement in dictionary: # If the complement is already in the dictionary, we've found the two numbers that add up to target
                # Return the index of the complement and the current index
                return [dictionary[complement], index] 
            # Store the current number and its index for future lookups
            dictionary[value] = index