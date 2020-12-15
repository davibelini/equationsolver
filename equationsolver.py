from lexer import Lexer

### equationsolver.py
version = '0.0.1'
print(f"equationsolver@{version}")
# print("hi.")
# print("example: 'eqationsolver > x = (10 - 5)'\n")
while True:
    text = input("equationsolver > ")
    lexer = Lexer(text)
    print(lexer.get_tokens())
    if text == 'exit' or text =='quit' or text == 'q':
        quit()
        break

### equationsolver.py