from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Flask está funcionando!'

@app.route('/sobre')
def sobre():
    return 'Sobre o sistema'



if __name__ == '__main__':
    app.run(debug=True)


