'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 10^4
-10^4 < xi, yi < 10^4
'''


class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    p = [(x*x+y*y, x, y) for x, y in points]
    # print(p)
    
    def kth(i: int, j: int, k: int):
      if j-i+1 == k:
        return
      
      high, low = max(p[i:j+1])[0], min(p[i:j+1])[0]
      pivot = (high + low) / 2.0
      l, r = i, j
      
      while l < r:
        while l <= j and p[l][0] <= pivot:
          l += 1
          
        while r >= i and p[r][0] > pivot:
          r -= 1
          
        if l >= r:
          break
          
        p[l], p[r] = p[r], p[l]
        
      count = r-i+1
      if count == k:
        return 
      
      if count > k:
        kth(i, r, k)
      else:
        kth(l, j, k-count)
    
    # arrange the array
    kth(0, len(points)-1, k)
    
    # extract points
    return [[x, y] for _, x, y in p[:k]]
  
  
  def kClosest0(self, points: List[List[int]], k: int) -> List[List[int]]:
    q = []
    
    for x, y in points:
      d = x*x + y*y
      # print(q, d)
      
      if len(q) < k or -d > q[0][0]:
        if len(q) == k:
          heappop(q)
          
        heappush(q, (-d, x, y))
    
    return [[p[1], p[2]] for p in q]
  
