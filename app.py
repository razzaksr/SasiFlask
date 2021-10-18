from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def first():
    return 'Welcome to flask web development!!!!!!!!!!!!!!!!!!!!!'

@app.route('/zealous')
def second():
    return render_template('index.html')
    #return 'Zealous Tech corp offers competency level of training'

if __name__ == '__main__':
    app.run(debug=True,port=8000)