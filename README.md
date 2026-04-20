# Learning Log Web Application

Learning Log is a Django-based web application that allows users to record and organize what they learn about different topics. Users can create topics, add entries, and keep track of their learning journey.

This project was developed as part of my learning journey using the book **"Python Crash Course" by Eric Matthes**, specifically from the Django project section in Part II.

---

## 📌 Features

* User registration and login system
* Create learning topics
* Add entries under each topic
* Edit existing entries
* Delete existing Topic and entries
* Secure user authentication
* Admin dashboard support
* PostgreSQL database integration
* Cloud deployment support

---

## 🛠 Technologies Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* PostgreSQL (Railway Database)
* Gunicorn
* Render (Web Hosting)
* Railway (Database Hosting)

---

## 📖 Learning Source

This project was built by following the Django project tutorial from:

**Book:** *Python Crash Course*
**Author:** Eric Matthes
**Project:** Learning Log
**Part:** Part II – Django Projects

---

## 🚀 Live Demo

Live Application:

https://learning-logs-oir1.onrender.com

---

## ⚙️ Installation (Local Setup)

Follow these steps to run the project locally:

1. Clone the repository:

git clone https://github.com/Mostakim15/Learning-logs

2. Navigate into the project folder:

cd Learning-logs

3. Create virtual environment:

python -m venv env

4. Activate virtual environment:

Windows:

env\Scripts\activate

5. Install dependencies:

pip install -r requirements.txt

6. Apply migrations:

python manage.py migrate

7. Run development server:

python manage.py runserver

---

## 🗄 Database Setup

This project uses **PostgreSQL hosted on Railway**.

Make sure to set the environment variable:

DATABASE_URL=your_postgresql_database_url

Example:

DATABASE_URL=postgresql://user:password@host:port/dbname

---

## 🔐 Admin Access

To create an admin user:

python manage.py createsuperuser

Then visit:

/admin

---

## 📂 Project Structure

learning_logs/
│
├── learning_logs/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── users/
├── manage.py
├── requirements.txt
├── README.md

---

## 🎯 Purpose of This Project

This project was created to practice Django development and understand:

* Django Models
* Views and Templates
* User Authentication
* PostgreSQL Database Integration
* Cloud Deployment

---

## 👨‍💻 Author

**Md Mostakim Hossen**
Computer Science and Engineering Student
GitHub: https://github.com/Mostakim15
