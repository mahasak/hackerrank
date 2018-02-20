""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys
def checkTree(root, left, right):
    if root == None:
        return True
    if root.data >= right or left >= root.data:
        return False
    return checkTree(root.left, left, root.data) and checkTree(root.right, root.data, right)

def checkBST(root):
    return checkTree(root, -sys.maxsize -1, sys.maxsize)
