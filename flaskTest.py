import sys
import subprocess


try:
    # 없는 모듈 import시 에러 발생
   from flask import Flask, make_response, redirect, render_template, request, session, url_for
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'Flask'])
    # 다시 import
    from flask import Flask, render_template
    
try:
    import pyrebase
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pyrebase'])
    # 다시 import
    import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBM3snbMYD3bZMX8QJjP1i7aIgWVDwaYBw",
  "authDomain": "jnu-server.firebaseapp.com",
  "projectId": "jnu-server",
  "storageBucket": "jnu-server.appspot.com",
  "messagingSenderId": "782346831123",
  "appId": "1:782346831123:web:c4488ea561ae50bda906e6",
  "measurementId": "G-LY5D9LX4CV"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main1', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return redirect(url_for('test'))
    return render_template('main1.html')
 
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/howtouse')
def explain():
    return "this is to introduce how to use this site"

if __name__ == '__main__':
    app.run(debug=True)