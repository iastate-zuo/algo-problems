'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:

n == ratings.length
1 <= n <= 2 * 10 ** 4
0 <= ratings[i] <= 2 * 10 ** 4
'''

from collections import defaultdict
from typing import List


class Solution:
  def candy(self, ratings: List[int]) -> int:
    nums = []
    n = len(ratings)
    candy = [0] * n
    rp = defaultdict(list)
    
    for i, r in enumerate(ratings):
      if len(rp[r]) == 0:
        nums.append(r)
        
      rp[r].append(i)
      
    nums.sort()
    # print(nums, rp)
    
    for r in nums:
      for pos in rp[r]:
        lc, rc = 0, 0
        if pos > 0 and ratings[pos] > ratings[pos-1]:
          lc = candy[pos-1]
          
        if pos < n-1 and ratings[pos] > ratings[pos+1]:
          rc = candy[pos+1]
          
        candy[pos] = max(lc, rc) + 1
        # print(pos, lc, rc, candy)
        
    # print(candy)
    
    return sum(candy)
  