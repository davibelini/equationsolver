from Token import Token

numbers = '0123456789'

class Lexer():
    def __init__(self, text):
        self.tokens = []
        self.text = iter(text)
        self.advance()
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
            # print("ERROR: self.current_char is NoneType.")
    def get_number(self):
        points = 0
        string = self.current_char
        self.advance()
        while self.current_char != None and (self.current_char == '.' or self.current_char in numbers):
            if self.current_char == '.':
                points += 1
                if points > 1:
                    break
        
            string += self.current_char
        return Token("NUMBER", float(string))
    def get_tokens(self):
        while self.current_char != None:
            if self.current_char in " \n\t":
                self.advance()
            if self.current_char.isalpha():
                self.tokens.append(Token("VARIABLE", self.current_char))
                self.advance()
            if self.current_char == '=':
                self.tokens.append(Token("EQUAL", self.current_char))
                self.advance()
            if self.current_char in numbers or self.current_char.startswith('.') or self.current_char.endswith('.'):
                self.tokens.append(self.get_number())
                self.advance()
            if self.current_char == '+':
                self.tokens.append(Token("PLUS", self.current_char))
                self.advance()
            if self.current_char == '-':
                self.tokens.append(Token("MINUS", self.current_char))
                self.advance()
            if self.current_char == '*':
                self.tokens.append(Token("MULTIPLY", self.current_char))
                self.advance()
            if self.current_char == '/':
                self.tokens.append(Token("DIVIDE", self.current_char))
                self.advance()
            # TODO: Continue(parenthesis)
        return self.tokens