from flask import Flask, render_template
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
    return render_template('alunos/lista.html', lista=lista)

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

if __name__ == '__main__':
    app.run(debug=True)