from Token import Token
import os

class Lexer():
    def __init__(self, text):
        self.text = iter(text)
        self.current_char = None
        self.advance()
    def advance(self):
        try:
            self.current_char = next(self.text) # First next() goes to first element
        except StopIteration:
            self.current_char = None
    def generate_number(self):
        points = 0
        number = ''
        while self.current_char != None and (self.current_char == '.' or self.current_char.isnumeric()):
            if self.current_char == '.':
                points += 1
                if points > 1:
                    print(f"Too many decimal points in one number: '{points}'")
                    exit()
            number += self.current_char
            self.advance()
        if points > 0:
            if number.startswith('.'):
               number = '0' + number
            return Token("NUMBER", float(number))
        return Token("NUMBER", int(number))
    def generate_tokens(self):
        self.tokens = []
        while self.current_char != None:
            if self.current_char in ' \t\n':
                self.advance()
            elif self.current_char.isnumeric() or self.current_char == '.':
                self.tokens.append(self.generate_number())
            elif self.current_char == '+': # Add
                self.advance()
                self.tokens.append(Token("ADD"))
            elif self.current_char == '-': # Subtract
                self.advance()
                self.tokens.append(Token("SUBTRACT"))
            elif self.current_char == '*': # Multiply
                self.advance()
                self.tokens.append(Token("MULTIPLY"))
            elif self.current_char == '/': # Divide
                self.advance()
                self.tokens.append(Token("DIVIDE"))
            elif self.current_char == 'q': # Quit
                quit()
            elif self.current_char != 'q' and self.current_char.isalpha():
                self.tokens.append(Token("VARIABLE", self.current_char))
                self.advance()
            elif self.current_char == '=':
                self.advance()
                self.tokens.append(Token("EQUAL"))
            elif self.current_char == '(':
                self.advance()
                self.tokens.append(Token("LPAR"))
            elif self.current_char == ')':
                self.advance()
                self.tokens.append(Token("RPAR"))
            else:
                return f"ERROR: illegal character '{self.current_char}'"
        return self.tokens