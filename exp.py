
class Val(object):
    __slots__ = ['value']
    def __init__(self, v = 0):
        self.value = v
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value
    
e = Val(1)
e.eval()

class Add(object):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()

e = Add(Val(1), Val(2))
assert e.eval() == 3
print(e.eval())
e = Add(Val(1),Add(Val(2),Val(3)))
assert e.eval() == 6
print(e.eval())
