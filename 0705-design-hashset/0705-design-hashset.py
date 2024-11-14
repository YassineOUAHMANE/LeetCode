class MyHashSet:
    def __init__(self):
        self.capacity = 100  # Array size
        self.keys = [[] for _ in range(self.capacity)]  # List of lists for separate chaining

    def _hash(self, key: int) -> int:
        return hash(key) % self.capacity  # Simple hash function

    def add(self, key: int) -> None:
        index = self._hash(key)
        # Check if key already exists at the index
        if key not in self.keys[index]:
            self.keys[index].append(key)  # Add key to the appropriate bucket

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.keys[index]:
            self.keys[index].remove(key)  # Remove key from the appropriate bucket

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.keys[index]  # Check if key exists at the index
