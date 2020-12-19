from Token import Token

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
                self.advance()
            elif self.current_char == '+': # Add
                self.tokens.append(Token("ADD"))
                self.advance()
            elif self.current_char == '-': # Subtract
                self.tokens.append(Token("SUBTRACT"))
                self.advance()
            elif self.current_char == '*': # Multiply
                self.tokens.append(Token("MULTIPLY"))
                self.advance()
            elif self.current_char == '/': # Divide
                self.tokens.append(Token("DIVIDE"))
                self.advance()
            elif self.current_char == 'q': # Quit
                self.tokens.append(Token("QUIT"))
                quit()
            elif self.current_char != 'q' and self.current_char.isalpha():
                self.tokens.append(Token("VARIABLE", self.current_char))
                self.advance()
            elif self.current_char == '=':
                self.tokens.append(Token("EQUAL"))
                self.advance()
        return self.tokens