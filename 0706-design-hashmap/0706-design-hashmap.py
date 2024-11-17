class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next
    

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]  # Array of dummy head nodes

    def _hash(self, key):
        return key % len(self.map)
    
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        curr = self.map[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value  # Update existing value
                return
            curr = curr.next
        curr.next = ListNode(key, value)  # Insert new node
    
    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.map[index].next  # Skip dummy node
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1  # Key not found

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.map[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Remove node
                return
            curr = curr.next
