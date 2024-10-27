from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'dee935d82234b5008853b857e9c01b60'  # Ensure this is kept secure in production

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://contactzcsco:Z3r0c0575k1ll%4066202@zcsproduction.zld0i.mongodb.net/?retryWrites=true&w=majority&appName=ZCSProduction")
db = client['NCCDatabase']
users_collection = db['users']

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_collection.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash(f'Welcome, {username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        flash('You need to log in first!', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('landing_page'))

if __name__ == '__main__':
    app.run(debug=True)
