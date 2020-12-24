# The purpose of nodes is that when the interpreter analises the nodes it knows what operation to do.

class NumberNode():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"({self.value})"

class AddNode():
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"

class SubtractNode():
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a} - {self.node_b})"

class MultiplyNode():
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"

class DivideNode():
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"

class PowerNode():
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a} ^ {self.node_b})"