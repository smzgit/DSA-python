# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        self.res = float('-inf')

        def solve(root):
            if not root:
                return 0

            l = solve(root.left)
            r = solve(root.right)

            temp = max(max(l, r) + root.val, root.val) # when node is part of path or ending node of path
            ans = max(temp, (root.val + l + r)) # when node is itself root in path
            self.res = max(self.res, ans)
            return temp

        solve(root)
        return self.res


def solve(root):
    max_sm = float('-inf')

    def dfs(node):
        if not node:
            return 0

        left=max(0,dfs(node.left))
        right=max(0,dfs(node.right))
        nonlocal max_sm
        print(max_sm)
        max_sm=max(max_sm,left+right+node.val)
        return max(left,right)+node.val

    dfs(root)
    return max_sm

if __name__ == '__main__':
    r=TreeNode(-10)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    r.right.left = TreeNode(15)
    r.right.right = TreeNode(7)
    ans=Solution().maxPathSum(r)
    print(f'max sum = {ans}')
    print(f'max sum = {solve(r)}')