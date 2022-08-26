#Test file for database manipulation
from models import USUARIOS, Alunos, db_session


def consulta(nome):
    aluno = Alunos.query.filter_by(nome=nome).first()    #For the usage of print() its necessary the first(), cause you cant print a table, just a row
    print(aluno)                                        #Alunos.query.filter_by(nome=nome) returns a 'sub-table' where nome=nome

def inserir_aluno(nome):
    aluno = Alunos(nome=nome)
    print(aluno)
    #db_session.add(aluno)
    #db_session.commit()
    aluno.save()

def excluir_aluno(nome):
    aluno = Alunos.query.filter_by(nome=nome).first()
    #db_session.delete(aluno)
    #db_session.commit()
    aluno.delete()


def inserir_usuario(username, password):
    aluno = Alunos.query.filter_by(id=2).first()
    usuario = USUARIOS(username=username, password=password, aluno=aluno)
    usuario.save()
    print(usuario)

def excluir_usuario(username):
    usuario = USUARIOS.query.filter_by(username=username).first()
    usuario.delete()
    print(usuario)



if __name__ == '__main__':
    #inserir_aluno('Arthur')
    #consulta('Arthur')
    inserir_usuario('Zezin','1234')