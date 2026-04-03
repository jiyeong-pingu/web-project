from flask import Flask, render_template, request, redirect, url_for, flash, session
import re

app = Flask(__name__)
app.secret_key = 'jizero_secret_key'

# 임시 회원 저장소
users = {"admin": "1234"}

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('profile.html', user_id=session['user_id'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # HTML의 name="username"과 일치시켜야 함
        user_id = request.form.get('username', '').strip()
        user_pw = request.form.get('password', '').strip()

        if user_id in users and str(users[user_id]) == str(user_pw):
            session['user_id'] = user_id
            return redirect(url_for('index'))
        else:
            flash("아이디 또는 비밀번호가 올바르지 않습니다.")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_id = request.form.get('username', '').strip()
        new_pw = request.form.get('password', '').strip()
        confirm_pw = request.form.get('confirm_password', '').strip()

        # 1. 중복 체크 (지영님 요청사항!)
        if new_id in users:
            flash("이미 사용 중인 아이디입니다.")
            return redirect(url_for('signup'))

        # 2. 유효성 검사 (영문/숫자 4~12자)
        if not re.match("^[a-zA-Z0-9]{4,12}$", new_id):
            flash("아이디 규칙을 확인해 주세요.")
            return redirect(url_for('signup'))

        if new_pw != confirm_pw:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for('signup'))

        # 저장 및 성공 문구와 함께 이동
        users[new_id] = new_pw
        flash("회원가입 성공! 이제 로그인해 보세요.")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
