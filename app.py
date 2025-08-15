from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample user credentials
users = {
    '1069': {'password': '7382676242', 'name': 'Agent Nikhil'},
    '1068': {'password': '8187896877', 'name': 'Agent Vasanth'},
    '1067': {'password': '7396348213', 'name': 'Agent Sri Teja'},
    '1057': {'password': '9346636182', 'name': 'Agent Ravi'},
    '1055': {'password': '9110793252', 'name': 'Agent Varun'}
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)
    
    if user and user['password'] == password:
        session['user'] = user['name']
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', name=session['user'])
    return redirect(url_for('login'))

@app.route('/careers')
def careers():
    if 'user' in session:
        return render_template('careers.html')
    return redirect(url_for('login'))

@app.route('/newsroom')
def newsroom():
    if 'user' in session:
        return render_template('newsroom.html')
    return redirect(url_for('login'))

@app.route('/mostwanted')
def mostwanted():
    if 'user' in session:
        return render_template('mostwanted.html')
    return redirect(url_for('login'))

@app.route('/missions')
def missions():
    if 'user' in session:
        return render_template('missions.html')
    return redirect(url_for('login'))

@app.route('/hierarchy')
def hierarchy():
    if 'user' in session:
        return render_template('hierarchy.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
