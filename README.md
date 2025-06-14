# 👶 KidKeeper – Attendance Management System

**KidKeeper** is a Django-based web application designed to help organizations or institutions manage kids' data and track daily attendance efficiently.

---

## 🎯 Features

- 📋 Add, Edit, and Delete Kid Profiles  
- 📆 Take Daily Attendance with Checkboxes  
- 🗂️ View Attendance Summary by Date  
- 📊 See List of Present Kids on Specific Dates  
- 🧮 Auto Age Calculation from Birthdate  
- 🖥️ Responsive Frontend using HTML + CSS

---

## 📸 Screenshots

| Dashboard | Take Attendance | Attendance Summary | Daily Records |
|----------|----------------|---------------------|----------------|
| _Upload your screenshots here_ |

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS  
- **Backend**: Django (Python)  
- **Database**: SQLite  
- **Templating Engine**: Django Templates  

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/kidkeeper.git
cd kidkeeper
python -m venv venv
source venv/bin/activate   # for Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
