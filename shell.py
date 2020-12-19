from lexer import Lexer

version = '0.0.1'
print("equationsolver@{}".format(version))

while True:
    text = input('solve > ')
    lexer1 = Lexer(text)
    tokens = lexer1.generate_tokens()
    print(tokens)