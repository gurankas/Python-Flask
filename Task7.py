from flask import request, Flask,render_template

app = Flask(__name__)

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