from typing import List

class Node:
    def __init__(self, key: int, p = None, l = None, r = None):
        self.left = l
        self.right  = r
        self.parent = p
        self.value = key

class Tree:
    def __init__(self, key):
        self.root = Node(key)



def searchIter(root: Node, key: int):
    cur = root
    while cur:
        if cur.value == key:
            return cur
        elif cur.value > key:
            cur = cur.left
        else:
            cur = cur.right
    print("cannot find the given key:", key)
    return None

def search(root: Node, key: int):
    if not root:
        print("cannot find the given key:", key)
        return None
    if root.value == key:
        return root
    if root.value > key:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
def insert(root: Node, key: int):
    if root.value == key:
        print("given key already exists!")
        return
    if root.value > key:
        if root.left:
            insert(root.left, key)
        else: # left is empty
            root.left = Node(key, root)
    else:
        if root.right:
            insert(root.right, key)
        else:
            root.right = Node(key, root)

def insertIter(root: Node, key: int):
    cur = root
    while cur:
        if cur.value == key:
            print("The given key already exists:", key)
            return
        elif cur.value > key:
            if cur.left:
                cur = cur.left
            else:
                cur.left = Node(key, cur)
                return
        else:
            if cur.right:
                cur = cur.right
            else:
                cur.right = Node(key, cur)
                return

def minimum(root: Node):
    cur = root
    while cur.left:
        cur = cur.left
    return cur
 
def transplant(tree: Tree, u: Node, v: Node): # replace one subtree with another in a binary tree
    if not u.parent: # u is root
        tree.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v:
        v.parent = u.parent

def delete(tree: Tree, key: int):
    cur = search(tree.root, key)
        
    if cur:
        if not cur.left:
            # no left child
            transplant(tree, cur, cur.right) # either right child is empty or not
            
        elif not cur.right:
            # no right child, but has left child
            transplant(tree, cur, cur.left)

        else: # has both children
            succ = minimum(cur.right)
            cur.value = succ.value
            transplant(tree, succ, succ.right)
          

def successor(root: Node):
    if root.right:
        return minimum(root.right)
    
    cur = root    
    while cur.parent and cur.parent.right == cur:
        cur = cur.parent
    if not cur.parent:
        return None
    else:
        return cur.parent
        
def inorder(tree: Tree):
    cur = minimum(tree.root)
    result = []
    while cur:
        result.append(cur.value)
        cur = successor(cur)
    return result


def printBST(tree: Tree):
    print_helper(tree.root, 1)

def print_helper(root: Node, depth: int):
    tab = "   "*depth
    if not root:
        print(tab, "None")
        return
    print_helper(root.right, depth + 1)
    print(tab, root.value)    
    print_helper(root.left, depth + 1)

def arrayToBST(nums: List[int]):
    tree = Tree(nums[0])
    for n in nums[1:]:
        insert(tree.root, n)
    return tree

# tree = arrayToBST([6])
# delete(tree, 6)
# printBST(tree)


tree = arrayToBST([6, 2, 10, 4, 9, 1, 11, 3, 8, 12, 5])
printBST(tree)
#print(inorder(tree))
insert(tree.root, 8.5)
print("==========================================")
printBST(tree)


# print(inorder(tree))

# #print(search(root, 9).value)
delete(tree, 6)
#delete(tree, 2)
#printBST(tree)
# delete(tree, 2)
# #printBST(root)
# delete(tree, 6)
# #insert(tree.root, 9)
# printBST(tree)
# #print(search(root, 2))
