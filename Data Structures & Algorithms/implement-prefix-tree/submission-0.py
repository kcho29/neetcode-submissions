class TreeNode:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []
        self.isEnd = False
    
    def addChild(self, newNode):
        self.children.append(newNode)
    
    def childrenContain(self, query):
        for child in self.children:
            if child.value == query:
                return True
        return False
    
    def getChild(self, query):
        for child in self.children:
            if child.value == query:
                return child
    
    def hasChildren(self):
        return len(self.children) != 0
    
    def setEnd(self, value):
        self.isEnd = value

class PrefixTree:

    def __init__(self):
        self.root = TreeNode(None, None)
        

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if not cur.childrenContain(letter):
                newNode = TreeNode(letter, cur)
                cur.addChild(newNode)
                cur = newNode
            else:
                cur = cur.getChild(letter)
        cur.setEnd(True)

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if not cur.childrenContain(letter):
                return False
            cur = cur.getChild(letter)
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if not cur.childrenContain(letter) or not cur.hasChildren():
                return False
            cur = cur.getChild(letter)
        return True
        
        