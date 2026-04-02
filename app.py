from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # 세션을 위한 비밀키

# 임시 사용자 저장소 (아이디: 비밀번호)
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        users[user_id] = user_pw
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        if user_id in users and users[user_id] == user_pw:
            session['user'] = user_id
            return redirect(url_for('profile'))
        else:
            flash('아이디 또는 비밀번호가 틀렸습니다.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'user' in session:
        return render_template('profile.html', user_id=session['user'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
