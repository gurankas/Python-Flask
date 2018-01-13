from flask import redirect, Flask,render_template

app = Flask(__name__)

@app.route('/image')
@app.route('/html')
def html():
    return render_template('html.html')

if __name__ == "__main__":
    app.run(debug=True)