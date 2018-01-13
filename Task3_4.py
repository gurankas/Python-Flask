from flask import Flask, render_template
from flask import request,make_response, redirect

app = Flask(__name__)

@app.route('/setcookie', methods = ['GET','POST'])
def setcookie():
    return render_template('setcookie.html')

@app.route('/submitted', methods = ['POST'])
def submitted():
    name = request.form['name']
    age = request.form['age']
    resp = make_response(render_template("submitted.html"))
    resp.set_cookie('name', name)
    resp.set_cookie('age', age)
    return resp


@app.route('/getcookie', methods = ['GET', 'POST'])
def getcookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    return render_template('getcookie.html', name=name, age=age)

@app.route('/robots.txt')
def deny():
    return redirect('http://httpbin.org/deny')

@app.route('/image')
@app.route('/html')
def html():
    return render_template('html.html')

@app.route('/input', methods = ['POST', 'GET'])
def input():
    return render_template('form.html')

@app.route('/output', methods=['POST'])
def output():
    weakness = request.form['weakness']
    print(weakness)
    return render_template('output.html', weakness=weakness)

if __name__ == "__main__":
    app.run(debug=True)