# 🔑 Password Checker

## I. Introduction

**Password Checker** is a simple web app (Python Flask) that helps you:
- Check if your password is strong or weak.
- Find out if your password was leaked using haveibeenpwned.com.
- **Your password is never saved or sent anywhere else.** Privacy is safe.

## II. Features

- Check password strength (entropy, security rules).
- Check if password is leaked in big password leak lists.
- Give suggestions to make your password stronger.
- Simple and easy web interface. Works on desktop and phone.
- No real password is stored or sent outside.

## III. Technology Used

- **Backend:** Python 3.x, Flask
- **Frontend:** HTML, CSS, JavaScript (simple)
- **API:** Use haveibeenpwned.com to check leaks

## IV. Installation Guide (with venv)

### 1. Clone the code

```sh
git clone https://github.com/username/password-checker.git
cd password-checker
```

### 2. Create and activate virtual environment (venv)

**Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install requirements

```sh
pip install -r requirements.txt
```

### 4. Run the app

```sh
python app.py
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 5. Stop venv (optional)
```sh
deactivate
```

## V. How to use

1. Type your password in the box.
2. Click the "Check" button.
3. You will see if your password is strong or weak, and if it was leaked before.
4. **Tip:** Do not use your real password if you worry about privacy.

## VI. Demo (Screenshot)

*(Add your image here if you have one)*

## VII. Project Structure

```
password-checker/
├── app.py
├── requirements.txt
├── utils/
│   ├── strength_check.py
│   └── validate.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## VIII. How to contribute

- You can fork this project or send a pull request to add new ideas!
- Use GitHub Issues for bugs or questions.

## IX. License

MIT License – Free to use for any purpose.

## X. Security Note

> **The password you enter is not saved or sent anywhere.**  
> It is only used to check if it is strong or weak, and check leaks using [haveibeenpwned.com](https://haveibeenpwned.com/).  
> Please do not use your real password if you feel unsafe.
