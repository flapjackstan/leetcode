"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

1. Go over test cases and confirm you understand
I can onlt iterate over the array a few times for this to be O(n), i cant go back and forth after each item
in example 1
0: 2x3x4
1: 1x3x4
...
in example 2
0: 0x9x0x0

2. Give initial naive solution even if wrong.

index 0 i can take product of everything to the right
index 1 i can take product of left and product of right
index -1 i can take product of everything left

1. left temp array
2. right temp array
3. loop through nums

Here I realized that this method would be O(n2)

2a. If you get that weird feeling that youre not getting to the solution ask the interviewer for thoughts

If i take a rolling product from left and right, for the index being evaluated i can multiply the
left and right index of the rolling product to get the product of every thing up to that index

2b. Whiteboard Example


3: Program

4: Run / Debug

5: What is the space time complexity

Notes
-----
Bidirectional cumulative product is used when looping over the array.
That way when youre at the index being evaluated, the index to the left has
the product of everything up to that index, and  
"""
from typing import List
import logging

def setup_logging(debug=False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s - %(message)s")


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        logger = logging.getLogger(__name__)

        logger.debug("Checkpoint 1")

        # Your code here
        logger.debug("Checkpoint 2")

        # More code
        logger.debug("Final checkpoint")

        return nums

def main():
    setup_logging(debug=True)
    nums = [1,2,3,4]

    solver = Solution()
    answer = solver.product_except_self(nums)

    expected = [24,12,8,6]
    
    try:
        assert answer == expected
    except AssertionError:
        print(f"{answer} != {expected}")


if __name__ == "__main__":
    main()