from flask import Flask,render_template
import test

app = Flask(__name__)

@app.route('/')
def inex():
    return render_template('main.html')


@app.route('/rozetka')
def rozetka():
    return render_template('rozetka.html',sol=test.parseRozetka())

@app.route('/fozzy')
def fozzy():
    return render_template('fozzy.html',sol= test.parseFozzy())

@app.route('/bigl')
def bigl():
    return render_template('bigl.html',sol = test.parseBigl())

if __name__=='__main__':
    app.run(debug=False, port=5000, host="0.0.0.0")