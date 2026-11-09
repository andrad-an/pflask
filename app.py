from flask import Flask, render_template, request, redirect, flash

# Importação dos DAOs
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO
from dao.matricula_dao import MatriculaDAO

app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica"


# =======================================================
# ROTAS DE NAVEGAÇÃO E PÁGINAS PRINCIPAIS
# =======================================================

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
def lista_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/turma/form')
def form_turma():
    lista_professores = ProfessorDAO().listar()
    lista_cursos = TurmaDAO().listar_cursos()
    return render_template('turma/form.html', turma=None, lista_professores=lista_professores, lista_cursos=lista_cursos)
@app.route('/turma/salvar/', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None):

    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']

    dao = TurmaDAO()
    resultado = dao.salvar(id, semestre, curso_id, professor_id)

    if resultado["status"] == "ok":
        flash("Cadastro salvo com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')
@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    lista_professores = ProfessorDAO().listar()
    lista_cursos = TurmaDAO().listar_cursos()
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)
    return render_template('turma/form.html', turma=turma, lista_professores=lista_professores, lista_cursos=lista_cursos)
@app.route('/turma/remover/<int:id>')
def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')

@app.route('/curso')
@app.route('/cursos')
def curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)



@app.route('/matricula')
@app.route('/matriculas')
def lista_matricula():
    dao = MatriculaDAO()
    lista = dao.listar()
    return render_template('matricula/lista.html', lista=lista)

@app.route('/matricula/form')
@app.route('/matriculas/form')
def form_matricula():
    lista_alunos = AlunoDAO().listar()
    lista_turmas = TurmaDAO().listar()
    return render_template('matricula/form.html', matricula=None, lista_alunos=lista_alunos, lista_turmas=lista_turmas)

@app.route('/matricula/editar/<int:id>')
@app.route('/matriculas/editar/<int:id>')
def editar_matricula(id):
    dao = MatriculaDAO()
    mat = dao.buscar_por_id(id)
    lista_alunos = AlunoDAO().listar()
    lista_turmas = TurmaDAO().listar()
    return render_template('matricula/form.html', matricula=mat, lista_alunos=lista_alunos, lista_turmas=lista_turmas)

@app.route('/matricula/salvar/', methods=['POST'])
@app.route('/matricula/salvar/<int:id>', methods=['POST'])
@app.route('/matriculas/salvar/', methods=['POST'])
@app.route('/matriculas/salvar/<int:id>', methods=['POST'])
def salvar_matricula(id=None):
    aluno_id = request.form['aluno_id']
    turma_id = request.form['turma_id']
    
    turma_info = TurmaDAO().buscar_por_id(turma_id)
    curso_id = turma_info[2] if turma_info else None

    dao = MatriculaDAO()
    result = dao.salvar(id, aluno_id, curso_id, turma_id)

    if result["status"] == "ok":
        flash("Matrícula salva com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/matricula')

@app.route('/matricula/remover/<int:id>')
@app.route('/matriculas/remover/<int:id>')
def remover_matricula(id):
    dao = MatriculaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Matrícula removida com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/matricula')



@app.route('/saudacao/<nome>')
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

@app.route('/desafio', methods=['GET', 'POST'])
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