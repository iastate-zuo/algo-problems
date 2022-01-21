'''
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

Example 1:

Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:

Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:

Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 10^6
1 <= startDayi <= endDayi <= 10^9
1 <= valuei <= 10^6
'''


from typing import List
from functools import lru_cache
from bisect import bisect_right


class Solution:
  def maxValue(self, events: List[List[int]], k: int) -> int:
    events.sort()
    start_time = [e[0] for e in events]
    # print(events, start_time)
    
    @lru_cache(None)
    def attend(i: int, k: int) -> int:
      if k == 0 or i >= len(events):
        return 0
      
      # if attending i-th event
      j = bisect_right(start_time, events[i][1])
      score0 = events[i][2] + attend(j, k-1)
      # print('attend', i, k, j)
      
      # if not attending i-th event
      score1 = attend(i+1, k)
      
      return max(score0, score1)
      
    return attend(0, k)
  