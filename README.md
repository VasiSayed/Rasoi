# Rasoi
🍲 Rasoi App – Your Personal Recipe Manager
Rasoi App is a Django-powered web application that lets users manage their own digital recipe book with ease. Whether you're cooking up breakfast, lunch, or dinner, Rasoi helps you store, update, and revisit your favorite recipes — all while tracking your cooking history!

✨ Features
👤 User Authentication – Secure registration, login, and logout system

📝 Recipe CRUD – Create, edit, view, and soft-delete your personal recipes

🍛 Filter Recipes – Filter by veg/non-veg or meal type (breakfast, lunch, dinner)

⏱️ Cooking History – Track when you last made a recipe

🎲 Random Suggestions – Get a recipe you haven’t made in the last 5 days

📧 Welcome Email – New users receive a personalized welcome email

⚠️ Interactive Alerts – Success & warning messages powered by Django’s message framework

🔐 Tech Stack
Backend: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Extras: Django Messages, Email Sending (SMTP)

🛠️ Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/rasoi-app.git
cd rasoi-app
Create a virtual environment & install dependencies

bash
Copy
Edit
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
Apply migrations & run the server

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
