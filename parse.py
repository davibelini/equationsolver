from Token import Token
from nodes import *

class Parser():
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def raise_error(self):
        print("ERROR: syntax error")
        return 1

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expression()

        if self.current_token != None:
            self.raise_error()

        return result

    def expression(self): # return an expression
        if self.current_token.type == "VARIABLE":
            var_name = self.current_token.value
            self.advance()
            if self.current_token.type != "EQUAL":
                self.raise_error(); return
            var_value = self.expression()
            return VarAssignNode(var_name, var_value)

        result = self.term()

        while self.current_token != None and self.current_token.type in ("ADD", "SUBTRACT"): # while loop, because if self.current_token changes the loop breaks 
            if self.current_token.type == "ADD":
                self.advance()
                result = AddNode(result, self.term())
                if not self.current_token: return result

            if self.current_token.type == "SUBTRACT":
                self.advance()
                result = SubtractNode(result, self.term())

        return result
        
    def term(self): # return a term
        result = self.factor()

        while self.current_token != None and self.current_token.type in ("MULTIPLY", "DIVIDE"):
            if self.current_token.type == "MULTIPLY":
                self.advance()
                result = MultiplyNode(result, self.factor())
                if not self.current_token: return result

            if self.current_token.type == "DIVIDE":
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def power(self):
        result = self.atom()

        while self.current_token != None and self.current_token.type == "POWER":
            self.advance()
            result = PowerNode(result, self.factor())

        return result

    def factor(self):
        if self.current_token == "PLUS":
            self.advance()
            return PlusNode(self.atom())

        if self.current_token == "MINUS":
            self.advance()
            return MinusNode(self.atom())

        return self.power() # else
    def atom(self):
        token = self.current_token

        if token.type == "NUMBER":
            self.advance()
            return NumberNode(token.value)

        if token.type == "LPAREN":
            self.advance()
            result = self.expression()
            if self.current_token.type != "RPAREN":
                self.raise_error()
            
            return result

        else:    
            self.raise_error()
