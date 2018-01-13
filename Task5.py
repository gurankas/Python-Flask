from flask import redirect, Flask

app = Flask(__name__)

@app.route('/robots.txt')
def deny():
    return redirect('http://httpbin.org/deny')

if __name__ == "__main__":
    app.run(debug=True)