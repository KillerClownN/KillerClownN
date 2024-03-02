#write a proram to find the height of the tree and print the tree in zig zag manner
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
def treeheight(root):
    if not root:
        return 0
    leftheight = treeheight(root.left)
    rightheight = treeheight(root.right)
    return max(leftheight, rightheight) + 1

def print_zigzag_tree(root):
    if not root:
        return

    current_level = [root]
    level_number = 1
    while current_level:
        if level_number % 2 == 1:
            for node in current_level:
                print(node.val, end=" ")
        else:
            for node in reversed(current_level):
                print(node.val, end=" ")

        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        current_level = next_level
        level_number += 1
        print()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Height of the tree:", treeheight(root))
print("Tree in zigzag order:")
print_zigzag_tree(root)
