from flask import Flask, render_template, request 
import sqlite3
from dao.curso_dao import CursoDAO
from dao.db_config import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO

app = Flask(__name__)

DB_PATH = 'banco_escola.db'

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')
@app.route('/alunos')
def lista_alunos():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)

@app.route('/ajuda')
def ajuda():
    return render_template('dashboard/ajuda.html')

@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

@app.route('/turma')
def turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/curso')
def curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    dados = f"Usuário: {usuario}, Senha: {senha}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio1', methods=['GET', 'POST'])
def desafio1():
    if request.method == 'POST':
        dados_cadastro = {
            'nome': request.form['nome'],
            'data_nascimento': request.form['data_nascimento'],
            'cpf': request.form['cpf'],
            'nome_mae': request.form['nome_mae']
        }
        return render_template('desafio/resultado.html', dados=dados_cadastro)
    
    return render_template('desafio/form.html')

if __name__ == '__main__':
    app.run(debug=True)