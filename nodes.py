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

class PlusNode():
    def __init__(self, node_a):
        self.node_a = node_a

    def __repr__(self):
        return f"(+{self.node_a})"

class MinusNode():
    def __init__(self, node_a):
        self.node_a = node_a

    def __repr__(self):
        return f"(-{self.node_a})"

class PowerNode():
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a} ^ {self.node_b})"

class VarAssignNode:
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def __repr__(self):
        return f"({self.var_name}={self.var_value})"