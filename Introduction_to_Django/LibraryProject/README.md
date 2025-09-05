# LibraryProject 📚

A Django-based project for managing books and library operations.

---

## 🚀 Features
- Add, edit, and delete books
- Track availability (checked out / returned)
- Manage authors and book details
- Simple and clean user interface

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd LibraryProject

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate    # On Linux / Mac
venv\Scripts\activate       # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the development server
python manage.py runserver

6. Running tests
python manage.py test

📂 Project Structure


LibraryProject/
│
├── LibraryProject/       # Django project settings
├── manage.py
├── requirements.txt
└── README.md


