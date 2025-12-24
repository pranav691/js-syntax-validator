# JS Syntax Validator  
A mini JavaScript syntax validator built using **Python PLY (Lex–Yacc)**.  
This project demonstrates how a compiler frontend works by implementing a custom **lexer** and **parser** that validate specific JavaScript constructs.

---

## 🚀 Features

### ✔ Custom Lexer  
Built using **PLY Lex** to tokenize:
- Keywords (`var`, `let`, `const`, `function`, `class`, `try`, `catch`)
- Identifiers  
- Numbers  
- Strings  
- Symbols (`{}`, `()`, `:`, `,`, `;`, `=`)

### ✔ Custom Parser  
Using **PLY Yacc**, the parser validates:
- Variable declarations  
- Object literals  
- Function declarations  
- Class declarations  
- Try–catch statements  

### ✔ Syntax Validation  
The program accepts JavaScript code and reports:
- `Syntax Accepted`  
or  
- `Syntax Error` (with examples)

---

## 📁 Project Structure

```
js-syntax-validator/
│
├── lexer.py      # Converts raw JS code into tokens
├── parser.py     # Grammar rules using PLY Yacc
├── main.py       # User menu + input handling
│
├── README.md     # Project documentation
├── LICENSE       # MIT License
└── .gitignore    # Python ignore rules
```

---

## 🔧 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/js-syntax-validator.git
cd js-syntax-validator
```

### 2️⃣ Install dependencies
```bash
pip install ply
```

---

## ▶️ Usage

Run the main program:
```bash
python main.py
```

You will see a menu:

```
1. Variable Declaration
2. Object Declaration
3. Function Declaration
4. Class Declaration
5. Try-Catch Statement
6. Exit
```

Enter any JavaScript code and the parser will validate it.

---

## 🧪 Example

### Input:
```javascript
let x = 10;
```

### Output:
```
Syntax Accepted
```

---

## 🌟 Future Enhancements
Potential improvements:
- Support nested objects  
- Support function parameters  
- Add if–else statements  
- Add while/for loops  
- Develop a GUI version  
- Add detailed error messages (line number, expected token)  

---

## 🏗️ Tech Stack
- **Python**
- **PLY (Lex–Yacc)**
- **Compiler Design Concepts**
- **JavaScript Syntax Rules**
