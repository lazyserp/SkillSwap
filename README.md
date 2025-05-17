# SkillSwap

SkillSwap is a Flask-based web application that enables users to register, log in, and exchange skills by sharing what they can teach and what they want to learn. It’s a community-driven learning platform where users can connect based on their knowledge and interests.

---

## 🚀 Features

- ✅ User registration with:
  - Username, date of birth, gender
  - Skills offered and skills needed
  - Short personal bio
- 🔐 Secure login with password hashing
- 🔁 Password reset functionality
- 👤 User dashboard displaying their bio and skills
- 🔓 Session-based authentication
- 🎨 Responsive frontend using Jinja2 templates

---

## 📁 Project Structure

```
project/
│
├── app/
│   ├── __init__.py          # App factory, DB config, blueprint registration
│   ├── models.py            # SQLAlchemy user model
│   ├── forms.py             # WTForms for login, registration, reset
│   ├── routes.py            # All app routes and views
│   └── templates/
│       ├── base.html.j2
│       ├── homepage.html.j2
│       ├── login.html.j2
│       ├── register.html.j2
│       ├── dashboard.html.j2
│       └── forgotPass.html.j2 (expected but missing)
└── static/
    └── styles.css (referenced in base.html)
```

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- Flask-WTF (Form handling + CSRF)
- Flask-SQLAlchemy
- Jinja2 Templates
- Werkzeug for password hashing

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/skillswap.git
cd skillswap
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the root with the following:

```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3  # or your DB URI
```

### 5. Run the app

```bash
flask run
```

Navigate to `http://127.0.0.1:5000/`

---

## 💡 Future Improvements

- User profile editing
- Skill-based search and matching
- Chat/messaging between users
- Admin dashboard
- Responsive CSS / TailwindCSS / Bootstrap

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! If you'd like to contribute, please fork the repo and submit a PR.
