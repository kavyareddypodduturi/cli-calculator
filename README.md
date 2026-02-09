# CLI Calculator (Python)

## 📌 Project Overview
This project is a Python command-line calculator that demonstrates
clean software development practices, automated testing, and CI integration.

Key features:

- REPL-based calculator interface
- Unit and parameterized testing using pytest
- 100% test coverage enforcement
- Continuous Integration with GitHub Actions
- Organized professional project structure

---

## 🔁 REPL Interface
The calculator runs in a **Read–Eval–Print Loop**.

### Supported Operations
- `+` → Addition  
- `-` → Subtraction  
- `*` → Multiplication  
- `/` → Division  

Type **`q`** to exit the program.

---

## 📁 Project Structure
```
cli-calculator/
├── src/calculator/        # Calculator logic + REPL
├── tests/                 # Unit tests
├── .github/workflows/     # CI configuration
├── requirements.txt
├── pytest.ini
├── .coveragerc
└── README.md
```

---

## ⚙️ Setup

### Clone repository
```bash
git clone <your-repo-url>
cd cli-calculator
```

### Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Run the calculator
```bash
PYTHONPATH=src python3 src/calculator/repl.py
```

---

## 🧪 Run tests
```bash
pytest
```

### Check coverage
```bash
pytest --cov=calculator --cov-report=term-missing
```

✔ Project enforces **100% test coverage**  
✔ CI fails automatically if coverage drops

---

## 🤖 Continuous Integration
GitHub Actions automatically:

- installs dependencies  
- runs tests  
- verifies 100% coverage  

on every push and pull request.

---

## 🧰 Tech Stack
- Python  
- pytest & pytest-cov  
- GitHub Actions  

---

