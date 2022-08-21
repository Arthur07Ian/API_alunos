#Test file for database manipulation
from models import Alunos, db_session


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
    db_session.delete()



if __name__ == '__main__':
    #inserir_aluno('Arthur')
    consulta('Arthur')