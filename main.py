import os
from lexer import Lexer
from parse import Parser
import os
from version import *
os.system('cls' if os.name == 'nt' else 'clear')

print("equationsolver@{}".format(version))

while True:
    text = input('solve > ')
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    ast = Parser(tokens).parse()
    if not ast: continue
    print(ast)