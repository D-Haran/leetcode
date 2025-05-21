"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return res
            for i in root.children:
                helper(i)
                res.append(i.val)
            return res
        res = helper(root)
        res.append(root.val) if root else None
        return res
        