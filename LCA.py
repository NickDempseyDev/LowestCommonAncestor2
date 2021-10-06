# Lowest Common Ancestor Implementation 2
from BinaryTree import BinaryTree

# translated from the Java implementation to Python
class LCA:

    def __init__(self, fileName):
        self.bst = BinaryTree(fileName)

    def __init__(self, arr):
        self.bst = BinaryTree(arr)

    
    def findPath(self,root,path, k):
    
        if root == None or k == None:
            return False
        
        path.append(root.key)

        if root.key == k:
            return True

        if (root.left != None and self.findPath(root.left,path,k)):
            return True

        if (root.right != None and self.findPath(root.right,path,k)):
            return True

        path.pop()

        return False
    
    def findLCA(self,n1, n2):
    
        path1 = []
        path2 = []
    

        if (not self.findPath(self.bst.root, path1, n1) or not self.findPath(self.bst.root, path2, n2)):
            return None
    
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]