from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signal/<signal>')
def kontroll(signal):
    if signal == "fram":
        #Robottest1.forward(40)
        print("Kjører fram")
    else:
        #Robottest1.stop_all(40)
        print("Stopper")
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
