# Dunder Function
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value + other.value)
        return NotImplemented

    def __repr__(self):
        return f"CustomNumber({self.value})"

# input
num1 = CustomNumber(10)
num2 = CustomNumber(20)
result = num1 + num2
print(f"Result of addition: {result}")
