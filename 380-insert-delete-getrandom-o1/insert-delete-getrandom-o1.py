import random

class RandomizedSet:

    def __init__(self):
        self.vals = []  # List to store elements
        self.vals_map = {}  # Dictionary to store the indices of elements

    def insert(self, val: int) -> bool:
        if val in self.vals_map:
            return False
        self.vals_map[val] = len(self.vals)  # Map value to its index in the list
        self.vals.append(val)  # Add value to the list
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals_map:
            return False
        last_val = self.vals[-1]  # Get the last element in the list
        idx_to_remove = self.vals_map[val]  # Get the index of the element to remove
        self.vals[idx_to_remove] = last_val  # Swap the last element with the element to remove
        self.vals_map[last_val] = idx_to_remove  # Update the index of the last element in the map
        self.vals.pop()  # Remove the last element from the list
        del self.vals_map[val]  # Remove the element from the map
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)  # Return a random element from the list

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
