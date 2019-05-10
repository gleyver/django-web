#import obrigatorio do views
from django.shortcuts import render, redirect
from django.http import HttpResponse

#views no django são dunções python que recebem uma requisicao do cliente e devolvem uma resposta com os dados necessarios
# Create your views here.
# toda funcao do views.py recebe como parametro um objeto do tipo  httpRequest


def index(request):
    return render(request, "index.html")


def controle(request):
    return render(request, "controle.html")


def armazenamento(request):
    return render(request, "armazenamento.html")


def disciplina(request):
    return render(request, "disciplina.html")


def consulta_aluno(request):
    # Aluno.objects.filter(nome='nome') verificar #
    aluno = Aluno.objects.all()
    return render(request, 'consulta_aluno.html', {'aluno': aluno})
    '''try:
          aluno = Aluno.objects.get(nome=nome)
     except Aluno.DoesNotExist:
          return redirect('/consulta_aluno')
     
     context = {'aluno':aluno}

     return render(request,'consulta_aluno.html',context)'''
    

def consulta_disciplina(request):
    aluno = Disciplina.objects.all()
    return render(request, 'consulta_disciplina.html', {'aluno': aluno})


def consulta_foco(request):
    nome = request.POST.get('nome')
    disciplinas = Disciplina.objects.all()
    matricula = {}
    lista = []
    for disciplina in disciplinas:
        if disciplina.nome == nome:
            lista.append(disciplina)
  
    return render(request, 'consulta_foco.html', {'alunos': lista})


def consulta_turma(request):
    nome = Turma.objects.all()
    return render(request, 'consulta_turma.html', {'nome': nome})


def consulta_professor(request):
    nome = Professor.objects.all()
    return render(request, 'consulta_professor.html', {'nome': nome})


def cadastro_aluno(request):
    return render(request, "cadastro_aluno.html")


def cadastro_disciplina(request):
    return render(request, "cadastro_disciplina.html")


def cadastro_turma(request):
    return render(request, "cadastro_turma.html")


def cadastro_professor(request):
    return render(request, "cadastro_professor.html")


def cadastro_matricula(request):
    return render(request, "cadastro_matricula.html")


def matricula(request):
    return render(request, "matricula.html")


def novo_aluno(request):
    nome = request.POST.get("nome")
    nota = request.POST.get("nota")
    Aluno.objects.create(nome=nome , nota=nota)
    return redirect("/")


def nova_turma(request):
    descricao = request.POST.get("descricao")
    id_professor = request.POST.get("professor")
    id_disciplina = request.POST.get("disciplina")
    id_aluno = request.POST.get("aluno")
    Turma.objects.create(descricao=descricao, id_professor=id_professor)
    return redirect("/")


def nova_disciplina(request):
    nome = request.POST.get('nome')
    Disciplina.objects.create(nome=nome)
    return redirect("/")


def professor(request):
    return render(request, "professor.html")


def novo_professor(request):
    nome = request.POST.get("nome")
    Professor.objects.create(nome=nome)
    return redirect("/")


def aluno(request):
    return render(request, "aluno.html")


def turma(request):
    return render(request, "turma.html")
