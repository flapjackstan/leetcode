"""
Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Notes
-----
Learned about range(start, stop, step) - was used to: for i in range(stop:len(list))
Pattern on using counts as an index
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # below should return {1:3, 2:2, 3:1}
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # I want to have a list with the count as an index
        # and within the content is a list of the values
        # that have that cound

        count_list = [[] for i in range(len(nums) + 1)]
        # should give [[],[],[],[],[],[],[]]

        for number, count in frequency.items():
            count_list[count].append(number)
        # should give [[],[3],[2],[1],[],[],[]]

        result = []
        for count in range(len(count_list) -1, 0, -1):
            for number in count_list[count]:
                result.append(number)

                if len(result) == k:
                    return result



        
