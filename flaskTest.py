import sys
import subprocess
import fibonacci
import factorial


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
def main():
    return render_template('main.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    return render_template('select.html')


@app.route('/select/recursion1', methods=['GET', 'POST'])
def recursion1():
    n_value = request.args.get('n', type=int)
    print("Received input_value:", n_value)
    
    fibonacci.links.clear()
    fibonacci.fibo(n_value)
    
    return render_template('index.html', links=fibonacci.links)

@app.route('/select/recursion2',  methods=['GET', 'POST'])
def recursion2():
    n_value = request.args.get('n', type=int)
    
    factorial.links.clear()
    factorial.factorial(n_value)
    return render_template('index.html', links=factorial.links)

@app.route('/select/recursion3',  methods=['GET', 'POST'])
def recursion3():
    n_value = request.args.get('n')
    t = n_value.split("=", 1)
    n_value = int([t[0].split("?", 1)][0][0])
    list = t[1].split(",")
    if (list[0] == ''):
        del list[0]
    if(list[-1] == ''):
        del list[-1]
    for a in range(len(list)):
        list[a] = int(list[a])
    print("Received input_value:", n_value)
    print("Received list:", list)
    return render_template('recursion3.html')

@app.route('/select/recursion4',  methods=['GET', 'POST'])
def recursion4():
    n_value = request.args.get('n', type=int)
    print("Received input_value:", n_value)
    return render_template('recursion3.html')

@app.route('/howtouse')
def explain():
    return "this is to introduce how to use this site"

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)