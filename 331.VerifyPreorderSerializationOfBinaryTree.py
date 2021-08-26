class Solution:
  def isValidSerialization(self, preorder: str) -> bool:
    if not preorder:
      return True
    
    stack = []
    for val in preorder.split(','):
      while val == '#' and stack and stack[-1] == '#':
        # pop the 'left' branch
        stack.pop()
        
        # if there's no parent node to the 2 null nodes, invalid tree
        if not stack:
          return False
        
        # pop the parent, since it's valid from this node blow
        stack.pop()
        
      # use the placeholder to mark the tree as either valid (i.e. '#'), or
      # has a value to the left
      stack.append(val)
    
    return stack == ['#']
  
    
  def isValidSerialization0(self, preorder: str) -> bool:
    arr = [int(s) if s != '#' else -1 for s in preorder.split(',')]
    # print(arr)
    
    def is_valid(i: int) -> Tuple[bool, int]:
      j = len(arr)-1
      
      if i > j:
        return (False, i)
      
      if i == j and arr[i] == -1:
        return (True, i)
      
      if arr[i] == -1:
        return (True, i)
      
      lv, li = is_valid(i+1)
      
      if not lv:
        return (False, li)
      
      return is_valid(li+1)
      
    valid, end = is_valid(0)
    # print(valid, end)
    
    return (valid and end == len(arr)-1)
  
