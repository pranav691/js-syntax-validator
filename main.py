from lexer import lexer
from parser import parser

syntax_examples = {
    '1': """Correct Syntax (Variable Declaration):
let x = 10;
var name = "Abhi";
const pi = 3.14;
""",

    '2': """Correct Syntax (Object Declaration):
let obj = { "name": "Abhi", "age": 20 };

""",

    '3': """Correct Syntax (Function Declaration):
function greet() { }
""",

    '4': """Correct Syntax (Class Declaration):
class Person { }
""",

    '5': """Correct Syntax (Try-Catch Statement):
try {
} catch(e) {
}
"""
}

def show_menu():
    print("\n1. Variable Declaration")
    print("2. Object Declaration")
    print("3. Function Declaration")
    print("4. Class Declaration")
    print("5. Try-Catch Statement")
    print("6. Exit\n")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '6':
        break

    if choice not in syntax_examples:
        print("Invalid choice")
        continue

    js_code = input("\nEnter JavaScript code:\n")

    try:
        parser.parse(js_code)
        print("Syntax Accepted")
    except SyntaxError:
        print("Syntax Error\n")
        print(syntax_examples[choice])

 
"""

var x = 10;
let obj = { "key" :"value" };
function greet() { }
class Student { }
try { } catch(error) { }

"""