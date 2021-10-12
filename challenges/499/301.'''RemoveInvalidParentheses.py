'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''


from typing import List


class Solution:
  '''
  idea is to record the number of '(' and ')' to be deleted, and then try
  all the combos of deleting/keeping the brackets. note that for ')', there
  must be equal or more '(' prior to make the case legal.
  '''
  def removeInvalidParentheses(self, s: str) -> List[str]:
    h, t = 0, len(s)-1
    pre, suf = '', ''

    # popping all the illegal ')' from the front of the string
    while h < len(s) and s[h] != '(':
      if s[h] != ')':
        pre += s[h]

      h += 1

    # popping all the illegal '(' from the tail of the string
    while t > h and s[t] != ')':
      if s[t] != '(':
        suf = s[t] + suf

      t -= 1
      
    s = s[h:t+1]
    if not s:
      return [pre+suf]
    
    # calculate the number of '(' and ')' to be deleted
    l, r = 0, 0
    for ch in s:
      if ch == '(':
        l += 1
      elif ch == ')':
        if l > 0:
          l -= 1
        else:
          r += 1
      
    # print(s, l, r)
    stack = set([('', l, r, 0)])
    nxt = set()
    bound = len(s) - l - r
    
    for ch in s:
      for curr, l, r, opened in stack:
        if ch == '(':
          # option 1: skip
          if l > 0:
            nxt.add((curr, l-1, r, opened))

          # option 2: don't skip
          if len(curr)+1 <= bound:
            nxt.add((curr+ch, l, r, opened+1))
            
        elif ch == ')':
          # option 1: skip
          if r > 0:
            nxt.add((curr, l, r-1, opened))
          
          # option 2: add and increase
          if len(curr)+1 <= bound and opened > 0:
            nxt.add((curr+ch, l, r, opened-1))
          
        else:
          nxt.add((curr+ch, l, r, opened))
          
      stack, nxt = nxt, stack
      nxt.clear()
      
    # print(stack)
    ans = []
    
    for res, l, r, _ in stack:
      if not l and not r:
        ans.append(pre+res+suf)
    
    return ans
    