from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/alunos')
def lista_alunos():
    lista = [
        (1, "Abel Nunes Vieira", 18, "THE"),
        (2, "Beatriz Lima Vasconcelos", 19, "THE"),
        (3, "Carlos Eduardo de Sousa", 20, "THE"),
        (4, "Daniela Fontes Carvalho", 18, "THE"),
        (5, "Gabriel Henrique Mesquita", 21, "THE"),
        (6, "Isabela Cristina Nogueira", 19, "THE"),
        (7, "Lucas Gabriel Ferreira", 22, "THE"),
        (8, "Mariana Rocha Albuquerque", 18, "THE"),
        (9, "Mateus Vinícius Ribeiro", 20, "THE"),
        (10, "Kelson Andre Veloso Moura Paiva", 18, "THE"),
    ]
    return render_template('alunos/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    return render_template('professor/lista.html')

if __name__ == '__main__':
    app.run(debug=True)