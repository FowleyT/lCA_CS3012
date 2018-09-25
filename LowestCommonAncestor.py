class Node:
    # Constructor
    def __init__(self, key):
        self.key =  key
        self.right = None
        self.left = None
 def Path( root, path, k):
     path.append(root.key)
     if root.key == k :
        return True
     if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True
     path.pop()
    return False
 def findLCA(root, n1, n2):
     path1 = []
    path2 = []
     if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
     i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
