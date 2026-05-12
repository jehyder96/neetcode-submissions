class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        # get a count of number and occurences
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        # make a pair of the number and frequency
        pairs = []
        for number in dictionary:
            frequency = dictionary[number]
            pairs.append((frequency, number))

        #sort the pair list by descending (most frequent)
        pairs.sort(reverse=True)
        #get the top k frequent elements
        result = []
        for i in range(k):
            result.append(pairs[i][1])
        
        return result