# Class Decoration

def add_str_method(cls):
    cls.__str__ = lambda self: f"Custom string for {self.__class__.__name__}"
    return cls

@add_str_method
class MyClass:
    pass

obj = MyClass()
print(str(obj)) 
