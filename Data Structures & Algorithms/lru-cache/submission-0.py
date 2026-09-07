class ListNode:
    def __init__(self, key,val, prev, nxt):
        self.val = val
        self.prev = prev
        self.next = nxt
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.last = ListNode(0,0,None,None) # Least recently used
        self.first = ListNode(0,0,self.last, None) # Most recently used
        self.last.next = self.first
        self.nodeDict = {}

    def get(self, key: int) -> int:

        if key not in self.nodeDict:
            return -1
        
        node = self.nodeDict[key]
        # remove the node from where it is in the list
        node.prev.next = node.next
        node.next.prev = node.prev

        # and move it to the top
        self.first.prev.next = node
        node.prev = self.first.prev
        self.first.prev = node
        node.next = self.first
        return node.val
        

    def put(self, key: int, value: int) -> None:

        # Purge the last if we're over the limit
        if len(self.nodeDict) >= self.capacity:
            tmp = self.last.next
            self.last.next = tmp.next
            tmp.next.prev = self.last
            del self.nodeDict[tmp.key]
        
        if key in self.nodeDict:
            node = self.nodeDict[key]
            node.prev.next = node.next
            node.next.prev = node.prev

        newNode = ListNode( key,value, self.first.prev, self.first)
        self.first.prev.next = newNode
        self.first.prev = newNode

        self.nodeDict[key] = newNode