from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

app=Flask(__name__)
app.secret_key='yogesh'
DB_HOST='aws-0-ap-south-1.pooler.supabase.com'
DB_NAME='postgres'
DB_USER='postgres.aijwyjyqwhzmmgosaefv'
DB_PASS='Abcd#1234'
conn=psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
with conn.cursor() as cur:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
         id SERIAL PRIMARY KEY,
         full_name VARCHAR(255),
         email VARCHAR(255) UNIQUE,
         password VARCHAR(255)
    )
    """)
    conn.commit()
@app.route('/')
def home():
    return redirect('/login')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        full_name=request.form['full_name']
        email=request.form['email']
        password=request.form['password']
        if not full_name or not email or not password:
            flash("All fields are required.")
        elif len(password)<6:
            flash("Password must be at least 6 characters long.")
        else:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
                    if cur.fetchone():
                        flash("Email already exists.")
                    else:
                        hashed_password=generate_password_hash(password)
                        cur.execute("INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)", 
                                    (full_name, email, hashed_password))
                        conn.commit()
                        flash("Registration successful. You can now log in.")
                        return redirect('/login')
            except Exception as e:
                flash("Error:" + str(e))
    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
      email=request.form['email']
      password=request.form['password']
      if not email or not password:
       flash("Both fields are required.", category='error')
      else:
        try:
         with conn.cursor() as cur:
           cur.execute("SELECT * FROM users WHERE email=%s", (email,))
           user=cur.fetchone()
           if not user:
             flash("Invalid email address.", category='email_error')
           elif not check_password_hash(user[3], password):
             flash("Incorrect password.", category='password_error')
           else:
             session['user']=user[1]
             return redirect('/welcome')
        except Exception as e:
            flash(f"Error:{str(e)}", category='error')
    return render_template('login.html')
@app.route('/welcome')
def welcome():
    if 'user' not in session:
      return redirect('/login') 
    user_name=session['user']
    return render_template('welcome.html', user_name=user_name)
@app.route('/logout')
def logout():
    session.pop('user', None) 
    flash("You have been logged out.", category='success')
    return redirect('/login')
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
