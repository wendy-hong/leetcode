# class TreeNode:
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        ans = []
        def preorder(root):
            if not root:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans

    def postorderTraversal(self, root: TreeNode):
        ans = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return ans

    def inorderTraversal(self, root: TreeNode):
        if not root: return []
        stack = [root]
        res = []
        while stack:
            while root.left:
                stack.append(root.left)
                root = root.left
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
                root = cur.right
        return res
