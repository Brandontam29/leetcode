# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def walk(head, path):
    if not head:
        return path

    if head.left:
        walk(head.left, path)

    path.append(head.val)

    if head.right:
        walk(head.right, path)

    return path


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        return walk(root, path)
