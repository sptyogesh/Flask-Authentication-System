# 🖥️ **Flask User Authentication System**

Welcome to the **Flask User Authentication System** project! 🚀 This is a simple web application built with Flask, allowing users to register, log in, and securely authenticate with their credentials. The project uses a PostgreSQL database and includes a registration and login page for user authentication.

---

## 🌟 Features

- **User Registration**: Users can create an account with a full name, email, and password.
- **Secure Login**: Users can log in with their credentials, with password encryption for security.
- **Flash Messages**: Real-time feedback for users, indicating success, error, and validation messages.
- **Session Management**: Users can stay logged in during their session and log out safely.

---

## 📚 Tech Stack

- **Frontend**: HTML, CSS (via Flask templating)
- **Backend**: Python with Flask
- **Database**: PostgreSQL (hosted on Supabase)
- **Authentication**: Secure password hashing with `werkzeug.security`
- **Hosting**: Can be deployed on platforms like PythonAnywhere, Heroku, or others.

---

## ⚙️ Setup and Installation

To get started with this project, follow the steps below:

### 1. Clone the repository 📂

First, clone the project to your local machine using Git.

```bash
git clone https://github.com/yourusername/flask-user-authentication.git
cd flask-user-authentication
```

### 2. Install Dependencies 📦

Make sure you have **Python 3.x** installed on your machine. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL Database 🗄️

   1. Create a PostgreSQL database and note the connection credentials (host, username, password).
   2. Update the database credentials in app.py.

### 4. Run the Application 🚀
Now you’re ready to run the Flask app! Start the development server:

```bash
python app.py
```
Access the app at http://127.0.0.1:5000 in your browser.

---

## 📝 **How It Works ** ⚙️

1. **User Registration** 📝
  - Form Fields: Full Name, Email, Password.
  - Validation:
    All fields are required.
    Password should be at least 6 characters.
    Email must be unique.
  - Password Hashing: The password is hashed before storing it in the database for security.
2. **User Login** 🔐
  - Users log in using their email and password.
  - The system checks the entered password by comparing it to the stored hashed password.
  - Upon successful login, users are redirected to the Welcome Page.
3. **Session Management** 💼
  - Once logged in, the user’s session is stored using Flask’s session object.
  - Users can stay logged in across different pages.
  - A logout button is available to clear the session and log out the user.

---

## 📅 **Database Schema**

The PostgreSQL database has a single table named `users` with the following schema:

| Field        | Type       | Description                          |
|--------------|------------|--------------------------------------|
| **id**       | SERIAL     | Primary Key, Auto Increment          |
| **full_name**| VARCHAR(255) | User’s full name                     |
| **email**    | VARCHAR(255) | Unique email address                 |
| **password** | VARCHAR(255) | Hashed password                      |

---
