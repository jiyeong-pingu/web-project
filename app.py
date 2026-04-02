from flask import Flask, render_template, request, redirect, url_for, flash, session
import re

app = Flask(__name__)
app.secret_key = 'jizero_secret_key'  # 세션 암호화를 위한 키

# 회원 정보를 저장할 곳 (실제 DB 대신 메모리 딕셔너리 사용)
# 기본 관리자 계정 하나를 넣어둡니다.
users = {
    "admin": "1234"
}

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('profile.html', user_id=session['user_id'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('username')
        user_pw = request.form.get('password')

        if user_id in users and users[user_id] == user_pw:
            session['user_id'] = user_id
            return redirect(url_for('index'))
        else:
            flash("아이디 또는 비밀번호가 틀렸습니다.")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_id = request.form.get('username')
        new_pw = request.form.get('password')
        confirm_pw = request.form.get('confirm_password')

        # 1. 아이디 규칙 체크 (영문/숫자 4~12자)
        if not re.match("^[a-zA-Z0-9]{4,12}$", new_id):
            flash("아이디는 영문/숫자 4~12자여야 합니다.")
            return redirect(url_for('signup'))

        # 2. 아이디 중복 체크
        if new_id in users:
            flash("이미 존재하는 아이디입니다.")
            return redirect(url_for('signup'))

        # 3. 비밀번호 확인 일치 체크
        if new_pw != confirm_pw:
            flash("비밀번호가 서로 일치하지 않습니다.")
            return redirect(url_for('signup'))

        # 4. 모든 조건 통과 시 저장
        users[new_id] = new_pw
        flash("회원가입 성공! 이제 로그인해 보세요.")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)