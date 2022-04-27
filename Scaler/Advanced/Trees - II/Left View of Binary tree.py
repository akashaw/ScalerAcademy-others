# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import collections

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        q = collections.deque()
        ans = []
        if not A:
            return ans
        q.append(A)
        while q:
            ql = len(q)
            insert_first = True
            for _ in range(ql):
                n = q.popleft()
                if insert_first:
                    ans.append(n.val)
                    insert_first = False
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return ans