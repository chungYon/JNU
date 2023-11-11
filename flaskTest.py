import sys
import subprocess
import fibonacci


try:
    # 없는 모듈 import시 에러 발생
   from flask import Flask, make_response, redirect, render_template, request, session, url_for
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'Flask'])
    # 다시 import
    from flask import Flask, make_response, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", links=fibonacci.links)

@app.route('/main1')
def main1():
    return render_template('main1.html')

@app.route('/main')
def main():
    return render_template('main.html')
 
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    return render_template('select.html')

@app.route('/howtouse')
def explain():
    return "this is to introduce how to use this site"

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)