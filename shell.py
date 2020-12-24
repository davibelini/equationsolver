import os
from lexer import Lexer
import os
os.system('cls' if os.name == 'nt' else 'clear')

version = '0.0.1'
print("equationsolver@{}".format(version))

while True:
    text = input('solve > ')
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(tokens)