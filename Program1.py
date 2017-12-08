from flask import Flask

name = "singh"
list_of_numbers = [12,14,35,76,23,75,4,888]
def table_of_four():
    print('This is a program to fnd multiples of 4 from 1 to 100')
    name = "Gurankas"
    for x in range(1, 101):
        if x % 4 is 0:
            print(x)
    print(name)

table_of_four()

def addition(*args):
    total = 0;
    for x in args:
        total += x
    print(total)
    return total


addition(*list_of_numbers)

app = Flask(__name__)

@app.route('/')
def index():
    print("The index page will display the sum of pre existing numbers")
    print("The sum of numbers is")
    addition(*list_of_numbers)
    return '<h3>The sum of the numbers is %s</h3>' % addition(*list_of_numbers)


if __name__ == "__main__":
    app.run(debug=True)