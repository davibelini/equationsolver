from Token import Token
from nodes import *

class Parser():
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance() # Goes to first token
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def raise_error(self):
        raise Exception("ERROR: syntax error")

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expression()

        if self.current_token != None:
            self.raise_error()

        return result

    def expression(self): # return an expression
        result = self.term()

        while self.current_token != None and self.current_token.type in ("ADD", "SUBTRACT"): # while loop, because if self.current_token changes the loop breaks 
            if self.current_token.type == "ADD":
                self.advance()
                result = AddNode(result, self.term())

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

            if self.current_token.type == "DIVIDE":
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def power(self):
        pass

    def factor(self):
        token = self.current_token

        if token.type == "NUMBER":
            self.advance()
            return NumberNode(token.value)

        else:    
            self.raise_error()

        return self.power()

    def atom(self):
        token = self.current_token

        if token.type == "NUMBER":
            self.advance()
            return NumberNode(token.value)

        else:    
            self.raise_error()
