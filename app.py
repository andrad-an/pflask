from flask import Flask, render_template, request, redirect, flash

from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO

app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica"


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/ajuda')
def ajuda():
    return render_template('dashboard/ajuda.html')

@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')



@app.route('/aluno')
@app.route('/alunos')
def lista_alunos():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('alunos/lista.html', lista=lista)

@app.route('/alunos/form')
def form_aluno():
    return render_template('alunos/form.html', aluno=None)

@app.route('/alunos/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('alunos/form.html', aluno=aluno)

@app.route('/alunos/salvar/', methods=['POST'])
@app.route('/alunos/salvar/<int:id>', methods=['POST'])
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade)

    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')

@app.route('/alunos/remover/<int:id>')
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/alunos')


@app.route('/professor')
@app.route('/professores')
def lista_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)

@app.route('/turma')
@app.route('/turmas')
def turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/curso')
@app.route('/cursos')
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