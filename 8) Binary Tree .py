# ---------------------------------------------
# درخت دودویی
# ---------------------------------------------

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def sum_tree(root):
    if root is None:
        return 0
    return root.data + sum_tree(root.left) + sum_tree(root.right)

def search_tree(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    return search_tree(root.left, target) or search_tree(root.right, target)

def max_tree(root):
    if root is None:
        return float("-inf")
    return max(root.data, max_tree(root.left), max_tree(root.right))
