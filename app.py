from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')



if __name__ == '__main__':
    app.run(debug=True)


