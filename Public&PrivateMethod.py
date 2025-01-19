# Public & Private Method 
class MyClass:
    def __init__(self, value):
        self.value = value

    def __private_method(self):
        return f"Private value is {self.value}"

    def public_method(self):
        return self.__private_method()

# input
obj = MyClass(42)
print(obj.public_method())
