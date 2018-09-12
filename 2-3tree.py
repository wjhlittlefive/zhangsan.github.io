class Node:
    def __init__(self, key1,key2 = None, key3 = None,left=None, right=None, right2 = None,middle = None, p=None):
        self.left = left
        ## 当节点为3-节点时，right为节点的右子树
        self.right = right
        ## 当节点为2-节点时middle为节点的右子树
        self.middle = middle
        ## 这个为临时4-节点的最右子树
        self.right2 = right2
        self.key1 = key1
        self.key2 = key2
        ## 这个节点是作为一个临时节点它用来存储从3-节点增加的那个节点
        self.key3 = key3 
        self.p = p
        ## 如果这个键为空的话那么它的父节点为它自己
        if key1 == "NIL":
            self.p = self
    def getChild(self,key):
        if key<self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key < self.key2:
            return self.middle
        else :
            
            return self.right
class Tree:
    def __init__(self):
        nil = Node("NIL")
        self.root = nil
        self.nil = nil
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self._get(self.root, key)
    def _get(self, node, key):
        if node is None:
            return None
        elif node.hasKey(key):
            return node
        else:
            child = node.getChild(key)
            return self._get(child, key)
    
    ## 直接插入不管fixup
    def insert(self , T ,x):
        if T.root.key1 == "NIL":
            T.root = Node(x)
        else:
            y = T.root
            while y.isLeaf() == False:
                print ("y",y.key1)
                y = y.getChild(x)
                print ("x",y)
            if y.key2 is not None:
                if x < y.key1:
                    y.key3 = y.key2
                    y.key2 = y.key1
                    y.key1 = x
                elif (x>y.key1 and x<y.key2):
                    y.key3 = y.key2
                    y.key2 = x
                else:
                    y.key3 = x
                print ("y.p",y.p)
                self.insertFixUp(T,y)
            else:
                if x < y.key1:
                    y.key2 = y.key1
                    y.key1 = x
                else :
                    y.key2 = x
    
    ## 插入的时候把4-节点变成符合2-3树的2/3节点
    def insertFixUp(self,T,x):
        ## case 1
        if x.p == None:
            print ("x == T.root")
            T.root = Node(x.key2)
            T.root.left = Node(x.key1)
            T.root.left.p = T.root
            T.root.middle = Node(x.key3)
            T.root.middle.p = T.root
    
            if T.root.left is not None:
                T.root.left.left = x.left
                if T.root.left.left is not None:
                    T.root.left.left.p = T.root.left
                T.root.left.middle = x.middle
                if T.root.left.middle is not None:
                    T.root.left.middle.p = T.root.left
            if T.root.middle is not None:
                T.root.middle.left = x.right
                if  T.root.middle.left is not None :
                     T.root.middle.left.p = T.root.middle
                T.root.middle.middle = x.right2
                if  T.root.middle.middle is not None :
                    T.root.middle.middle.p = T.root.middle
            return
        ## case 2
        if x.p.key2 is None:
            ## 在 左侧插入
            print ("case2执行")
            z = x.p
            print(x.key1)
            if x is x.p.left:
                print ("case2 从左侧插入")
                z.key2 = z.key1
                z.key1 = x.key2
                z.left = Node(x.key1)
                z.right = z.middle
                z.middle = Node(x.key3)
                z.left.p = z
                z.middle.p = z
                if x.left is not None:
                    z.left.left = x.left
                    z.left.left.p = z.left
                if x.middle is not None :
                    z.left.middle = x.middle
                    z.left.middle.p = z.left
                if x.right is not None:
                    z.middle.left = x.right
                    z.middle.left.p = z.middle
                if x.right2 is not None:
                    z.middle.middle = x.right2
                    z.middle.middle.p = z.middle
            ## 在右侧插入
            else:
                print("右侧插入执行")
                z.key2 = x.key2
                z.middle = Node(x.key1)
                z.right = Node(x.key3)
                z.middle.p = z
                z.right.p = z
                if x.left is not None:
                    z.middle.left = x.left
                    z.middle.left.p = z.middle
                if x.middle is not None:
                    z.middle.middle = x.middle
                    z.middle.middle.p = z.middle
                if x.right is not None :
                    z.right.left = x.right
                    z.right.left.p = z.middle
                if x.right2 is not None:
                    z.right.middle = x.right2
                    z.right.middle.p = z.right
            return
        if x.p.key2 is not None:
            z = x.p
            #在左侧插入
            if x is z.left:
                z.key3 = z.key2
                z.key2 = z.key1
                z.key1 = x.key2
                z.right2 = z.right
                z.right2.p = z
                z.right = z.middle
                z.middle = Node(x.key3)
                z.left = Node(x.key2)
                z.left.p = z
                z.middle.p = z
                z.left.left = x.left
                z.left.left.p = z.left
                z.left.right = x.middle
                z.left.right.p = z.left
                z.middle.left = x.right
                z.middle.left.p = z.middle
                z.middle.right = x.right2
                z.middle.right.p = z.middle
            # 在中间插入
            if x is z.middle:
                z.key3 = z.key2
                z.key2 = x.key2
                z.right2 = z.right
                z.right2.p = z
                z.right = Node(x.key3)
                z.right.p = z
                z.right.left = x.right
                z.right.left.p = z.right
                z.right.right = x.right2
                z.right.right.p = z.right
                z.middle = Node(x.key1)
                z.middle.p = z
                z.middle.left = x.left
                z.middle.left.p = z.middle
                z.middle.right = x.middle
                z.middle.right.p = z.middle
            # 从右侧插入
            if x is z.right:
                z.key3 = x.key2
                z.right2 = Node(x.key3)
                z.right2.p = z
                z.right2.left = x.right
                z.right2.right = x.right2
                if z.right2.left is not None:
                    z.right2.left.p = z.right2 
                if z.right2.right is not None:
                    z.right2.right.p = z.right2
                z.right = Node(x.key1)
                z.right.left = x.left
                z.right.right = x.middle
                if z.right.left is not None:
                    z.right.left.p = z.right
                if z.right.left is not None:
                    z.right.right.p = z.right
        self.insertFixUp(T,z)
