from ast import main
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine('sqlite:///alunos.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Alunos(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)


    # Parameter/Column that is gonna represent the row (the student) when printed (or something like that)
    def __repr__(self):
        return '<Aluno {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Cursos(Base):
    __tablename__='cursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    pessoa = relationship("Alunos")

    def __repr__(self):
        return '<Curso {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()