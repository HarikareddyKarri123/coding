class Solution:
    def isBalanced(self, root):
        # returns height if balanced, -1 if not balanced
        def check(node):
            if not node:
                return 0
            
            left_h = check(node.left)
            if left_h == -1:
                return -1
            
            right_h = check(node.right)
            if right_h == -1:
                return -1
            
            if abs(left_h - right_h) > 1:
                return -1
            
            return 1 + max(left_h, right_h)
        
        return check(root) != -1
      