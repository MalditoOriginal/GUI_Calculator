# 🧮 GUI Calculator

A modern calculator application built with Python using the MVVM (Model-View-ViewModel) architecture pattern.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 Basic Arithmetic | Addition, subtraction, multiplication, division |
| 🔢 Decimal Support | Accurate decimal number handling |
| ⚠️ Error Handling | Division by zero detection and error display |
| ⌨️ Keyboard Support | Full keyboard input support |
| 🎨 Clean UI | Simple and intuitive graphical interface |

---

## 🏗️ Architecture

The application follows the **MVVM** pattern:

| Component | File | Description |
|-----------|------|-------------|
| **Model** | [`calculator_model.py`](calculator_model.py) | Core calculation logic and expression evaluation |
| **ViewModel** | [`calculator_viewmodel.py`](calculator_viewmodel.py) | Manages UI state and handles user commands |
| **View** | [`calculator_view.py`](calculator_view.py) | Graphical user interface using tkinter |

---

## 📋 Requirements

- **Python**: 3.6 or higher
- **Dependencies**: None (uses standard library only)

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/MalditoOriginal/GUI_Calculator.git
cd GUI_Calculator
```

### Run the Calculator

```bash
python main.py
```

---

## 🎮 Usage

### Mouse/Click Input

| Button | Action |
|--------|--------|
| `0-9` | Enter digits |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `=` | Calculate result |
| `C` | Clear all |
| `CE` | Clear entry |
| `⌫` | Backspace |
| `±` | Toggle sign |
| `.` | Decimal point |

### Keyboard Input

| Key | Action |
|-----|--------|
| `0-9` | Enter digits |
| `+ - * /` | Select operator |
| `Enter` | Calculate result |
| `Esc` | Clear all |
| `Backspace` | Delete last character |
| `.` | Decimal point |

---

## 📐 Division Logic Improvements

The calculator includes several improvements to division operations:

| Improvement | Description |
|-------------|-------------|
| 🔍 Division-by-zero Detection | Enhanced regex pattern to detect `/0`, `/0.0`, `/00`, `/0.00`, etc. |
| 📱 Decimal Input Validation | Robust handling of decimal points in complex expressions |
| 🧮 Floating-point Precision | Uses Python's `Decimal` module for precise division results |

---

## 🧪 Testing

Run the test suite to verify functionality:

```bash
python test_calculator.py
```

---

## 📁 Project Structure

```
GUI_Calculator/
├── calculator_model.py      # Core calculation logic
├── calculator_view.py       # GUI implementation
├── calculator_viewmodel.py  # MVVM ViewModel
├── main.py                  # Entry point
├── test_calculator.py       # Unit tests
├── CMakeLists.txt           # C++ build config (for reference)
├── optimized_calculator.cpp # C++ implementation (for reference)
├── optimized_calculator.hpp # C++ header (for reference)
├── *.md files               # Documentation
└── .gitignore
```

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 🙏 Acknowledgments

- Optimized C++ implementation included for performance comparison
- Build instructions for C++ version available in [`COMPILATION_INSTRUCTIONS.md`](COMPILATION_INSTRUCTIONS.md)

---

<div align="center">
  <sub>Built with ❤️ using Python and tkinter</sub>
</div>
