# Dunder Function With List 
class CustomList:
    def __init__(self):
        self._data = []

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if index >= len(self._data):
            self._data.extend([None] * (index - len(self._data) + 1))
        self._data[index] = value

# Input
cl = CustomList()
cl[0] = 10
cl[1] = 20
print(cl[0])  # Output: 10
print(cl[1])  # Output: 20
